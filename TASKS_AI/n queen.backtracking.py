global N 
N = 4
def printSolution(board):
    for row in board:
        print(row)  
def isSafe(board, row, col):
    
    # check this row on left side
    for i in range(col):
       if board[row][i] == 1:
           return False

    # check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
       if board[i][j] == 1:
           return False
    # check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
       if board[i][j] == 1:
           return False

    return True

def solveNQUTil(board, col):
    # base case: If all queens are placed
    #then return true
    if col >= N:
        return True


   # consider this column and try placing 
   # this queen in all rows one by one    
    for i in range(N):
        if isSafe(board, i , col):

        # place this queen in board[i][col]
          board[i][col] = 1

        # recur to place rest of the queens
          if solveNQUTil(board, col + 1) == True:
             return True
        # if placing queen in board[i][col]
        # doesn't lead to a solution, then
        # queen from board[i][col]
          board[i][col] = 0

# if the queen can not be placed in any row in 
# this column col then return false
    return False

def solveNQ():
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]
    
    ]

    if solveNQUTil(board, 0) == False:
        print ("Solution does not exist")
        return False
    
    printSolution(board)
    return True
solveNQ()