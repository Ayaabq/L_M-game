import pygame
import sys
from game import Game
from utils import load_levels_from_json
from piece import Piece  

pygame.init()


TILE_SIZE = 80
GRID_SIZE = 5
WINDOW_SIZE = GRID_SIZE * TILE_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = {
    "red": (255, 0, 0),
    "purple": (128, 0, 128),
    "grey": (128, 128, 128),
    "blocked": (0, 0, 0)
}

def draw_board(screen, game):
    screen.fill(WHITE)
    
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            pygame.draw.rect(screen, BLACK, (y * TILE_SIZE, x * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
            piece = game.board.grid[x][y]
            if piece != 'empty':
                color = COLORS.get(piece.color, BLACK) if isinstance(piece, Piece) else COLORS.get(piece, BLACK)
                pygame.draw.rect(screen, color, (y * TILE_SIZE, x * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    pygame.display.flip()

def main():
    levels = load_levels_from_json('logic_magnets/levels.json')
    level = int(input("Choose a level (0 for level 1, 1 for level 2, etc.): "))
    game = Game(levels, level_index=level)
    
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Logic Magnets")

    selected_piece = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = y // TILE_SIZE
                col = x // TILE_SIZE
                
                if selected_piece is None:
                    selected_piece = (row, col) if game.board.grid[row][col] != 'empty' else None
                else:
                    game.move_piece(selected_piece, (row, col))
                    selected_piece = None

        draw_board(screen, game)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
