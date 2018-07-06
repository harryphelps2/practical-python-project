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
        username = "Harry"
        new_score = run.increment_score(username, 2)
        self.assertEqual(new_score, 3)

if __name__ == '__main__':
    unittest.main()