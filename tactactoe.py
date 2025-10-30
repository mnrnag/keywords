def print_board(board):
    for row in board:
        print("|".join (row))
        print("-" * 5)

def check_winner(board,player):
    for i in range(3):
        if all(cell == player for cell in board[i]) or\
        all(board[j][i] == player for j in range(3) ):
            return True
        return(
            all(board[i][i] == player for i in range(3))or
            all(board[i][2-i] == player for i in range(3))  
        )
    
def is_full(board):
    return all(cell in ['x','o'] for row in board for cell in row)

def tic_tac_toe():
    board=[[" " for _ in range(3)] for _ in range(3)]
    current_player="x"

    print("Welcome to tic tac toe")
    print_board(board)

    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
            if board[row][col] != " ":
                print("That spot is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as numbers between 0 and 2.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()

   