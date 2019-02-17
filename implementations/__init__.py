import os
from dotenv import load_dotenv
from importlib import import_module

load_dotenv()
CLIENT = os.getenv('CLIENT')

implementation = import_module(f'.{CLIENT}', __name__)