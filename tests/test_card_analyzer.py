from unittest import TestCase


from solitaire_solver.card_analyzer.card_analyzer import CardAnalyzer
from solitaire_solver.card_analyzer.model.state_model import State_model
from solitaire_solver.card_analyzer.controller.solitaire_controller import Solitaire_controller
import random
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
        board = [['5H','4S','3H'],['[]','QH','JS'],['[]','[]','2H'],['[]','[]','AS'],['[]','[]','[]','6D'],['[]','[]','[]','[]','[]','KH'],['[]','[]','[]','[]','TS','9D']]
        analyzer.update_card(board)
        analyzer.get_next_moves()

        board = [['KH'],['[]','TH','9C','8D'],['[]','[]','TD'],['[]', '[]','4C','3H'],['[]','[]','[]','2H'],['[]','[]','[]','[]','5H'],['[]','[]','[]','[]','[]','[]','JS']]
        analyzer.update_card(board)
        analyzer.get_next_moves()

    def testGame(self):
        values = ['A', '2', '3', '4', '5', '6',
                '7', '8', '9', 'T', 'J', 'Q', 'K']
        types = ['H','C','S','D']
        cards = []

        
        
        victories = 0
        number = 0

        while victories != 10:
            iswon = False
            while iswon == False:
                number +=1

                print(number)
                cards = []
                for value in values:
                    for type in types:
                        cards.append(value+type)

                board = [[], ['[]'], ['[]', '[]'], ['[]', '[]', '[]'], ['[]', '[]', '[]', '[]'], ['[]', '[]', '[]', '[]', '[]'], ['[]', '[]', '[]', '[]', '[]', '[]']]
                for row in board:
                    index = random.randint(0, len(cards)-1)
                    row.append(cards[index])
                    cards.pop(index)
                analyzer = CardAnalyzer()
                analyzer.update_card(board)

                output = analyzer.get_next_moves()

                while output != False and not analyzer.game.is_goal(analyzer.state):

                    index = random.randint(0, len(cards)-1)
                    analyzer.update_card([cards[index]])
                    cards.pop(index)
                    output = analyzer.get_next_moves()
                iswon = output
            victories +=1
            print('won ' + str(victories) + ' times')
            
        print('won ' + str(victories) + ' times out of ' + str(number) )
        
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
        analyzer = CardAnalyzer()
        analyzer.update_card(board)
        output = analyzer.get_next_moves()
        while output != False and not analyzer.game.is_goal(analyzer.state):
            index = random.randint(0, len(cards)-1)
            analyzer.update_card([cards[index]])
            cards.pop(index)
            output = analyzer.get_next_moves()
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
