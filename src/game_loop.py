from src import constants as c
from src.game_state import GameState
from src.graphics import draw_board, draw_title, draw_start_screen, draw_start_button
from src.utils import get_cell_from_mouse

import pygame


def game_loop(screen: pygame.Surface, game_state: GameState):
    run = True
    clicked = False
    while run:
        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_state.reset()

            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked:
                clicked = False
                if game_state.in_start_screen:
                    button_rect = draw_start_button(screen)
                    if button_rect.collidepoint(pygame.mouse.get_pos()):
                        game_state.start_game()
                else:
                    row, col = get_cell_from_mouse(pygame.mouse.get_pos())
                    game_state.make_move(row, col)

        screen.fill(c.BACKGROUND_COLOR)

        if game_state.in_start_screen:
            draw_start_screen(screen)
        else:
            draw_board(screen, game_state)

        pygame.display.flip()