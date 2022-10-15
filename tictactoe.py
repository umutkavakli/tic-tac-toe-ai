"""
Tic Tac Toe Player
"""
from copy import deepcopy

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
    
    countX = 0
    countO = 0

    for row in board:
        countX += row.count(X)
        countO += row.count(O)

    return X if countX <= countO else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = deepcopy(board)
    i, j = action

    if board[i][j] != EMPTY:
        raise "Invalid"
    
    new_board[i][j] = player(board)
    
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for player in (X, O):

        # horizontal check
        for row in board:
            if row == [player] * 3:
                return player
        
        # vertical check
        for col in range(3):
            column = [board[i][col] for i in range(3)]
            if column == [player] * 3:
                return player

        # diagonal check
        if [board[i][i] for i in range(3)] == [player] * 3:
            return player

        elif [board[i][j] for i, j in zip(range(3), range(2, -1, -1))] == [player] * 3:
            return player

    # tie
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True

    for row in board:
        if EMPTY in row:
            return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    current = player(board)

    if terminal(board):
        return None

    return maximize(board)[1] if current == X else minimize(board)[1]
    
def maximize(board):
    optimal = ()
    v = -10

    if terminal(board):
        return utility(board), optimal
    
    for action in actions(board):
        value = minimize(result(board, action))[0]
        if value > v:
            v = value
            optimal = action
    
    return v, optimal

def minimize(board):
    optimal = ()
    v = 10

    if terminal(board):
        return utility(board), optimal
    
    for action in actions(board):
        value = maximize(result(board, action))[0]
        if value < v:
            v = value
            optimal = action
    
    return v, optimal

