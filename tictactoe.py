"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of x's
    # Count the number of o's
    # Since X starts first. if numX > numO -> O's Move
    
    numX = 0
    numO = 0
    for row in board:
        for cell in row:
            if cell == X:
                numX += 1
            elif cell == O:
                numO += 1
    
    if numX > numO:
        return O
    else:
        return X
    
  
        
    
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Create an empty set
    # Loop through cells, if they're empty then add them to the set
    
    moves = set()
    for i, row in  enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                moves.add((i,j))
    return moves       
    
    
    
  


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    actionI, actionJ = action
    
    if not((0 <= actionI <= 2) and (0 <= actionJ <=2)):
        raise IndexError("Action provided is out of bounds.")
    elif board[actionI][actionJ] != EMPTY:
        raise RuntimeError("Action unallowed: cell is not empty")
    else:
        newBoard[actionI][actionJ] = player(newBoard)
        return newBoard
        
    
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check Horizontal winner
    
    for row in board:
        if (row[0] == row[1] == row[2]) and (row[0] != EMPTY):
            return row[0]
        
    
    # Check Vertical Winner
    for j in range(3):
        if(board[0][j] == board[1][j] == board[2][j]) and (board[0][j] != EMPTY):
            return board[0][j]
    
    # Check Diagonal Winner
    if (board[0][0] == board[1][1] == board[2][2]) and (board[1][1] != EMPTY):
        return board[1][1]
    
    if (board[0][2] == board[1][1] == board[2][0]) and (board[1][1] != EMPTY):
        return board[1][1]
    
    # Else Return None
    
    return EMPTY

def fullBoard(board):
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True
            
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    return (winner(board) != EMPTY) or (fullBoard(board))
   


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerValue = winner(board)
    if(winnerValue == X):
        return 1
    elif(winnerValue == O):
        return -1
    else:
        return 0
    
def maxValue(board):
    v = - math.inf
    if terminal(board):
        return utility(board), EMPTY
    
    availableActions = actions(board)
    
    optimalAction = next(iter(availableActions))
    
    for action in availableActions:
        min_val, _ = minValue(result(board,action))
        maxResult = max(v,min_val )
        if maxResult > v:
            v = maxResult
            optimalAction = action
            if maxResult == 1:
                return v, optimalAction
        
    
    return v, optimalAction

def minValue(board):
    v =  math.inf
    if terminal(board):
        return utility(board), EMPTY
    
    availableActions = actions(board)
    
    optimalAction = next(iter(availableActions))
    
    for action in availableActions:
        max_val, _ = maxValue(result(board, action))
        minResult = min(v, max_val)

        if minResult < v:
            v = minResult
            optimalAction = action
            if minResult == -1:
                return v, optimalAction
            
        
    
    return v, optimalAction




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        return maxValue(board)[1]
    else:
        return minValue(board)[1]
