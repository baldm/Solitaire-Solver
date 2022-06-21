
from unittest import TestCase

from solitaire_solver.card_recognizer import card_recognizer


card_recognize = card_recognizer()
class Testcard_recognizer(TestCase):
    def test(self):
        self.assertEqual( card_recognize.recognize_cards("images/test_images/hjerte2.jpg")[0][0],"2H")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/hjerte3.jpg")[0],"3H")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/hjerte4.jpeg")[0],"4H")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/hjerte5.jpg")[0],"5H")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/hjerte6.jpg")[0],"6H")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/hjerte7.jpeg")[0],"7H")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/hjerte8.jpg")[0],"8H")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/hjerte9.jpeg")[0],"9H")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/hjertebonde.jpeg")[0],"JH")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/hjertedronning.jpg")[0],"QH")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/hjertekonge.jpeg")[0],"KH")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/hjertees.jpeg")[0],"AH")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/spar2.jpeg")[0],"2S")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/spar3.jpg")[0],"3S")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/spar4.jpeg")[0],"4S")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/spar5.jpeg")[0],"5S")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/spar6.jpg")[0],"6S")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/spar7.jpeg")[0],"7S")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/spar8.jpeg")[0],"8S")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/spar9.jpeg")[0],"9S")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/sparbonde.jpeg")[0],"JS")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/spardronning.jpg")[0],"QS")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/sparkonge.jpeg")[0],"KS")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/spares.jpeg")[0],"AS")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/klor2.jpeg")[0],"2C")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/klor3.jpeg")[0],"3C")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/klor4.jpg")[0],"4C")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/klor5.jpeg")[0],"5C")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/klor6.jpeg")[0],"6C")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/klor7.jpeg")[0],"7C")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/klor8.jpeg")[0],"8C")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/klor9.jpg")[0],"9C")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/klorbonde.jpeg")[0],"JC")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/klorkonge.jpeg")[0],"KC")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/klores.jpeg")[0],"AC")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/rude2.jpeg")[0],"2D")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/rude3.jpg")[0],"3D")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/rude4.jpg")[0],"4D")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/rude5.jpeg")[0],"5D")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/rude6.jpg")[0],"6D")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/rude7.jpeg")[0],"7D")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/rude8.jpg")[0],"8D")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/rude9.jpg")[0],"9D")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/rudebonde.jpeg")[0],"JD")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/rudedronning.jpg")[0],"QD")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/rudekonge.jpg")[0],"KD")
        self.assertEqual( card_recognize.recognize_cards("images/test_images/rudees.jpeg")[0],"AD")
        
        
        
        