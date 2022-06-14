import os
import base64
import requests

paths = os.listdir("cardDetector/billeder")

url = 'http://localhost:8000'
timeout = 5
# Send simple request to check if there is a connection to the backend
response = requests.get(url, timeout=timeout)

url = 'http://localhost:8000/analyze_image'

while True:
    user_input = input("input kort, feks. klør4.jpg: ")

    with open('cardDetector/billeder/'+user_input, 'rb') as file:
        # Read image and encode
        encoded_string = base64.b64encode(file.read())

        # Encode image to string
        body = {'image_string': encoded_string.decode()}

        # Send request and parse response
        response = requests.post(url, json=body)
        print(response.status_code)
        if response.status_code == 200:
            print(response.json())
