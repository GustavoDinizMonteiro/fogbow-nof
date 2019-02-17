import os
import requests
from dotenv import load_dotenv

API = os.getenv('PROVIDER_API')

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
        # preempt
        # try create again and preempt until there are not
        # member options to try.
        pass
    
    return {
        'content': 'It was not possible to fulfill your request.',
        'status_code': 404
    }


def try_create_remote_order():
    pass