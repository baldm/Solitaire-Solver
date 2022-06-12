class CardAnalyzer:

    def __init__(self):
        self.card_info = ""
        self.board = []

        # TODO: Her kan i implementer de objecter i skal bruge til det

    def _goes_here(self):
        # TODO: her kan i implentere hjælpe funktioner til at finde næste move
        pass

    def get_next_move(self, card_info):

        return [
            {'move_from': 3, 'move_card': '4H', 'move_to': '5C'},
            {'move_from': 4, 'move_card': '3S', 'move_to': '4H'}
        ]
