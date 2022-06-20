import unittest
from app import create_app

class BaseTestClass(unittest.TestCase):
    def setUp(self):
        self.app = create_app(settings_module="config.testing")
        self.client = self.app.test_client()
    
    def tearDown(self):
        print("Finish Test")