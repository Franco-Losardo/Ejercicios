board = [[0, 1, 2],
        [2, 2, 0],
        [2, 1, 1]]

winners = {0: "Nobody", 1: "Player 1", 2:"Player 2"}


def who_wins():
    for i in range(1,3):
        # Row check
        if board[0] == [i,i,i] or board[1] == [i,i,i] or board[2] == [i,i,i]:
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

winner = who_wins()
print("The winner is ", winner)