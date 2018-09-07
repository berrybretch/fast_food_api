import unittest
from flask import Flask  
import json
from app import APP
class TestPost(unittest.TestCase):


    def test_client_post(self):
        '''
                Testing if the POST requests return the proper status codes
        '''
        dummy = APP.test_client(self)
        payload = {"order_id": 19,
                   "order_content": "Little Chicken",
                   "user": "Eric",
                   "order_status": "Denied",
                   }
        response = dummy.post(json.dumps(payload), headers={
                              'content_type': 'application/json'})
        self.assertEqual(response.status_code, 200)
