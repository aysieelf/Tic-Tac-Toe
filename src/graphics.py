from src import constants as c

import pygame


def draw_grid(screen):
    # draw vertical lines
    for x in range(1, c.GRID_SIZE):
        pygame.draw.line(
            screen,
            c.GRID_COLOR,
            (x * c.CELL_SIZE, 0),
            (x * c.CELL_SIZE, c.WINDOW_SIZE),
            c.LINE_WIDTH,
        )

    # draw horizontal lines
    for y in range(1, c.GRID_SIZE):
        pygame.draw.line(
            screen,
            c.GRID_COLOR,
            (0, y * c.CELL_SIZE),
            (c.WINDOW_SIZE, y * c.CELL_SIZE),
            c.LINE_WIDTH,
        )
