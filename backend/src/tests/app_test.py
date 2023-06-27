import pytest
from flask import Flask
from flask_testing import TestCase

from server.app import app

class MyTest(TestCase):
    def create_app(self):
        return app
    
    def test_index_route(self):
        response = self.client.get("/api/")
        self.assert200(response)
        self.assertEqual(response.json, {"api_version": "1.0.0"})