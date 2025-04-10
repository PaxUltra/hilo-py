import unittest
from io import StringIO
from unittest.mock import patch, Mock
from hilo import start_game, set_difficulty, take_guess, play_game, game_loop

class TestHiloFunctions(unittest.TestCase):
    def test_start_game(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            number = start_game()
            expected_output = "\nWelcome to HiLo!\n" \
            "I'm thinking of a number between 1 and 100 (inclusive).\n" \
            "It is your job to guess what it is.\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)
            self.assertGreaterEqual(number, 1)
            self.assertLessEqual(number, 100)

    def test_set_difficulty(self, mock_input):
        # Test the three difficulties
        return