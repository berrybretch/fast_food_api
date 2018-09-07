import unittest
import json
from app import api

'''
Tests for Api endpoints
'''


class TestEndpoints(unittest.TestCase):

    def test_client_post(self):
        '''
                Testing if the GET  requests return the proper status codes
        '''
        dummy = api.APP.test_client(self)
        payload = {"order_id": 19,
                   "order_content": "Little Chicken",
                   "user": "Eric",
                   "order_status": "Denied",
                   }
        response = dummy.post(json.dumps(payload), headers={
                              'content_type': 'application/json'})
        self.assertEqual(response.status_code, 200)
