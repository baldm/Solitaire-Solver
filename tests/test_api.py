# TEST FILE FOR TESTING ENDPOINT
# Can also be used as reference for frontend
import unittest
import requests


class TestApi(unittest.TestCase):
    def test_connection(self):
        url = 'http://127.0.0.1:8000'
        timeout = 5
        response = requests.get(url, timeout=timeout)
        self.assertIsNotNone(response)

    def test_post_image(self):
        url = 'http://127.0.0.1:8000/analyze_image'

        with open('tests/cards.jpg', 'rb') as file:
            response = requests.post(url, files={'file': file})
            self.assertTrue(response.status_code == 200)


if __name__ == '__main__':
    unittest.main()
