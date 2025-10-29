import json
from datetime import datetime
from django.utils.dateparse import parse_datetime
from django.test import TestCase
from .models import Account

class AccountViewTestCase(TestCase):
    def test_post_accounts(self):
        """POST /api/accounts with valid inputs"""
        body = { 'name': 'Account 3' }
        response = self.client.post(
            '/api/accounts/',
            data=json.dumps(body),
            content_type='application/json'
        )
        data = json.loads(response.content.decode())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data, {
            'id': data['id'],
            'name': 'Account 3',
            'balance': 0,
            'created_at': data['created_at']
        })
        self.assertTrue(isinstance(data['id'], int))
        self.assertTrue(isinstance(parse_datetime(data['created_at']), datetime))

    def test_get_accounts(self):
        """GET /api/accounts"""
        response = self.client.get('/api/accounts/')
        data = json.loads(response.content.decode())
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(data, list))

class TransactionViewTestCase(TestCase):
    def test_post_transactions(self):
        """POST /api/transactions with valid inputs"""
        body = {
            'receiver_id': 2,
            'payer_id': 1,
            'value': 50
        }
        response = self.client.post(
            '/api/transactions/',
            data=json.dumps(body),
            content_type='application/json'
        )
        data = json.loads(response.content.decode())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data, {
            'id': data['id'],
            'receiver_id': 2,
            'payer_id': 1,
            'value': 50,
            'date': data['date']
        })
        self.assertTrue(isinstance(data['id'], int))
        self.assertTrue(isinstance(parse_datetime(data['date']), datetime))