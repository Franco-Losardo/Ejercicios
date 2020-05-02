import random

print("Welcome to the guess number GAME!!")
number = random.randint(1, 9)
numberOfGuesses = 0
while True:
    guess = int(input("Enter a number: "))

    if guess > number:
        numberOfGuesses += 1
        print("Too high")

    elif guess < number:
        numberOfGuesses += 1
        print("Too low")

    elif guess == number:
        numberOfGuesses += 1
        print("That is correct! You have hit the right number after", numberOfGuesses, "guess(es)")
        finish = input("Enter exit to quit: ")
        if finish == "exit":
            print("See you later👋")
            break
