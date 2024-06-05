import random

difficulty = input("Choose difficulty level. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    number_to_guess = random.randint(1, 5)
else:
    number_to_guess = random.randint(1, 10)

attempts = 0
guess = None
print(f"I have chosen a number between 1 and {5 if difficulty == 'easy' else 10}. Try to guess it!")
while guess != number_to_guess:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
