# Function reverse takes input from user then splits the word and turns it into a
# list which is saved in a variable. After that the Function returns the
# word(the list) in reverse order


def reverse():
    word = input("Enter a two words or a setntence: ")
    result = word.split()
    return result[::-1]


print(reverse())
