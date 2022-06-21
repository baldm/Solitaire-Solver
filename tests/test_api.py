# TEST FILE FOR TESTING ENDPOINT
# Can also be used as reference for frontend
import unittest
import requests
import base64


class TestApi(unittest.TestCase):
    def test_connection(self):
        url = 'http://localhost:8000'
        timeout = 5

        # Send simple request to check if there is a connection to the backend
        try:
            response = requests.get(url, timeout=timeout)
        except requests.exceptions.ConnectionError as e:
            print("[WARN] Test cannot run. There is no connection to the backend.")

        self.assertIsNotNone(response)

    def test_post_image(self):
        url = 'http://localhost:8000/analyze_image'

        with open('images/test_images/cards.jpg', 'rb') as file:
            # Read image and encode
            encoded_string = base64.b64encode(file.read())

            # Encode image to string
            body = {'image_string': encoded_string.decode()}

            # Send request and parse response
            try:
                response = requests.post(url, json=body)
            except requests.exceptions.ConnectionError as e:
                print(
                    "[WARN] Test cannot run. There is no connection to the backend.")
            self.assertTrue(response.status_code == 200)


if __name__ == '__main__':
    unittest.main()
