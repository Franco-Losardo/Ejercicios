import random


def check(random_number, user):
    cow_bull = [0, 0]  # cows then bulls
    if user > random_number:
        print("Too high")

    elif user < random_number:
        print("Too low")
    for i in range(len(random_number)):
        if random_number[i] == user[i]:
            cow_bull[0] += 1
        elif user[i] in random_number:
            cow_bull[1] += 1
    return cow_bull


if __name__ == "__main__":
    playing = True  # plays the game until becomes False
    random_number = str(random.randint(1000, 9999)) # 4 digit random number
    numberOfGuesses = 0
print("Let's play a game of Cowbull!")
print("I will generate a random number of 4 digits, and you have to guess the number.")
print("For every number in the right place, you get a cow. For every one in the wrong place, you get a bull.")
print("The game ends when you get 4 cows!")
print("Type exit at any prompt to quit the game.")


while playing:
    user = input("Enter your guess: ")
    if user == "exit":
        break
    cow_bull_count = check(random_number, user)
    numberOfGuesses += 1
    print("You have "+ str(cow_bull_count[0]) + " cows, and " + str(cow_bull_count[1]) + " bulls.")

    if cow_bull_count[0] == 4:
        playing = False
        print("You won the game after" ,numberOfGuesses, "guess(es)!")
        break
    else:
        print("Your guess isn't quite right, try again.")
