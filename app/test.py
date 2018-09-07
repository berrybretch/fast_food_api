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
        payload = {"order_id": 000000000,
                   "order_content": "TestChicken",
                   "user": "Test",
                   "order_status": "Tests"
                   }
        response = dummy.post('/orders',  data=json.dumps(payload),
                              content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
