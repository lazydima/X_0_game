# for creatinng bord
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 3))

def is_position_free(board, row, col):
    return board[row][col] == " "

def check_winner(board):
    row = 0
    while row < 3:
        if board[row][0] == board[row][1] == board[row][2] != " ": # for rows
            return board[row][0]
        row += 1

    col = 0
    while col < 3:
        if board[0][col] == board[1][col] == board[2][col] != " ": # for collums
            return board[0][col]
        col += 1

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    current_player = "X"
    winner = None
    while not winner:
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if is_position_free(board, row, col):
                    board[row][col] = current_player
                    print_board(board)
                    winner = check_winner(board)
                    if winner:
                        print(f"Player {winner} wins!")
                    elif all(cell != " " for row in board for cell in row):
                        print("It's a draw!")
                    current_player = "O" if current_player == "X" else "X"
                else:
                    print("Position isnt free. Try again.")
            else:
                print("Row and column values should be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()