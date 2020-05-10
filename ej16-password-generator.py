import string
import random
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
print("It is highly recommended passwords have at least 8 characters")


def creates_random_password():
    number_of_letters = int(input("How many letters do you want your password to have? "))
    quantity_of_numbers = int(input("How many numbers do you want your password to have? "))
    number_of_symbols = int(input("How many symbols do you want your password to have? "))
    random_letters = random.choices(letters, k=number_of_letters)
    random_numbers = random.choices(numbers, k=quantity_of_numbers)
    random_symbols = random.choices(symbols, k=number_of_symbols)
    # Converts the password from a list to a string
    password = "".join(random_letters + random_numbers + random_symbols)
    print("Your password is: {}".format(password))


creates_random_password()


def new_password():
    # str.casefold() makes the input not case_sensitive
    new = str.casefold(input("Do you want a new password? "))
    if new == "yes":
        creates_random_password()
    else:
        print("See you 👋")


new_password()
