import random

def start_game():
    print("\nWelcome to HiLo!\n"
    "I'm thinking of a number between 1 and 100 (inclusive).\n"
    "It is your job to guess what it is.")

    return random.randint(1, 100)

def set_difficulty():
    diffs = {
        "easy": 10,
        "medium": 5,
        "hard": 3
    }

    valid_diff = False

    print("\nPlease select the difficulty level:\n"
    "1. Easy (10 guesses)\n"
    "2. Medium (5 guesses)\n"
    "3. Hard (3 guesses)")
    
    while not valid_diff:
        user_diff = input("\nEnter your choice: ").lower()

        if user_diff not in diffs.keys():
            print("\nThat is not a valid difficulty. Please try again.")
        else:
            valid_diff = True

    return diffs.get(user_diff)



if __name__ == "__main__":
    # Start game, and select number
    number = start_game()

    # Select difficulty
    max_guesses = set_difficulty()
    print(f"\nGuesses: {max_guesses}")

    # Accept user input

    # Evaluate input

    # End game