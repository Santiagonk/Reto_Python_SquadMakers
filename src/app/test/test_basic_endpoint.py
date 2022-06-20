from . import BaseTestClass

class TestBasicEndPoint(BaseTestClass):
    def test_main_endpoint(self):
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
    
    def test_jokes_endpoint(self):
        res = self.client.get('/jokes/')
        self.assertEqual(200, res.status_code)
    
    def test_jokes_dad_endpoint(self):
        res = self.client.get('/jokes/Dad')
        self.assertEqual(200, res.status_code)
    
    def test_jokes_chuck_endpoint(self):
        res = self.client.get('/jokes/Chuck')
        self.assertEqual(200, res.status_code)