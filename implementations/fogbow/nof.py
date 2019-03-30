import os
import requests
from dotenv import load_dotenv
from implementations.fogbow.accounting import get_members_with_more_debt

API = os.getenv('PROVIDER_API')

resource_cannot_be_providede_response = {
    'content': 'It was not possible to fulfill your request.',
    'status_code': 404
}

__all__ = ['create_local', 'create_remote']

def create_local(request, path):
    try_local_reponse = requests.post(
        API+path,
        data=request.data, 
        headers=request.headers,
        allow_redirects=True
    )

    if (try_local_reponse.status_code < 400):
        return try_local_reponse
    else:
        # preempt any order, including local if necessary
        # try create again and preempt until there are not
        # member options to try.
        member = '' # TODO: initialize this variable
        member_list = get_members_with_more_debt(member)
        # get orders from this members and preempt it

    
    return resource_cannot_be_providede_response


def create_remote(request, path):
    # check if cloud has request resource available
    # check if member has quota
    try_local_reponse = requests.post(
        API+path,
        data=request.data, 
        headers=request.headers, 
        allow_redirects=True
    )
    if (try_local_reponse.status_code < 400):
        return try_local_reponse
    else:
        # preempt orders from other members, and only if you 
        # debit with it is less than the existing one of 
        # the owner of the current order.
        # try create again and preempt until there are not
        # members options to try.
        pass
    return resource_cannot_be_providede_response