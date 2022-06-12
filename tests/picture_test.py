import os
import base64
import requests

paths = os.listdir("cardDetector/billeder")

url = 'http://0.0.0.0:8000'
timeout = 5
# Send simple request to check if there is a connection to the backend
response = requests.get(url, timeout=timeout)

while True:
    user_input = input("skriv et kort som foreksempel klør4.jpg")
    for path in paths:
        if user_input in path:
            url = 'http://0.0.0.0:8000/analyze_image'

            with open('cardDetector/billeder/'+path, 'rb') as file:
                # Read image and encode
                encoded_string = base64.b64encode(file.read())

                # Encode image to string
                body = {'image_string': encoded_string.decode()}

                # Send request and parse response
                response = requests.post(url, json=body)
                print(response.json())