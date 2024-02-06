import random


def get_integer(prompt):
    while True:
        number = input(prompt)
        if number.isnumeric():
            return int(number)


highest = 100
answer = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and {highest}.")

valid_levels = ['1', '2']
level = 0
print("1... Easy (10 guesses)")
print("2... Hard (5 guesses)")
while level not in valid_levels:
    level = input("Choose your level ")

lives = 10 if level == '1' else 5

while lives > 0:
    plural = 's' if lives != 1 else ''
    print(f"You have {lives} attempt{plural} remaining")
    guess = get_integer("Have a guess: ")
    if guess == answer:
        print("Well done. You guessed it.")
        break
    else:
        lives -= 1
        if guess > answer:
            print("Guess is too high")
        else:
            print("Guess is too low")
else:
    print(f"You ran out of lives. The number was {answer}")
