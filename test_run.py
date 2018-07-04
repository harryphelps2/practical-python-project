import unittest
import run

class TestRiddle(unittest.TestCase):
    """
    Test suite for riddle-me-this game
    """
    def test_is_correct(self):
        """Test to see if the guessed answer is correct or not"""
        answer = run.is_correct()
        self.assertTrue(answer)

if __name__ == '__main__':
    unittest.main()