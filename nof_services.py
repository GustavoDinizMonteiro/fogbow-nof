import os
import requests
from dotenv import load_dotenv
from implementations import implementation

load_dotenv()
ENV = os.getenv('ENV')
API = os.getenv('PROVIDER_API')
LOCAL_MEMBER = os.getenv('NOF_MEMBER')

resource_cannot_be_providede_response = {
    'content': 'It was not possible to fulfill your request.',
    'status_code': 404
}


def get_requester_from_req(request):
    return implementation.get_requester_from_req(request)

def resend(request, path):
    # NOTE: send headers crash requests in Postman mock API
    headers = {} if ENV == 'dev' else request.headers
    return requests.request(
        request.method, 
        API+path, 
        data=request.data, 
        headers=headers, 
        allow_redirects=True)

def member_has_quota(member):
    pass

def get_members_with_less_quota(member):
    pass

def get_current_orders_from_member(member):
    pass

def preempt_order(order):
    pass

def create_local(request, path):
    requester = get_requester_from_req(request)
    if requester == LOCAL_MEMBER:
        return resend(request, path)
    has_quota = member_has_quota(requester)
    if not has_quota:
        return resource_cannot_be_providede_response
    create_local_resp = implementation.create_local(request, path)
    if create_local_resp.status_code < 400:
        return create_local_resp
    members = get_members_with_less_quota(requester)
    for member in members:
        orders = get_current_orders_from_member(member)
        for order in orders:
            preempt_order(order)
            create_local_resp = implementation.create_local(request, path)
            if create_local_resp.status_code < 400:
                return create_local_resp
    return resource_cannot_be_providede_response
    
    
    
    



