# Write a code for tic tac toe game
import random 
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for cond in win_conditions:
        if all(board[i] == player for i in cond):
            return True
    return False

def check_draw(board):
    return all(cell != ' ' for cell in board)

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move. Try again.")
            else:
                board[move] = 'X'
                break
        except ValueError:
            print("Please enter a number between 1 and 9.")

def computer_move(board):
    available = [i for i, cell in enumerate(board) if cell == ' ']
    move = random.choice(available)
    board[move] = 'O'
    print(f"Computer chose position {move + 1}")

def main():
    board = [' '] * 9
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        player_move(board)
        print_board(board)
        if check_win(board, 'X'):
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        computer_move(board)
        print_board(board)
        if check_win(board, 'O'):
            print("Computer wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    while(True):
        main()