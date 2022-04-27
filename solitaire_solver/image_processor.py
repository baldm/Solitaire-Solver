from .card_recognizer import CardRecognizer

import random

def process_and_analyze_image(image):

    # Image processing
    card_recognizer = CardRecognizer()
    results = card_recognizer.recognize_cards(image)

    # analyzing board
    # main analyzing things go here

    # Change to analyzers output, e.i the next move
    move_from = random.randint(0, 7)
    move_to = random.randint(0, 7)
    move_card = random.choice(['1 Clubs','2 Spades','5 Clubs', '8 Hearts'])
    return {'move_from':move_from, 'move_card': move_card, 'move_to': move_to}
