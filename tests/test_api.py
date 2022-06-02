# TEST FILE FOR TESTING ENDPOINT
# Can also be used as reference for frontend
import unittest
import requests
import base64

class TestApi(unittest.TestCase):
    def test_connection(self):
        url = 'http://0.0.0.0:8000'
        timeout = 5
        response = requests.get(url, timeout=timeout)
        self.assertIsNotNone(response)

    def test_post_image(self):
        url = 'http://0.0.0.0:8000/analyze_image'

        with open('tests/cards.jpg', 'rb') as file:
            # Read image and encode
            encoded_string = base64.b64encode(file.read())

            body = {'image_string': encoded_string.decode()}
            response = requests.post(url, json=body)
            self.assertTrue(response.status_code == 200)


if __name__ == '__main__':
    unittest.main()