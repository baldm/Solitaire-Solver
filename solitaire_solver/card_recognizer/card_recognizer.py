

class CardRecognizer:

    # Types of cards:
    # [D, H, C, S]
    ## D = Ruder, H = hjerter, C=Klør, S=Spar

    # Card values:
    # [A, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]

    # Cards facing down
    # '[]'



    def __init__(self):
        self.temp_output = {
            'foundation': [
                'AD',
                'AH',
                'AC',
                'AS'
            ],
            'board': [
                ['[]', '8D'],
                ['3C','2C','AC'],
                ['[]','5S'],
                ['3H'],
                ['AH'],
                ['2H'],
                ['9D']
            ],
            'talon': 
                '4C'
            

        }

    def recognize_cards(self, image):
        return self.temp_output
