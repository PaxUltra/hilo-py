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

    print(f"\nGreat! You have selected the {user_diff.capitalize()} difficulty level.\nLet's start the game!")

    return diffs.get(user_diff)

def take_guess():
    while True:
        user_guess_str = input("\nEnter your guess: ")

        if not user_guess_str.isdigit():
            print("Your guess must be a number between 1 and 100 (inclusive). Please try again.")
            continue
        
        guess = int(user_guess_str)
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100 (inclusive). Please try again.")
            continue

        return guess

def play_game(number, max_guesses):
    game_over = False
    remaining_guesses = max_guesses

    while not game_over:
        user_guess = take_guess()

        if user_guess > number:
            print(f"Incorrect! The number is less than {user_guess}.")
            remaining_guesses -= 1
        elif user_guess < number:
            print(f"Incorrect! The number is greater than {user_guess}.")
            remaining_guesses -= 1
        else:
            attempts = max_guesses - remaining_guesses
            print(f"\nCongratulations! You guessed the correct number in {attempts} attempts.\n")
            game_over = True

        if remaining_guesses < 1:
            print(f"\nYou ran out of attempts! The number was {number}.\n")
            game_over = True

if __name__ == "__main__":
    # Start game, and select number
    number = start_game()

    # Select difficulty
    max_guesses = set_difficulty()

    # Play the game
    play_game(number, max_guesses)