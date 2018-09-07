import unittest
import json
from flask import Flask
from app import APP
'''
Tests for PUT requests
'''


class TestPut(unittest.TestCase):

    def test_put(self):
        '''
                Test status code returns
        '''
        dummy = APP.test_client(self)
        payload = {"order_status": "Tests"}

       # response = dummy.put(
        #    '/orders/204863', data=json.dumps(payload), content_type='application/json')
        response = dummy.put('/orders/60',  data=json.dumps({"order_status": "Tests"}),
                             content_type='application/json')
        print(response)
        self.assertEqual(response.status_code, 200)
