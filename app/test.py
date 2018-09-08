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
        response = dummy.put('/orders/60', data=json.dumps({"order_status": "Tests"}),
                             content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = dummy.put('/orders/000000', data=json.dumps({"order_status": "Tests"}),
                             content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_client_get(self):
        '''
                Testing if the GET  requests return the proper status codes
        '''
        dummy = APP.test_client(self)
        self.assertEqual(dummy.get('/orders').status_code, 200)  # OK
        self.assertEqual(dummy.get('/orders/12').status_code, 200)
        self.assertEqual(dummy.get('/orders/204863').status_code, 200)
        self.assertEqual(
            dummy.get('/orders/23516648').status_code, 404)  # Not Found
        self.assertEqual(
            dummy.get('/orders/ericmwachala').status_code, 404)
        self.assertEqual(dummy.get('/order/204863').status_code, 404)
        self.assertEqual(dummy.get('/orders/12').status_code, 200)

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
