import unittest
import json
from flask import Flask, request
from app import api

'''
Tests for Api endpoints
'''


class TestEndpoints(unittest.TestCase):

    def test_post_status_codes(self):
        dummy = api.APP.test_client(self)
        response = dummy.post('/orders', data={"order_id": 60,
                                               "order_content": "Little Chicken",
                                               "user": "Eric",
                                               "order_status": "Denied",
                                               })
        self.assertEqual(response.status_code, 200)

        #{"order_id": 60,
        #"order_content": "Little Chicken",
        #"user": "Eric",
        #"order_status": "Denied",
        #}
