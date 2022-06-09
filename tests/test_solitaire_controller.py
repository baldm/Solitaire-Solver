
from unittest import TestCase

from solitaire_solver.card_analyzer.controller import solitaire_controller
from solitaire_solver.card_analyzer.ai import Agent,BFS
from solitaire_solver.card_analyzer.model import action_model,state_model



class TestSolitaire_controller(TestCase):
    ## Tests all combinations of colors being moved
    def test_alternating_color(self):
        card_diamond = "3D"
        card_heart = "4H"
        card_clubs = "5C"
        card_spade = "6S"
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(self, card_heart, card_clubs))
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(self, card_heart, card_spade))
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(self, card_diamond, card_clubs))
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(self, card_diamond, card_spade))
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(self, card_clubs, card_heart))
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(self, card_clubs, card_diamond))
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(self, card_spade, card_heart))
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(self, card_spade, card_diamond))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(self, card_clubs, card_clubs))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(self, card_clubs, card_spade))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(self, card_spade, card_spade))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(self, card_spade, card_clubs))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(self, card_heart, card_heart))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(self, card_heart, card_diamond))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(self, card_diamond, card_diamond))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(self, card_diamond, card_heart))

    ## Test if king moves to an empty column and populated column
    def test_king_to_empty(self):
        card_king = "KH"
        empty_list = []
        list = ["2H, 3C"]
        self.assertTrue(solitaire_controller.Solitaire_controller.king_to_empty(self, card_king, empty_list))
        self.assertFalse(solitaire_controller.Solitaire_controller.king_to_empty(self, card_king, list))

    def test_descending_order(self):
        values = list(range(1, 14))
        keys = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        self.order = dict(zip(keys, values))
        

        ace = "AC"
        two = "2H"
        three = "3C"
        four = "4H"
        five = "5C"
        six = "6H"
        seven = "7C"
        eight = "8H"
        nine = "9C"
        ten = "TH"
        jack = "JC"
        queen = "QH"
        king = "KC"
        ## Test correct descending order
        self.assertTrue(solitaire_controller.Solitaire_controller.descending_order(self, ace, two))
        self.assertTrue(solitaire_controller.Solitaire_controller.descending_order(self, two, three))
        self.assertTrue(solitaire_controller.Solitaire_controller.descending_order(self, three, four))
        self.assertTrue(solitaire_controller.Solitaire_controller.descending_order(self, four, five))
        self.assertTrue(solitaire_controller.Solitaire_controller.descending_order(self, five, six))
        self.assertTrue(solitaire_controller.Solitaire_controller.descending_order(self, six, seven))
        self.assertTrue(solitaire_controller.Solitaire_controller.descending_order(self, seven, eight))
        self.assertTrue(solitaire_controller.Solitaire_controller.descending_order(self, eight, nine))
        self.assertTrue(solitaire_controller.Solitaire_controller.descending_order(self, nine, ten))
        self.assertTrue(solitaire_controller.Solitaire_controller.descending_order(self, ten, jack))
        self.assertTrue(solitaire_controller.Solitaire_controller.descending_order(self, jack, queen))
        self.assertTrue(solitaire_controller.Solitaire_controller.descending_order(self, queen, king))
        ## Test edge cases
        self.assertFalse(solitaire_controller.Solitaire_controller.descending_order(self, king, ace))
        self.assertFalse(solitaire_controller.Solitaire_controller.descending_order(self, ace, king))

    def test_actions(self):
        

        game = solitaire_controller.Solitaire_controller()
        board = [[],['2H', '3C'],['KH'],[],[],[],[]]
        stock = ['[]','[]','[]']
        foundations = [[],[],[],[]]
        talon = []
        state = state_model.State_model(board,foundations,stock,talon)

        self.assertTrue(len(game.Actions(state)) == 6)
        stock = ['[]','[]']
        state.stock = stock

        self.assertTrue(len(game.Actions(state)) == 5)
        
        talon = ['KS']
        state.talon = talon
        self.assertTrue(len(game.Actions(state)) == 11)

