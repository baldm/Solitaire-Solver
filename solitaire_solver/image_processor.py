from .card_recognizer import CardRecognizer
from .card_analyzer import CardAnalyzer

import random


def process_and_analyze_image(image):

    # Image processing
    card_recognizer = CardRecognizer()
    card_analyzer = CardAnalyzer()

    # Get Analyze the incoming image and get
    # info from all cards and their placement
    card_info = card_recognizer.recognize_cards(image)

    # analyzing board
    # main analyzing things go here
    next_move = card_analyzer.get_next_move(card_info)

    return next_move
