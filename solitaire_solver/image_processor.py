from .card_recognizer import card_recognizer
from .card_analyzer import CardAnalyzer

import random
card_analyzer = CardAnalyzer()
card_recognizer = card_recognizer()


def process_and_analyze_image(image):

    # Image processing

    # Get Analyze the incoming image and get
    # info from all cards and their placement
    card_info = card_recognizer.recognize_cards(image)

    print("Card info:")
    print(card_info)

    if len(card_info) != 0:
        # Updating board state
        card_analyzer.update_card(card_info)
        # main analyzing things go here
        next_move = card_analyzer.get_next_moves()

        print("Next move:")
        print(next_move)
    else:
        raise Exception("No cards found")
    
    return next_move
    
