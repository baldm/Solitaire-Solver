from unittest import TestCase
from solitaire_solver.card_analyzer.controller import solitaire_controller


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
        values = range(1, 13)
        keys = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        self.order = dict(keys, values) ## TODO dict laver fejl: "TypeError: dict expected at most 1 argument, got 2"
        pass

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



