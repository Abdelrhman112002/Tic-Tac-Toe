def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):

    for row in board:
        if all(square == player for square in row):
            return True


    for col in range(3):
        if all(row[col] == player for row in board):
            return True


    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_tie(board):
    return all(square != "" for row in board for square in row)


def main():
    board = [["" for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        current_player = players[turn]

        print_board(board)
        move_row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
        move_col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))

        if 0 <= move_row < 3 and 0 <= move_col < 3 and board[move_row][move_col] == "":
            board[move_row][move_col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_tie(board):
                print_board(board)
                print("It's a tie!")
                break

            turn = 1 - turn  # Switch player's turn

        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    main()