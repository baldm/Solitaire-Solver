from unittest import TestCase


from solitaire_solver.card_analyzer.card_analyzer import CardAnalyzer
class TestCard_analyzer(TestCase):
    def test(self):
        analyzer = CardAnalyzer()
        board = [['2S'], ['[]', 'QC'], ['[]', '[]', '4S'], ['[]', '[]', '[]', 'QH'], ['[]', '[]', '[]', '[]', '2S'], ['[]', '[]', '[]', '[]', '[]', '4H'], ['[]', '[]', '[]', '[]', '[]', '[]', '4S']]
        analyzer.update_card(board)
        analyzer.get_next_moves()
        analyzer.update_card(['9S'])


        board = [['2S'], ['[]', 'QC'], ['[]', '[]', '4S'], ['[]', '[]', '[]', 'QH'], ['[]', '[]', '[]', '[]', '2D'], ['[]', '[]', '[]', '[]', '[]', '4H'], ['[]', '[]', '[]', '[]', '[]', '[]', '4D']]
        analyzer.update_card(board)
        analyzer.get_next_moves()
        analyzer.update_card(['TC'])
        analyzer.get_next_moves()
        analyzer.update_card(['9C'])

    def bugfix(self):
        analyzer = CardAnalyzer()
        board = [['8D'], ['[]', '9D'], ['[]', '[]', 'JH'], ['[]', '[]', '[]', '6D'], ['[]', '[]', '[]', '[]', 'TH'], ['[]', '[]', '[]', '[]', '[]', '8C'], ['[]', '[]', '[]', '[]', '[]', '[]', '9S']]
        analyzer.update_card(board)
        analyzer.get_next_moves()
        analyzer.update_card(['TC'])
        analyzer.get_next_moves()
        analyzer.update_card(['AD'])
        analyzer.get_next_moves()
        analyzer.update_card(['9C'])
        analyzer.get_next_moves()
        a = 1
