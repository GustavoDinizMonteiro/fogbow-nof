import os
import requests
from dotenv import load_dotenv
from implementations import ServiceImplementation
from db import get_members_data, get_member_data

load_dotenv()

ENV = os.getenv('ENV')
API = os.getenv('PROVIDER_API')
LOCAL_MEMBER = os.getenv('NOF_MEMBER')
implementation = ServiceImplementation()

resource_cannot_be_providede_response = {
    'content': 'It was not possible to fulfill your request.',
    'status_code': 404
}

def resend(request, path):
    return requests.request(
        request.method, 
        API+path, 
        data=request.data, 
        headers=request.headers, 
        allow_redirects=True)

def member_has_quota(member):
    member_data = get_member_data(member)
    # TODO: define a default value for this.
    used_quota = implementation.get_current_quota_used(member_data)
    return True

def get_members_with_less_quota(member):
    member_data = get_member_data(member)
    f = lambda x: x.justice < member_data.justice
    return list(filter(f, get_members_data()))

def preempt_order(order):
    return implementation.preempt_order(order)

# TODO: check this method
def create(request, path):
    if path == 'remote-request':
        return create_remote(request, path)
    provider = implementation.get_provider_from_req(request)
    if provider == LOCAL_MEMBER:
        return resend(request, path)
    return create_local(request, path)
    

def create_local(request, path):
    requester = implementation.get_requester_from_req(request)
    has_quota = member_has_quota(requester)
    if not has_quota:
        return resource_cannot_be_providede_response
    create_local_resp = implementation.create_local(request, path)
    if create_local_resp.status_code < 400:
        return create_local_resp
    members = get_members_with_less_quota(requester)
    for member in members:
        orders = implementation.get_current_orders_from_member(member)
        for order in orders:
            preempt_order(order)
            create_local_resp = implementation.create_local(request, path)
            if create_local_resp.status_code < 400:
                return create_local_resp
    for member in members:
        create_remote_resp = implementation.dispatch_remote_request(request, path)
        if create_remote_resp.status_code < 400:
            return create_remote_resp 

def create_remote(request, path):
    requester = implementation.get_requester_from_req(request)
    has_quota = member_has_quota(requester)
    if not has_quota:
        return resource_cannot_be_providede_response
    create_local_resp = implementation.create_local(request, path)
    if create_local_resp.status_code < 400:
        return create_local_resp
    members = get_members_with_less_quota(requester)
    for member in members:
        orders = implementation.get_current_orders_from_member(member)
        for order in orders:
            preempt_order(order)
            create_local_resp = implementation.create_local(request, path)
            if create_local_resp.status_code < 400:
                return create_local_resp
    return resource_cannot_be_providede_response
