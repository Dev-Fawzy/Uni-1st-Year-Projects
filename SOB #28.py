#import used to gain access to code in another module

import random


def guess_number():
    play_again = True

    while play_again:
        # Generate a random number between 1 and 100
        secret_number = random.randint(1, 100)
        
        print("Welcome to the Number Guessing Game!")
        print("I have selected a number between 1 and 100. Try to guess it.")

        attempts = 0
        while True:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            
            # Increment the attempts counter
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in, {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")

        # Ask the player if they want to play again
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'

if __name__ == "__main__":
    guess_number()
