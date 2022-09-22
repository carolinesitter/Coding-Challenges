# CHALLENGE: VALID SUDOKU
# -----------------------
## Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
## validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# TEST CASE 1:
# ------------
## Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# TEST CASE 2:
# ------------
## Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false


# PSEUDOCODE:
# -----------
## write a class that takes in an object
## within this class, write a function that takes in 

# CODE:
class Sudoku(object):
    # "board: List[List[str]] -> bool" is 'type' information. The board
    # will be a list of list of strings and the '->' points to the return type
    # of the function; in this case a boolean (True or False.)
    def is_valid(self, board: List[List[str]]) -> bool:

        # hash maps for rows, cols, and 3x3 squares
        # key is going to be the column/row/square number
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key (r/3, c/3) since squares are 3x3

        # iterate over the entire grid (dimensions are 9x9)
        for r in range(9):
            for c in range(9):

                # if this is an empty space, skip and continue to the next iteration
                if board[r][c] == ".":
                    continue

                # if we already have seen this value in the current row/col/square
                ## we are in, return False
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3,c//3)]):

                    return False
                
                # if valid (i.e. not a repeat), update all 3 hashmaps accordingly
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True # if we never detected any duplicates


# RUNTIME COMPLEXITY:
# -------------------
## This solution has an O(N^2) or Quadratic runtime complexity as there are two for loops (one is nested).
## For this solution, we need to iterate over the entire board, including the rows, columns, and 3x3 squares. 

