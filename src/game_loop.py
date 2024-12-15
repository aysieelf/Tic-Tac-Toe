import pygame

from src.graphics import draw_board
from src.utils import get_cell_from_mouse
from src.game_state import GameState
from src import constants as c


def game_loop(screen: pygame.Surface, game_state: GameState):
    run = True
    clicked = False
    while run:
        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked:
                clicked = False
                row, col = get_cell_from_mouse(pygame.mouse.get_pos())
                game_state.make_move(row, col)

        screen.fill(c.BACKGROUND_COLOR)
        draw_board(screen, game_state)
        pygame.display.flip()