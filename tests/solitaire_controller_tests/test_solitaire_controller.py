from unittest import TestCase
from solitaire_solver.card_analyzer.controller import solitaire_controller


class TestSolitaire_controller(TestCase):
    def test_alternating_color(self):
        card_diamond = "3D"
        card_heart = "4H"
        card_clubs = "5C"
        card_spade = "6S"
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(card_heart, card_clubs))
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(card_heart, card_spade))
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(card_diamond, card_clubs))
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(card_diamond, card_spade))
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(card_clubs, card_heart))
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(card_clubs, card_diamond))
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(card_spade, card_heart))
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(card_spade, card_diamond))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(card_clubs, card_clubs))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(card_clubs, card_spade))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(card_spade, card_spade))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(card_spade, card_clubs))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(card_heart, card_heart))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(card_heart, card_diamond))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(card_diamond, card_diamond))
        self.assertFalse(solitaire_controller.Solitaire_controller.alternating_color(card_diamond, card_heart))