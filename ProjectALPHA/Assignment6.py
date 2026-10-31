
N = 8

board = [[0 for _ in range(N)] for _ in range(N)]

def is_safe(board, row, col):

    # Check the left side of the current row
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower-left diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col):

    # Base case: all columns are filled
    if col >= N:
        return True

    # Try every row in the current column
    for row in range(N):

        if is_safe(board, row, col):
            board[row][col] = 1

            # Place a queen in the next column
            if solve_n_queens(board, col + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


if solve_n_queens(board, 0):
    print("Solution to 8-Queens Problem:")
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
else:
    print("No solution exists")
