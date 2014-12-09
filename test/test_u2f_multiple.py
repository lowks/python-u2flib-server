import unittest
from u2flib_server import u2f_multiple as u2f
from soft_u2f_v2 import SoftU2FDevice

APP_ID = 'http://www.example.com/appid'
FACET = 'https://www.example.com'
FACETS = [FACET]


class MyTestCase(unittest.TestCase):  # TODO: Use Nosetest instead of unittest
    def test_register_soft_u2f(self):
        token = SoftU2FDevice()

        request_data = u2f.start_register(APP_ID, [])
        response = token.register(request_data.registerRequests[0].json, FACET)

        device, cert = u2f.complete_register(request_data, response)
        assert device

    def test_authenticate_soft_u2f(self):
        pass  # See corresponding method in test_u2f_v2.py

if __name__ == "__main__":
    unittest.main()