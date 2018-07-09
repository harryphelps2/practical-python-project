import unittest
import run
from flask import Flask, redirect, render_template, request
import os
import tempfile

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
    
    def test_order_leaderboard(self):
        """Test to order users dictionary by score value to 
        display on leaderboard"""
        users = {'a' : '1', 'b' : '4', 'c' : '7'}
        ordered_leaderboard = run.order_leaderboard(users)
        leaderboard = { 'c' : '7', 'b' : '4', 'a' : '1'}
        self.assertEqual(ordered_leaderboard, leaderboard)

if __name__ == '__main__':
    unittest.main()