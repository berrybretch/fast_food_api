import unittest
import requests
from flask import Flask
from app import api
'''
Tests for PUT requests
'''


class TestPut(unittest.TestCase):

    def test_put(self):
        '''
                Test status code returns
        '''
        payload = {'order_status': 'Test'}
        dummy = requests.put(
            'http://127.0.0.1:5000/orders/204863', json=payload)
        self.assertEqual(dummy.status_code, 200)
        dummy = requests.put(
            'http://127.0.0.1:5000/orders/missing', json=payload)
        self.assertEqual(dummy.status_code, 404)

    def test_content(self):
        '''
                Tests the json result
        '''
        payload = {'order_status': 'TestPhrase'}
        dummy = requests.put(
            'http://127.0.0.1:5000/orders/204863', json=payload)
        self.assertIn('TestPhrase', dummy.text)
