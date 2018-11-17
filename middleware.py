import os
import requests
from dotenv import load_dotenv

load_dotenv()

API = os.getenv('API')

__all__ = ['resend']

def resend(request, path):
    return requests.request(request.method, API+path, data=request.data, headers=request.headers)