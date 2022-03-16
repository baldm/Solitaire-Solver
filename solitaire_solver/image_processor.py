from .card_recognizer import CardRecognizer


def process_and_analyze_image(image):

    # Image processing
    card_recognizer = CardRecognizer()
    results = card_recognizer.recognize_cards(image)
    print(results)

    # analyzing board
    # main analyzing things go here

    # Change results to analyzers output
    return results
