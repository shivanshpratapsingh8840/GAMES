import numpy as np

# Initialize the board
board = np.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
p1s = 'X'
p2s = 'O'

# Function to check rows
def check_rows(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(symbol, 'won')
            return True
    return False

# Function to check columns
def check_cols(symbol):
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(symbol, 'won')
            return True
    return False

# Function to check diagonals
def check_diagonals(symbol):
    # Main diagonal
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        print(symbol, 'won')
        return True
    # Anti-diagonal
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        print(symbol, 'won')
        return True
    return False

# Function to check if someone won
def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

# Function to place symbol on board
def place(symbol):
    print(np.matrix(board))
    while True:
        row = int(input('Enter row (1, 2, or 3): '))
        col = int(input('Enter column (1, 2, or 3): '))
        if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == '-':
            board[row - 1][col - 1] = symbol
            break
        else:
            print('Invalid input. Please enter again.')

# Function to play the game
def play():
    for turn in range(9):
        if turn % 2 == 0:
            print('X turn')
            place(p1s)
            if won(p1s):
                break
        else:
            print('O turn')
            place(p2s)
            if won(p2s):
                break
    else:
        print('Draw')

play()
