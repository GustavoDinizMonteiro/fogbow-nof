import os
import requests
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

def preempt_order(order):
    pass

def get_current_orders_from_member(member):
    pass

def get_current_quota_used(member):
    pass