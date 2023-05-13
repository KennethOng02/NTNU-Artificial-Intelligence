import pygame
from board import Board
from constant import WIDTH, HEIGHT, BLUE, SQUARE_SIZE, ROW, COL, WHITE, BLACK
from computer import *

class Game:
    def __init__(self, win, font):
        self.win = win
        self.font = font
        self.board = Board()
        self.player_turn = True
        self.selected = None
        self.valid_moves = []

    def update(self):
        self.board.draw(self.win)
        self.board.draw_score(self.win, self.font)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
    
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0:
            self.selected = piece
            self.valid_moves = self.board.get_valid_move(piece)
            return True
        return False
        
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and (row, col) in self.valid_moves:
            for r, c in self.valid_moves:
                if not (row == r and col == c):
                    if row == r:
                        self.board.move(row, col, True, isRow=True)
                        break
                    elif col == c:
                        self.board.move(row, col, True, isRow=False)
                        break
            self.change_turn()
        else:
            return False
        return True
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def winner(self):
        return self.board.winner()

    def change_turn(self):
        self.valid_moves = {}
        self.player_turn = not self.player_turn
    
    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()