from unittest import TestCase
from solitaire_solver.card_analyzer.controller import solitaire_controller


class TestSolitaire_controller(TestCase):
    def test_alternating_color(self):
        card_heart = "4H"
        card_clubs = "5C"
        self.assertTrue(solitaire_controller.Solitaire_controller.alternating_color(card_heart, card_clubs))
