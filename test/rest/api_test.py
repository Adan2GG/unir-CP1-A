import http.client
import os
import unittest
from urllib.request import urlopen

import pytest

BASE_URL = "http://localhost:5000"
BASE_URL_MOCK = "http://localhost:9090"
DEFAULT_TIMEOUT = 2  # in secs

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/1/2"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(
                response.status, http.client.OK, f"Error en la petición API a {url}"
            )
            self.assertEqual(
            response.read().decode(), "3", "ERROR ADD"
            )
        except Exception as e:
            if isinstance(e.reason, socket.timeout):
                pass
                raise e 
            

    def test_api_sqrt(self):
        url = f"{BASE_URL_MOCK}/calc/sqrt/64"
        try:
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "8", "ERROR SQRT"
        )
        except Exception as e:
            if isinstance(e.reason, socket.timeout):
                pass
                raise e 
    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        try:
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "4", "ERROR MULTIPLY"
        )
        except Exception as e:
            if isinstance(e.reason, socket.timeout):
                pass
                raise e 
    def test_api_divide(self):
    url = f"{BASE_URL}/calc/divide/4/2"
    try:
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "2", "ERROR DIVIDE"
        )
        except Exception as e:
            if isinstance(e.reason, socket.timeout):
                pass
                raise e 

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
