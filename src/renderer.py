from src import constants as c
from src.graphics import draw_board, draw_start_screen

import pygame


class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def render(self, game_state):
        self.screen.fill(c.BACKGROUND_COLOR)

        if game_state.in_start_screen:
            draw_start_screen(self.screen)
        else:
            draw_board(self.screen, game_state)

        pygame.display.flip()
