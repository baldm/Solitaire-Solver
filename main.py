import base64

from os.path import join
from os import getcwd, remove

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from solitaire_solver import process_and_analyze_image


# Temp import for testing:
import time


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Image(BaseModel):
    image_string: str


@app.post("/analyze_image")
async def upload_board_image(item: Image):

    # Get path where image will be saved
    save_path = join(getcwd(), 'images', 'temp_images', 'filename.png')

    # Decode image from base64
    decoded_image = base64.b64decode(item.image_string)

    # Save image to drive
    with open(save_path, 'wb') as file:
        file.write(decoded_image)

    endpoint_output = process_and_analyze_image(save_path)

    if not endpoint_output:
        endpoint_output = [
            {'move_from': '', 'move_card': "No cards found", 'move_to': '', 'reg_card': '', 'get_talon': False, 'game_over': False}
        ]

    # Removing temp file
    remove(save_path)

    return endpoint_output
