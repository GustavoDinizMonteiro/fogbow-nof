import os
import requests
from dotenv import load_dotenv

API = os.getenv('PROVIDER_API')

resource_cannot_be_providede_response = {
    'content': 'It was not possible to fulfill your request.',
    'status_code': 404
}

def try_create(request, path):
    try_local_reponse = requests.post(
        API+path,
        data=request.data, 
        headers=request.headers, 
        allow_redirects=True
    )

    if (try_local_reponse.status_code < 400):
        return try_local_reponse
    else:
        # preempt any order, including location if necessary
        # try create again and preempt until there are not
        # member options to try.
        pass
    
    return resource_cannot_be_providede_response


def try_create_remote_order(request, path):
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