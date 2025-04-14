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

    def test_set_difficulty(self):
        # Easy
        with patch('builtins.input', side_effect=['eAsY']) as mock_input:
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                result = set_difficulty()

                expected_output = "\nPlease select the difficulty level:\n" \
                "1. Easy (10 guesses)\n" \
                "2. Medium (5 guesses)\n" \
                "3. Hard (3 guesses)\n" \
                "\nGreat! You have selected the Easy difficulty level.\nLet's start the game!\n"

                self.assertEqual(mock_stdout.getvalue(), expected_output)
                self.assertEqual(result, 10)

        # Medium
        with patch('builtins.input', side_effect=['MeDiUM']) as mock_input:
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                result = set_difficulty()

                expected_output = "\nPlease select the difficulty level:\n" \
                "1. Easy (10 guesses)\n" \
                "2. Medium (5 guesses)\n" \
                "3. Hard (3 guesses)\n" \
                "\nGreat! You have selected the Medium difficulty level.\nLet's start the game!\n"

                self.assertEqual(mock_stdout.getvalue(), expected_output)
                self.assertEqual(result, 5)

        # Hard
        with patch('builtins.input', side_effect=['hARd']) as mock_input:
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                result = set_difficulty()

                expected_output = "\nPlease select the difficulty level:\n" \
                "1. Easy (10 guesses)\n" \
                "2. Medium (5 guesses)\n" \
                "3. Hard (3 guesses)\n" \
                "\nGreat! You have selected the Hard difficulty level.\nLet's start the game!\n"

                self.assertEqual(mock_stdout.getvalue(), expected_output)
                self.assertEqual(result, 3)

        # Bad input
        with patch('builtins.input', side_effect=['hardmode', 'hard']) as mock_input:
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                result = set_difficulty()

                expected_output = "\nPlease select the difficulty level:\n" \
                "1. Easy (10 guesses)\n" \
                "2. Medium (5 guesses)\n" \
                "3. Hard (3 guesses)\n" \
                "\nThat is not a valid difficulty. Please try again.\n" \
                "\nGreat! You have selected the Hard difficulty level.\nLet's start the game!\n"

                self.assertEqual(mock_stdout.getvalue(), expected_output)
                self.assertEqual(result, 3)

    def test_take_guess(self):
        # Invalid guess
        with patch('builtins.input', side_effect=['dog', '50']) as mock_input:
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                guess = take_guess()
                expected_output = "Your guess must be a number between 1 and 100 (inclusive). Please try again.\n"
                self.assertEqual(mock_stdout.getvalue(), expected_output)
                self.assertEqual(guess, 50)

        # Out of range
        with patch('builtins.input', side_effect=['0', '999', '50']) as mock_input:
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                guess = take_guess()
                expected_output = "Your guess must be between 1 and 100 (inclusive). Please try again.\n" \
                    "Your guess must be between 1 and 100 (inclusive). Please try again.\n"
                self.assertEqual(mock_stdout.getvalue(), expected_output)
                self.assertEqual(guess, 50)