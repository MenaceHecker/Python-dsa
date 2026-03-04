## Write a program that plays every possible tic-tac-toe game,
## and then prints the number of valid, completed games.

winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def winner(board):
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            return True
    return False


def play(board, player):
    # Terminal game: someone has won, or the board is full (draw).
    if winner(board) or "" not in board:
        return 1

    total = 0
    next_player = "O" if player == "X" else "X"

    for i in range(9):
        if board[i] == "":
            board[i] = player
            total += play(board, next_player)
            board[i] = ""

    return total


empty_board = [""] * 9
final_answer = play(empty_board, "X")
print(final_answer)







                                                                                                                                                                                                                                                                                                                                                    


