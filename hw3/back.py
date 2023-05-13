import numpy as np

class Board:
    def __init__(self, state, playerScore, opponentScore):
        self.state = state
        self.playerScore = playerScore
        self.opponentScore = opponentScore
        self.path = 0
        self.isRow = False

class Game:
    def __init__(self, board, win):
        self.board = board
        self.win = win
        self.brow, self.bcol = board.state.shape
   
    def solve(self):
        return self.alpha_beta_pruning(self.board, np.NINF, np.PINF, 0, False, True)
   
    def alpha_beta_pruning(self, board, alpha, beta, path, isRow, maximizing_player):
        if not board.state.any():
            return board.playerScore - board.opponentScore, board.path, board.isRow
       
        children = self.next_state(board, maximizing_player)
       
        if maximizing_player:
            value = np.NINF
            for child in children:
                maxEval, _, _ = self.alpha_beta_pruning(child, alpha, beta, path, isRow, False)
                value = max(value, maxEval)
                temp = alpha
                alpha = max(alpha, maxEval)
                if temp != alpha: # updated
                    path = child.path
                    isRow = child.isRow
                if beta <= alpha:
                    break
        else:
            value = np.PINF
            for child in children:
                minEval, _, _ = self.alpha_beta_pruning(child, alpha, beta, path, isRow, True)
                value = min(value, minEval)
                temp = beta
                beta = min(beta, minEval)
                if temp != beta: # updated
                    path = child.path
                    isRow = child.isRow
                if beta <= alpha:
                    break

        return value, path, isRow
   
    def next_state(self, board, maximizing_player):
        child_state = []
       
        row_move = np.count_nonzero(board.state, axis=1)
        col_move = np.count_nonzero(board.state, axis=0)

        best_score = row_move.max()
        for i in range(self.brow):
            if row_move[i] == best_score:
                new = Board(board.state.copy(), board.playerScore, board.opponentScore)
                new.state[i] = np.zeros(self.bcol)
                if maximizing_player:
                    new.playerScore += best_score
                else:
                    new.opponentScore += best_score
                new.path = i
                new.isRow = True
                child_state.append(new)
       
        best_score = col_move.max()
        for i in range(self.bcol):
            if col_move[i] == best_score:
                new = Board(board.state.copy(), board.playerScore, board.opponentScore)
                new.state[:,i] = np.zeros(self.brow)
                if maximizing_player:
                    new.playerScore += best_score
                else:
                    new.opponentScore += best_score
                new.path = i
                child_state.append(new)

        return child_state
   
    def is_terminal(self, board):
        return not np.any(board)

