import random 
number = 50
maximum = 100
minumim = 0
answer = None
numberOfGuesses = 1
running = True
print("Think of a number between 0 and 100, I will guess it!!")
print("Done? Good")
while running:
    print("Is the number", number,"?")
    answer = int(input("""1) Too low 
2) Too high 
3) Correct ==> """))
    if answer == 1:
        numberOfGuesses += 1
        # Add 1 to the minimum so that when the computer makes a guess does not repeat the same number over and over
        minumim = number + 1
        number = random.randint(minumim, maximum)
        # number = number + round(number / 2)


    elif answer == 2:
        numberOfGuesses += 1
        maximum = number + 1
        number = random.randint(minumim, maximum)
        # number = number - round(number / 2)
       
    else:
        print("I knew it!! I got it after ", numberOfGuesses, "tries")
        break

#     guess = int(input("Enter a number: "))

#     if guess > number:
#         numberOfGuesses += 1
#         print("Too high")

#     elif guess < number:
#         numberOfGuesses += 1
#         print("Too low")

#     elif guess == number:
#         numberOfGuesses += 1
#         print("That is correct! You have hit the right number after",
#               numberOfGuesses, "guess(es)")
#         finish = input("Enter exit to quit: ")
#         if finish == "exit":
#             print("See you later👋")
#             break
