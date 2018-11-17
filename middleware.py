import requests

__all__ = ['resend']

API = 'http://localhost'

def resend(request, path):
    return requests.request((request.method, ''.join(API, path),
                     data=request.data, headers=request.headers))
