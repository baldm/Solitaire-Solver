

class CardRecognizer:

    def __init__(self):
        self.temp_output = {
            'foundation': [
                [1, 2, 3],
                [1],
                [3],
                [4]
            ],
            'board': [
                [5],
                [6, 3, 4],
                [3],
                [2],
                [4],
                [4],
                [5]
            ]
        }

    def recognize_cards(self, image):
        return self.temp_output
