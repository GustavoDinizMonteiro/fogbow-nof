import requests

__all__ = ['resend']

API = 'http://localhost:3000/'

def resend(request, path):
    return requests.request(request.method, API+path, data=request.data, headers=request.headers)