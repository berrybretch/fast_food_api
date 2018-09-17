import unittest
import json
from flask import Flask
from app import APP
'''
Tests for PUT requests
'''


class TestPut(unittest.TestCase):

    def test_client_get(self):
        '''
                Testing if the GET  requests return the proper status codes
        '''
        dummy = APP.test_client(self)
        self.assertEqual(dummy.get('/api/v1/orders').status_code, 200)  # OK
        self.assertEqual(dummy.get('/api/v1/orders/12').status_code, 200)
        self.assertEqual(dummy.get('/api/v1/orders/204863').status_code, 200)
        self.assertEqual(
            dummy.get('/api/v1/orders/23516648').status_code, 404)  # Not Found
        self.assertEqual(
            dummy.get('/api/v1/orders/ericmwachala').status_code, 404)
        self.assertEqual(dummy.get('/api/v1/order/204863').status_code, 404)
        self.assertEqual(dummy.get('/api/v1/orders/12').status_code, 200)
        self.assertNotEqual(dummy.get('/api/v1/orders/12').status_code, 400)
        self.assertTrue(
            dummy.get('/api/v1/orders/204863').status_code == 200)
        self.assertFalse(
            dummy.get('/api/v1/orders/204863').status_code == 400)

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
        response = dummy.post('/api/v1/orders',  data=json.dumps(payload),
                              content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_put(self):
        '''
                Test status code returns
        '''
        dummy = APP.test_client(self)
        response = dummy.put('/api/v1/orders/60', data=json.dumps({"order_status": "Tests"}),
                             content_type='application/json')
        self.assertEqual(response.status_code, 200)
