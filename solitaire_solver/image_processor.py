from .card_recognizer import CardRecognizer


def process_and_analyze_image(image):

    # Image processing
    card_recognizer = CardRecognizer()
    results = card_recognizer.recognize_cards(image)

    # analyzing board
    # main analyzing things go here

    # Change to analyzers output, e.i the next move
    return {'move_from': 2, 'move_card': 'temp card', 'move_to': 3}
