import pygame
from constant import SQUARE_SIZE, ROW, COL, BLACK, WHITE, RED, BOARD, WIDTH, HEIGHT, TEXT_HEIGHT
from piece import Piece

class Board:
    def __init__(self):
        self.board = self.create_board()
        self.player_score = self.computer_score = 0
        
    def draw_square(self, win):
        win.fill(BLACK)
        for row in range(COL):
            for col in range(row % 2, ROW, 2):
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_score(self, win, font):
        text = font.render(f'Player: {self.player_score}   Computer: {self.computer_score}', True, WHITE, BLACK)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT + TEXT_HEIGHT // 2)
        win.blit(text, text_rect)
    
    def evaluate(self):
        return self.player_score - self.computer_score
    
    def get_all_pieces(self):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0:
                    pieces.append(piece)
        return pieces
    
    def move(self, row, col, maximizing_player, isRow=True):
        count = 0
        if isRow:
            for i in range(COL):
                if self.board[row][i]:
                    self.board[row][i] = 0
                    count += 1
        else:
            for i in range(ROW):
                if self.board[i][col]:
                    self.board[i][col] = 0
                    count += 1
        if maximizing_player:
            self.player_score += count
        else:
            self.computer_score += count

    def get_piece(self, row, col):
        return self.board[row][col]
    
    def create_board(self):
        board = []
        for row in range(ROW):
            board.append([])
            for col in range(COL):
                if BOARD[row][col]:
                    board[row].append(Piece(row, col))
                else:
                    board[row].append(0)
        return board
    
    def draw(self, win):
        self.draw_square(win)
        for row in range(ROW):
            for col in range(COL):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
    
    def get_piece(self, row, col):
        return self.board[row][col]

    def winner(self):
        if all(x == 0 for v in self.board for x in v):
            if self.player_score > self.computer_score:
                return True
            elif self.player_score < self.computer_score:
                return False
            else:
                return False
        return None
    
    def get_valid_move(self, piece):
        moves = []
        row = piece.row
        col = piece.col
        for i in range(COL):
            if((row, i) != (row, col)):
                moves.append((row, i))
        for i in range(ROW):
            if((i, col) != (row, col)):
                moves.append((i, col))
        return moves