def ttt_winner(board):
    if board[0][0] == board[0][1] == board[0][2]:
        print("Player {} WIN".format(board[0][0]))
    elif board[1][0] == board[1][1] == board[1][2]:
        print("Player {} WIN".format(board[1][0]))
    elif board[2][0] == board[2][1] == board[2][2]:
        print("Player {} WIN".format(board[2][0]))
    elif board[0][0] == board[1][0] == board[2][0]:
        print("Player {} WIN".format(board[0][0]))
    elif board[0][1] == board[1][1] == board[2][1]:
        print("Player {} WIN".format(board[0][1]))
    elif board[0][2] == board[1][2] == board[2][2]:
        print("Player {} WIN".format(board[0][2]))
    elif board[0][0] == board[1][1] == board[2][2]:
        print("Player {} WIN".format(board[0][0]))
    elif board[0][2] == board[1][1] == board[2][0]:
        print("Player {} WIN".format(board[0][2]))
    else:
        print("DRAW")