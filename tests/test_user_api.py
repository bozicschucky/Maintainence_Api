import unittest

import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        print("==> starting up the env tests")
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        self.dummy_data = {'id': 10, 'request': 'I am requesting a car fix',
                           "status": True, "request_type": "repair", "request_details": "This the description"}

    def tearDown(self):
        print("==>Tearing down after tests!")

    def test_get_user_request(self):
        """Test user can get a request after creating one"""
        resp = self.app.post('/api/v1/user/request/10', json={'id': 10, "request": "iam requesting", "status": True,
                                                              "request_type": "repair",
                                                              "request_details": "This the description"})
        self.assertEqual(resp.status_code, 201)
        resp = self.app.get('/api/v1/user/request/10')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('10', str(resp.data))
        self.assertIn('repair', str(resp.data))

    def test_api_all_user_request(self):
        resp = self.app.post('/api/v1/user/request/10', json={'id': 10, "request": "iam requesting", "status": True,
                                                              "request_type": "repair",
                                                              "request_details": "This the description"})
        self.assertEqual(resp.status_code, 201)
        resp = self.app.get('/api/v1/user/requests')
        assert resp.status_code, 200
        assert resp.headers['content-type'] == 'application/json'
        self.assertIn('10', str(resp.data))
        self.assertIn('iam requesting', str(resp.data))

    def test_api_create_request(self):
        """Test user can get a request after creating one"""
        resp = self.app.post('/api/v1/user/request/10', json={'id': 10, "request": "iam requesting", "status": True,
                                                              "request_type": "repair",
                                                              "request_details": "This the description"})
        self.assertEqual(resp.status_code, 201)
        resp = self.app.get('/api/v1/user/request/10')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('10', str(resp.data))
        self.assertIn('repair', str(resp.data))

    def test_api_update_request(self):
        resp = self.app.post('/api/v1/user/request/10', json={'id': 10, "request": "iam requesting", "status": True,
                                                              "request_type": "repair",
                                                              "request_details": "This the description"})
        self.assertEqual(resp.status_code, 201)
        resp = self.app.put('/api/v1/user/request/10', json={'id': 10, "request": "iam requesting", "status": True,
                                                             "request_type": "repair",
                                                             "request_details": "This is updated"})
        self.assertEqual(resp.status_code, 200)
        self.assertIn("This is updated", str(resp.data))

    def test_api_delete_request(self):
        resp = self.app.delete('/api/v1/user/request/1')
        self.assertEqual(resp.status_code, 202)
        self.assertNotIn(b'id', resp.data)
        self.assertIn(b'Message', resp.data)
        self.assertIn("Item deleted", str(resp.data))
        assert resp.status_code, 202
