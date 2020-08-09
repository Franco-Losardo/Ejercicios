board = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def tic(r, c):
    board[row_input-1][col_input-1] = 1
    print(board)


def tac(r, c):
    board[row_input-1][col_input-1] = 2
    print(board)


print('Lets play tic tac toe')
print("This is the game board ⬇️ ")
print(board)
print("The winner will be displayed once the game is finished")
winners = {0: "Nobody", 1: "Player 1", 2: "Player 2"}

def who_wins():
    for i in range(1, 3):
        # Row check
        if board[0] == [i, i, i] or board[1] == [i, i, i] or board[2] == [i, i, i]:
            return winners[i]
        # Left column
        elif board[0][0] == i and board[1][0] == i and board[2][0] == i:
            return winners[i]
        # Centre column
        elif board[0][1] == i and board[1][1] == i and board[2][1] == i:
            return winners[i]
        # Right column
        elif board[0][2] == i and board[1][2] == i and board[2][2] == i:
            return winners[i]
        # Top-left diagonal
        elif board[0][0] == i and board[1][1] == i and board[2][2] == i:
            return winners[i]
        # Top-right diagonal
        elif board[0][2] == i and board[1][1] == i and board[2][0] == i:
            return winners[i]
    else:
        return winners[0]

for i in range(0, 9):
    if i % 2 == 0:
        row_input = int(
            input('Enter the row where you want to place your answer player 1:'))
        col_input = int(
            input('Enter the column where you want to place your answer player 1:'))
        if board[row_input-1][col_input-1] == 0:
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
        if board[row_input-1][col_input-1] == 0:
            tac(row_input, col_input)
        else:
            print('The column is already occupied. Please enter another value:')
            col_input = int(
                input('Enter the column where you want to place your answer player 2:'))
            tac(row_input, col_input)
            continue
winner = who_wins()
print("The winner is", winner)




