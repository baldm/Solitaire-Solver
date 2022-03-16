import uuid
from os.path import join
from os import getcwd, remove

from fastapi import FastAPI, File, UploadFile

from solitaire_solver import process_and_analyze_image


# Temp import for testing:
import time


app = FastAPI()


@app.post("/analyze_image/")
async def upload_board_image(file: UploadFile = File(...)):
    # User @im_baby
    # https://stackoverflow.com/questions/66162654/fastapi-image-post-and-resize

    # Getting filename and reading file into memory
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!

    # Saving the file to process
    # Not sure we have to save the file,
    # but we can always remove it later when it works.
    save_path = join(getcwd(), 'images', file.filename)
    with open(save_path, "wb+") as f:
        f.write(contents)

    # PROCESS IMAGE HERE:
    # sleep here to demonstrate processing image
    endpoint_output = process_and_analyze_image('temp')
    time.sleep(5)
    # END PROCESS IMAGE:

    # Removing temp file
    remove(save_path)

    return {'board_state': endpoint_output}
