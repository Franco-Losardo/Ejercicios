import random
# Opens word list
with open('sowpods.txt', 'r') as open_file:
    all_text = open_file.read()
    new_list = all_text.split()
    random_word = random.choice(new_list)

if __name__ == '__main__':
    print("Welcome to the Hangman!")
    print("----------")
    print(random_word)
    word = random_word
    word = list(word)
    lines = "_" * len(word)
    lines = list(lines)
    lstguesses = []
    mistakes = 0
    print("You have one extra life at the begginig of the game, afterwards you can make 6 mistakes, remeber letters you have already tried if you repeat it you will lose one mistake")
    guess = input("Guess your letter: ")
    

    while mistakes < 6:
        if guess.upper() in lstguesses:
            guess = ""
            print("Already guessed")
            mistakes += 1
            print("You have", 6 - mistakes, "lives left")
        elif guess.upper() in word: 
            index = word.index(guess.upper())
            lines[index] = guess.upper()
            word[index] = '_' 
        else:
            print(''.join(lines))
            if guess != '':
                lstguesses.append(guess.upper())
            guess = input("Guess your letter: ")                
            if guess.upper() not in word:
                if guess.upper() not in lstguesses:
                    mistakes += 1
                    print("You have", 6 - mistakes, "lives left")
        if '_' not in lines:
            print("You won and have", 6 - mistakes, "lives remaining!!")
            break

