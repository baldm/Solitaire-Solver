from unittest import TestCase


from solitaire_solver.card_analyzer.card_analyzer import CardAnalyzer
from solitaire_solver.card_analyzer.model.state_model import State_model
from solitaire_solver.card_analyzer.controller.solitaire_controller import Solitaire_controller
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
        analyzer.update_card(['QD'])
        analyzer.get_next_moves()
        analyzer.update_card(['3C'])
        analyzer.get_next_moves()
        analyzer.update_card(['QH'])
        analyzer.get_next_moves()
        analyzer.update_card(['JS'])
        analyzer.get_next_moves()
        analyzer.update_card(['4H'])
        analyzer.get_next_moves()
        analyzer.update_card(['2C'])
        analyzer.get_next_moves()
        analyzer.update_card(['5H'])
        analyzer.get_next_moves()
        analyzer.update_card(['AH'])
        analyzer.get_next_moves()
        a = 1


    def testEquals(self):
        game = Solitaire_controller()
        stock = ['[]'] * 24
        talon = []
        foundations = [[], [], [], []]
        board = [['2S'], ['[]', 'QC'], ['[]', '[]', '4S'], ['[]', '[]', '[]', 'QH'], ['[]', '[]', '[]', '[]', '2D'], ['[]', '[]', '[]', '[]', '[]', '4H'], ['[]', '[]', '[]', '[]', '[]', '[]', '4D']]
        state = State_model(board, foundations, stock, talon)
        state2 = State_model(board, foundations, stock, talon)

        self.assertTrue(state.equals(state2))
        state2 = game.Result(state2,game.Actions(state2)[0])
        self.assertFalse(state.equals(state2))
