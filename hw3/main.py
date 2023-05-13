# Install dependencies
#
#
# pip install -r requirements.txt
# or
# pip3 install -r requirements.txt
#
#
# how to execute
#
#
# python main.py
# or
# python3 main.py

# input
#
# stored in file named "input.txt"
#
# <row_num> <col_num>
# boards filled with 1's and 0's separated by space
#
# example:
# 4 3
# 1 0 0 1
# 0 0 0 1
# 1 1 1 1

import pygame
import time
from game import Game
from constant import WIDTH, HEIGHT, SQUARE_SIZE, TEXT_HEIGHT
from computer import alpha_beta_pruning

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# output the required value into "output.txt"
def hw_out(game):
    start = time.time()
    score, (_, pos, is_row) = alpha_beta_pruning(game.get_board(), 6, True, game) 
    end = time.time()
    
    with open("output.txt", "w") as f:
        if is_row:
            f.write(f'Row #: {pos + 1}\n')
        else:
            f.write(f'Column #: {pos + 1}\n')
        f.write(f'{score} points\n')
        f.write(f'Total run time = {end - start} seconds.')

FPS = 60

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT + TEXT_HEIGHT))
FONT = pygame.font.Font(None, 32)
pygame.display.set_caption('縱橫殺棋對抗賽')

if __name__ == "__main__":
    game = Game(WIN, FONT)
    
    hw_out(game)
    
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        
        # computer move
        if not game.player_turn:
            value, (new_board, _, _) = alpha_beta_pruning(game.get_board(), 6, False, game)
            game.ai_move(new_board)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

        if game.winner() != None:
            pygame.time.delay(2000)
            run = False
        
    pygame.quit()