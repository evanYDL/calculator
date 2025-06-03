import unittest
import threading
import json
from http.server import HTTPServer
from urllib.request import urlopen
from server import CalcHandler

class TestServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.port = 8001
        cls.httpd = HTTPServer(('localhost', cls.port), CalcHandler)
        cls.thread = threading.Thread(target=cls.httpd.serve_forever)
        cls.thread.daemon = True
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.thread.join()
        cls.httpd.server_close()

    def test_calc_endpoint(self):
        from urllib.parse import quote_plus
        expr = quote_plus('1+2*3')
        with urlopen(f'http://localhost:{self.port}/calc?expr={expr}') as resp:
            data = json.loads(resp.read().decode())
        self.assertEqual(data['result'], 7)

if __name__ == '__main__':
    unittest.main()
