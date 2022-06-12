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
    #(image,card_analyzer.board)

    # analyzing board
    # main analyzing things go here
    next_move = card_analyzer.get_next_move(card_info)

    return next_move
