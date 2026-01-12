#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(player):
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Row and column must be 0, 1, or 2.")
                continue
            return row, col
        except ValueError:
            print("Invalid input. Please enter numeric values only.")

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_valid_input(current_player)

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place the move
        board[row][col] = current_player

        # Check for win
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("The game is a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()