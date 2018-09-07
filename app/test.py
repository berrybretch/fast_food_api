import unittest
import requests
from app import api

'''
Tests for Api endpoints
'''


class TestEndpoints(unittest.TestCase):

    def test_client_post(self):
        '''
                Testing if the POST  requests return the proper status codes
        '''
        payload = {"order_id": 19,
                   "order_content": "TestPhrase",
                   "user": "testphrase",
                   "order_status": "testphrase",
                   }
        url = 'http://127.0.0.1:5000/orders'
        dummy = requests.post(url, json=payload)
        self.assertEqual(dummy.status_code, 200)

    def test_post_content(self):
        '''
        Test the content of the POST request
        '''
        payload = {"order_id": 900,
                   "order_content": "TestPhraseOne",
                   "user": "testphraseTwo",
                   "order_status": "testphraseThree",
                   }
        url = 'http://127.0.0.1:5000/orders'
        dummy = requests.post(url, json=payload)
        self.assertIn('TestPhraseOne', dummy.text)
        self.assertIn('testphraseTwo', dummy.text)
        self.assertIn('testphraseThree', dummy.text)
