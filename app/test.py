import unittest
import requests
from app import api

'''
Tests for Api endpoints
'''


class TestEndpoints(unittest.TestCase):

    def test_client_post(self):
        '''
                Testing if the GET  requests return the proper status codes
        '''
        payload = {"order_id": 19,
                   "order_content": "Little Chicken",
                   "user": "Eric",
                   "order_status": "Denied",
                   }
