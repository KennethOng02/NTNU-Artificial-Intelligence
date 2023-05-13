import pygame

ROW = 0
COL = 0
HEIGHT = 0
WIDTH = 0
SQUARE_SIZE = 0
TEXT_HEIGHT = 50
BOARD = []

BLACK = pygame.Color('Black')
WHITE = pygame.Color('White')
RED = pygame.Color('Red')
GREY = pygame.Color('Grey')
BLUE = pygame.Color('Blue')

count = 0
if count == 0:
    try:
        with open("input.txt", "r") as f:
            row, col = [int(x) for x in f.readline().strip().split()]
            
            ROW = row
            COL = col
            HEIGHT = ROW * 100
            WIDTH = COL * 100
            SQUARE_SIZE = WIDTH // COL

            board = []
            for i in range(row):
                c = [int(x) for x in f.readline().strip().split()]
                board.append(c)
            
            BOARD = board

    except FileNotFoundError:
        print("Unable to find 'input.txt' file")
    
    count += 1