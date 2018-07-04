import unittest
import run

class TestRiddle(unittest.TestCase):
    """
    Test suite for riddle-me-this game
    """
    def test_is_correct(self):
        """Test to see if the guessed answer is correct or not"""
        correct = run.is_correct(3,3)
        self.assertTrue(correct)
    
    def test_increment_score(self):
        """Test to see if the score is incremented by 1
        if the answer is correct"""
        new_score = run.increment_score(0)
        self.assertEqual(new_score, 1)

    def test_determine_high_score(self):
        """Test to see if the new score is a high score"""
        high_score = 1
        new_score = 2
        high_score = run.determine_high_score(high_score, new_score)
        self.assertEqual(high_score, new_score)

if __name__ == '__main__':
    unittest.main()