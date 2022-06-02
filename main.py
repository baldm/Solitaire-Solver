import base64

from os.path import join
from os import getcwd, remove

from fastapi import FastAPI
from pydantic import BaseModel

from solitaire_solver import process_and_analyze_image


# Temp import for testing:
import time


app = FastAPI()



class Image(BaseModel):
    image_string: str


@app.post("/analyze_image/")
async def upload_board_image(item: Image):
  
    save_path = join(getcwd(), 'images', 'filename.png')

    decoded_image = base64.b64decode(item.image_string)

    with open(save_path, 'wb') as file:
        file.write(decoded_image)

    # PROCESS IMAGE HERE:
    # sleep here to demonstrate processing image
    endpoint_output = process_and_analyze_image('temp')
    time.sleep(2)

    # Removing temp file
    #  TODO: Remove this comment when it works
    # remove(save_path)

    return {'next_move': endpoint_output}
