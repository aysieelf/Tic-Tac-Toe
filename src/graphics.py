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

    if game_state.game_over:
        draw_game_over(screen, game_state)


def draw_start_screen(screen: pygame.Surface):
    screen.fill(c.BACKGROUND_COLOR)

    draw_title(screen)
    draw_start_button(screen)


def draw_title(screen: pygame.Surface):
    title_font = pygame.font.SysFont(c.TITLE_FONT, c.TITLE_FONT_SIZE)
    title_surface = title_font.render(c.TITLE_TEXT, True, c.TITLE_COLOR)
    title_rect = title_surface.get_rect(centerx=c.WINDOW_SIZE // 2, y=c.TITLE_Y_POS)

    screen.blit(title_surface, title_rect)


def get_start_button_rect() -> pygame.Rect:
    return pygame.Rect(
        (c.WINDOW_SIZE - c.START_BUTTON_WIDTH) // 2,
        (c.WINDOW_SIZE - c.START_BUTTON_HEIGHT * 2.5),
        c.START_BUTTON_WIDTH,
        c.START_BUTTON_HEIGHT,
    )


def draw_start_button(screen: pygame.Surface | None):
    button_rect = get_start_button_rect()

    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        button_color = c.START_BUTTON_HOVER_COLOR
        button_text_color = c.START_BUTTON_TITLE_HOVER_COLOR
    else:
        button_color = c.START_BUTTON_COLOR
        button_text_color = c.START_BUTTON_TITLE_COLOR

    pygame.draw.rect(screen, button_color, button_rect)

    button_font = pygame.font.SysFont(None, c.START_BUTTON_FONT_SIZE)
    button_surface = button_font.render(c.START_BUTTON_TEXT, True, button_text_color)
    text_rect = button_surface.get_rect(center=button_rect.center)

    screen.blit(button_surface, text_rect)

    return button_rect


def draw_game_over(screen, game_state):
    overlay = pygame.Surface((c.WINDOW_SIZE, c.WINDOW_SIZE))
    overlay.set_alpha(200)
    overlay.fill(c.BLACK)
    screen.blit(overlay, (0, 0))

    font = pygame.font.Font(None, c.FONT_SIZE)

    if game_state.winner:
        text = f"Player {game_state.winner} wins!"
    else:
        text = "It's a draw!"

    text_surface = font.render(text, True, c.TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(c.WINDOW_SIZE // 2, c.WINDOW_SIZE // 2 - 30))
    screen.blit(text_surface, text_rect)

    small_font = pygame.font.Font(None, c.FONT_SIZE // 2)
    restart_text = 'Press "R" to try again'
    restart_surface = small_font.render(restart_text, True, c.TEXT_COLOR)
    restart_rect = restart_surface.get_rect(
        center=(c.WINDOW_SIZE // 2, c.WINDOW_SIZE // 2 + 20))
    screen.blit(restart_surface, restart_rect)
