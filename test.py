from tests.test_solitaire_controller import TestSolitaire_controller
from tests.test_card_analyzer import TestCard_analyzer

from tests.test_picture import Testcard_recognizer

test = TestSolitaire_controller()
test.test_BFS()
test3 = Testcard_recognizer()
test3.test()
test3.test_full_picture()
test2 = TestCard_analyzer()
test2.testEquals()
test2.bugfix()