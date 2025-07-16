def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for c in '123456789':
                    if valid(board, i, j, c):
                        board[i][j] = c
                        if solve(board):
                            return True
                        board[i][j] = '.'
                return False
    return True

def valid(board, r, c, ch):
    for i in range(9):
        if board[i][c] == ch or board[r][i] == ch or board[r//3*3 + i//3][c//3*3 + i%3] == ch:
            return False
    return True

# Test board: Điền '.' vào các ô trống và gọi solve(board)
