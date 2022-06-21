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

    if len(card_info) == 0:
        # Return empty list if no cards are found
        return []

    # Updating board state
    card_analyzer.update_card(card_info)
    # main analyzing things go here
    next_move = card_analyzer.get_next_moves()

    # If the game cannot be won. Return empty states with game over
    if not next_move:
        next_move = {'move_from': '', 'move_card': '', 'move_to': '', 'get_talon': False, 'game_over': True}

    # Add regconized card to the output
    # Used to display card in frontend
    if len(card_info) == 1:
        next_move[0]['reg_card'] = card_info[0]
    else:
        # Return the amount of columns found in the first picture
        next_move[0]['reg_card'] = str(len(card_info))

    return next_move

#
