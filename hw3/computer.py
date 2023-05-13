from copy import deepcopy
from constant import ROW, COL
from board import Board

def alpha_beta_pruning(position, depth, maximizing_player, game, alpha=None, beta=None):
    pos = None
    is_row = None

    if depth == 0 or position.winner() != None:
        return position.evaluate(), (position, pos, is_row)
    
    if not alpha and not beta:
        alpha = -float('inf')
        beta = float('inf')
   
    children = get_next_move(position, maximizing_player)
   
    if maximizing_player:
        maxEval = -float('inf')
        best_move = None
        for child, p, ir in children:
            evaluation = alpha_beta_pruning(child, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, maxEval)
            if maxEval >= beta: # pruning
                break
            if maxEval == evaluation:
                best_move = child
                pos = p
                is_row = ir
        return maxEval, (best_move, pos, is_row)
    else:
        minEval = float('inf')
        best_move = None
        for child, p, ir in children:
            evaluation = alpha_beta_pruning(child, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            beta = min(beta, minEval)
            if minEval <= alpha: # pruning
                break
            if minEval == evaluation:
                best_move = child
                is_row = ir
        return minEval, (best_move, pos, is_row)

def simulate(move, board, maximizing_player, isRow=True):
    board.move(move, move, maximizing_player, isRow)
    return board

# select the best next move by the number of pieces in row and col
def get_next_move(board, maximizing_player):
    moves = []
   
    rowMove = [0 for i in range(ROW)]
    colMove = [0 for i in range(COL)]

    for i in range(ROW):
        for j in range(COL):
            if board.board[i][j]:
                rowMove[i] += 1

    for i in range(COL):
        for j in range(ROW):
            if board.board[j][i]:
                colMove[i] += 1
    
    best_score = max(rowMove)
    for i in range(ROW):
        if rowMove[i] == best_score:
            temp_board = deepcopy(board)
            new_board = simulate(i, temp_board, maximizing_player, isRow=True)
            moves.append((new_board, i, True))
   
    best_score = max(colMove)
    for i in range(COL):
        if colMove[i] == best_score:
            temp_board = deepcopy(board)
            new_board = simulate(i, temp_board, maximizing_player, isRow=False)
            moves.append((new_board, i, False))

    return moves