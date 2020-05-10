import random

random_number = str(random.randint(1000, 9999))
print("Let's play a game of Cowbull!")
print("I will generate a random number, and you have to guess the numbers one digit at a time.")
print("For every number in the right place, you get a cow. For every one in the wrong place, you get a bull.")
print("The game ends when you get 4 cows!")
print("Type exit at any prompt to quit the game.")
print(random_number)
user = input("Enter your guess: ")
cows = 0
numberOfGuesses = 0
bulls = 0


def check():
    for i in range(len(random_number)):
        if random_number[i] == user[i]:
            global cows
            cows += 1
            global numberOfGuesses
            numberOfGuesses += 1
        elif user[i] in random_number:
            global bulls
            bulls += 1
            numberOfGuesses += 1
    print("{} cows".format(cows), "{} bulls. Keep trying".format(bulls))


while True:
    check()
    if random_number == user:
        print("{} cows".format(cows), "{} bulls. You have won after {} guesses".format(bulls, numberOfGuesses))
        break
    else:
        check()
