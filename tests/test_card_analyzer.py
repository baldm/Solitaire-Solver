import unittest

from solitaire_solver.card_analyzer.card_analyzer import CardAnalyzer
from solitaire_solver.card_analyzer.model.action_model import Action_model
from solitaire_solver.card_analyzer.model.state_model import State_model
from solitaire_solver.card_analyzer.controller.solitaire_controller import Solitaire_controller

import random
class TestCard_analyzer(unittest.TestCase):

    def setUp(self):
        
        self.analyzer = CardAnalyzer()

    def set_seed(self, seed):
        random.seed(seed)

    def test(self):
        
        board = [['2S'], ['[]', 'QC'], ['[]', '[]', '4S'], ['[]', '[]', '[]', 'QH'], ['[]', '[]', '[]', '[]', '2S'], ['[]', '[]', '[]', '[]', '[]', '4H'], ['[]', '[]', '[]', '[]', '[]', '[]', '4S']]
        self.analyzer.update_card(board)
        self.analyzer.get_next_moves()
        self.analyzer.update_card(['9S'])


        board = [['2S'], ['[]', 'QC'], ['[]', '[]', '4S'], ['[]', '[]', '[]', 'QH'], ['[]', '[]', '[]', '[]', '2D'], ['[]', '[]', '[]', '[]', '[]', '4H'], ['[]', '[]', '[]', '[]', '[]', '[]', '4D']]
        self.analyzer.update_card(board)
        self.analyzer.get_next_moves()
        self.analyzer.update_card(['TC'])
        self.analyzer.get_next_moves()
        self.analyzer.update_card(['9C'])

    def bugfix(self):
        analyzer = CardAnalyzer()
        board = [['6D','5S'], ['[]', '2S'], ['[]', '[]', 'AS'], ['[]', '[]', '[]', '2H'], ['[]', '[]', '[]', '[]', 'TD'], ['[]', '[]', '[]', '[]', '[]', '7C'], ['[]', '[]', '[]', '[]', '[]', '[]', 'TH']]
        analyzer.update_card(board)
        analyzer.state.talon = []
        analyzer.state.stock = ['[]']*23
        analyzer.get_next_moves()
        board = [['5H','4S','3H'],['[]','QH','JS'],['[]','[]','2H'],['[]','[]','AS'],['[]','[]','[]','6D'],['[]','[]','[]','[]','[]','KH'],['[]','[]','[]','[]','TS','9D']]
        analyzer.update_card(board)
        analyzer.get_next_moves()

        board = [['KH'],['[]','TH','9C','8D'],['[]','[]','TD'],['[]', '[]','4C','3H'],['[]','[]','[]','2H'],['[]','[]','[]','[]','5H'],['[]','[]','[]','[]','[]','[]','JS']]
        analyzer.update_card(board)
        analyzer.get_next_moves()
 
    def testOneGame(self):
        
        values = ['A', '2', '3', '4', '5', '6',
                '7', '8', '9', 'T', 'J', 'Q', 'K']
        types = ['H','C','S','D']
        cards = []
        for value in values:
                for type in types:
                    cards.append(value+type)

        board = [[], ['[]'], ['[]', '[]'], ['[]', '[]', '[]'], ['[]', '[]', '[]', '[]'], ['[]', '[]', '[]', '[]', '[]'], ['[]', '[]', '[]', '[]', '[]', '[]']]
        for row in board:
            index = random.randint(0, len(cards)-1)
            row.append(cards[index])
            cards.pop(index)
       
        self.analyzer.update_card(board)
        output = self.analyzer.get_next_moves()
        while output != False:
            if self.analyzer.game.is_goal(self.analyzer.state):
                break

            index = random.randint(0, len(cards)-1)
            self.analyzer.update_card([cards[index]])
            cards.pop(index)
            output = self.analyzer.get_next_moves()
        iswon = output
        if iswon == False:
            return False
        return True

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




            





if __name__ == '__main__':
    unittest.main()