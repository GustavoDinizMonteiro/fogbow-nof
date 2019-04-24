import os
from dotenv import load_dotenv
from importlib import import_module

load_dotenv()
CLIENT = os.getenv('CLIENT')

implementation = import_module(f'.{CLIENT}', __name__)

class ServiceImplementation:
    def __init__(self):
        self.implementation = import_module(f'.{CLIENT}', __name__)

    def get_provider_from_req(self, request):
        return self.implementation.get_provider_from_req(request)
    

    def get_requester_from_req(self, request):
        return self.implementation.get_requester_from_req(request)
    
    def create_local(self, request, path):
        return self.implementation.create_local(request, path)


    def get_current_orders_from_member(self, member):
        return self.implementation.get_current_orders_from_member(member)
    

    def preempt_order(self, order):
        return self.implementation.preempt_order(order)
    

    def get_current_quota_used(self, member):
        return self.implementation.get_current_quota_used(member)