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

       # response = dummy.put(
        #    '/orders/204863', data=json.dumps(payload), content_type='application/json')
        response = dummy.put('/orders/60',  data=json.dumps({"order_status": "Tests"}),
                             content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = dummy.put('/orders/000000',  data=json.dumps({"order_status": "Tests"}),
                             content_type='application/json')
        self.assertEqual(response.status_code, 404)
