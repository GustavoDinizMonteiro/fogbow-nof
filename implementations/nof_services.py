import os
from imp import load_source
from dotenv import load_dotenv

CLIENT = os.getenv('CLIENT')

implementation = load_source(CLIENT, './')

def create_local(request, path):
    return implementation.create_local(request, path)


def create_remote(request, path):
    return implementation.create_remote(request, path)