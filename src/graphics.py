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


def draw_x(screen, row, col):
    x = col * c.CELL_SIZE
    y = row * c.CELL_SIZE

    start_pos1 = (x + c.X_PADDING, y + c.X_PADDING)
    end_pos1 = (x + c.CELL_SIZE - c.X_PADDING, y + c.CELL_SIZE - c.X_PADDING)

    start_pos2 = (x + c.X_PADDING, y + c.CELL_SIZE - c.X_PADDING)
    end_pos2 = (x + c.CELL_SIZE - c.X_PADDING, y + c.X_PADDING)

    pygame.draw.line(screen, c.X_COLOR, start_pos1, end_pos1, c.X_WIDTH)
    pygame.draw.line(screen, c.X_COLOR, start_pos2, end_pos2, c.X_WIDTH)


def draw_o(screen, row, col):
    x = col * c.CELL_SIZE
    y = row * c.CELL_SIZE

    center = (x + c.CELL_SIZE // 2, y + c.CELL_SIZE // 2)
    radius = c.CELL_SIZE // 2 - c.O_PADDING

    pygame.draw.circle(screen, c.O_COLOR, center, radius, c.O_WIDTH)


def draw_board(screen, game_state):
    draw_grid(screen)

    for row in range(c.GRID_SIZE):
        for col in range(c.GRID_SIZE):
            if game_state.grid[row][col] == 1:
                draw_x(screen, row, col)
            elif game_state.grid[row][col] == -1:
                draw_o(screen, row, col)
