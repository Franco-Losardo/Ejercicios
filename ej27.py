game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]



def tic(r, c):
    game[row_input-1][col_input-1] = 'X'
    print(game)


def tac(r, c):
    game[row_input-1][col_input-1] = 'O'
    print(game)


print('Lets play tic tac toe')
print("This is the game board ⬇️ ")
print(game)
for i in range(0, 9):
    if i % 2 == 0:
        row_input = int(input('Enter the row where you want to place your answer player 1:'))
        col_input = int(
            input('Enter the column where you want to place your answer player 1:'))
        if game[row_input-1][col_input-1] == 0:
            tic(row_input, col_input)
        else:
            print('The column is already occupied. Please enter another value:')
            col_input = int(
                input('Enter the column where you want to place your answer player 1:'))
            tic(row_input, col_input)
            continue
    else:
        row_input = int(
            input('Enter the row where you want to place your answer player 2:'))
        col_input = int(
            input('Enter the column where you want to place your answer player 2:'))
        if game[row_input-1][col_input-1] == 0:
            tac(row_input, col_input)
        else:
            print('The column is already occupied. Please enter another value:')
            col_input = int(
                input('Enter the column where you want to place your answer player 2:'))
            tac(row_input, col_input)
            continue
