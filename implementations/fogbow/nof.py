import os
import requests
from json import loads
from dotenv import load_dotenv
from implementations.fogbow.accounting import get_members_with_more_debt

API = os.getenv('PROVIDER_API')

resource_cannot_be_providede_response = {
    'content': 'It was not possible to fulfill your request.',
    'status_code': 404
}

def create_local(request, path):
    return requests.post(
        API+path,
        data=request.data, 
        headers=request.headers,
        allow_redirects=True
    )

def dispatch_remote_request(request, path):
    pass

def preempt_order(order):
    pass

def get_provider_from_req(req):
    return loads(req.data).get('provider')

def get_requester_from_req(req):
    return req.headers.get('requester')

def get_current_orders_from_member(member):
    req = requests.get(
        API+'computes/status'
    )
    f = lambda x: x.state == 'READY' and x.provider == member
    return list(filter(f, req.data))

def get_current_quota_used(member):
    req = requests.get(
        API+'computes/status'
    )
    f = lambda x: x.state == 'READY' and x.provider == member
    orders = len(list(filter(f, req.content)))