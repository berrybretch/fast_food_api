import unittest
from flask import Flask
from api import *

'''
Tests for Api endpoints
'''


class Test_Endpoints(unittest.TestCase):

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
