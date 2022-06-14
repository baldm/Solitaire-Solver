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
        board = [['6D','5S'], ['[]', '2S'], ['[]', '[]', 'AS'], ['[]', '[]', '[]', '2H'], ['[]', '[]', '[]', '[]', 'TD'], ['[]', '[]', '[]', '[]', '[]', '7C'], ['[]', '[]', '[]', '[]', '[]', '[]', 'TH']]
        analyzer.update_card(board)
        analyzer.state.talon = []
        analyzer.state.stock = ['[]']*23
        analyzer.get_next_moves()



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
