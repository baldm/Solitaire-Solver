from tests.test_solitaire_controller import TestSolitaire_controller
from tests.test_card_analyzer import TestCard_analyzer

test = TestSolitaire_controller()
test.test_BFS()

test2 = TestCard_analyzer()
test2.testEquals()
test2.bugfix()