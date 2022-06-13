from unittest import TestCase


from solitaire_solver.card_analyzer.card_analyzer import CardAnalyzer
class TestCard_analyzer(TestCase):
    def test(self):
        analyzer = CardAnalyzer()
        board = [['2S'], ['[]', 'QC'], ['[]', '[]', '4S'], ['[]', '[]', '[]', 'QH'], ['[]', '[]', '[]', '[]', '2S'], ['[]', '[]', '[]', '[]', '[]', '4H'], ['[]', '[]', '[]', '[]', '[]', '[]', '4S']]
        analyzer.update_card(board)
        analyzer.get_next_moves()
        analyzer.update_card(['9S'])
    