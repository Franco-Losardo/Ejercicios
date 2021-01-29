birthdays = {
    "Albert Einstein" : "14/03/1879",
    "Nikola Tesla" : "10/07/1856",
    "Ada Lovelace" : "10/12/1815",
    "Charles Darwin" : "12/02/1809"
    }
print("Welcome to the birthday dictionary. We know the birthdays of:")

for name in birthdays:
    print(name)
# print("Albert Einstein , Nikola Tesla, Ada Lovelace, Charles Darwin")
answer = str.casefold(input("Who's birthday do you want to look up?"))

def show_birthdays():
    if answer == "albert einstein":
        print("Albert Einstein's birthday is",birthdays["Albert Einstein"])
    elif answer == "nikola tesla":
        print("Nikola Tesla's birthday is", birthdays["Nikola Tesla"])
    elif answer == "ada lovelace":
        print("Ada Lovelace's birthday is", birthdays["Ada Lovelace"])
    elif answer == "charles darwin":
        print("Charles Darwin's birthday is", birthdays["Charles Darwin"])
    else:
        print("Do not have", answer,"'s birthdays, try another one")


show_birthdays()
