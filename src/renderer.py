from src import constants as c
from src.game_state import GameState
from src.graphics import draw_board, draw_start_screen

import pygame


class Renderer:
    """
    Class to render the game state on the screen

    Attributes:
        screen (pygame.Surface): The screen to render on
    """

    def __init__(self, screen):
        self.screen = screen

    def render(self, game_state: GameState) -> None:
        """
        Render the game state on the screen

        Args:
            game_state (GameState): The current game state
        """
        self.screen.fill(c.BACKGROUND_COLOR)

        if game_state.in_start_screen:
            draw_start_screen(self.screen)
        else:
            draw_board(self.screen, game_state)

        pygame.display.flip()
