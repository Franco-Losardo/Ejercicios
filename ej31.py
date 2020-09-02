if __name__ == '__main__':
    print("Welcome to the Hangman!")
    print("----------")
    word = "EVAPORATE"
    word = list(word)
    lines = "_" * len(word)
    lines = list(lines)
    lstguesses = []
    guess = input("Guess your letter: ")

    while True:
        if guess.upper() in lstguesses:
            guess = ""
            print("Already guessed")
        elif guess.upper() in word:
            index = word.index(guess.upper())
            lines[index] = guess.upper()
            word[index] = '_'
        else:
            print(''.join(lines))
            if guess is not '':
                lstguesses.append(guess.upper())
            guess = input("Guess your letter: ")
        if '_' not in lines:
            print("You won!!")
            break
