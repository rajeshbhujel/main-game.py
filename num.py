import random

def guess_the_number():
    # Generate a random number between 1 and 10
    number_to_guess = random.randint(1, 10)
    
    # Give the user a chance to guess
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 10.")
    
    attempts = 0
    while True:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is correct
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()
