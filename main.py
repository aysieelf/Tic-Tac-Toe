from src import constants as c
from src.game_loop import game_loop
from src.game_state import GameState

import pygame


def main() -> None:
    """
    Main function to run the game.
    Initializes the game and runs the game loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((c.WINDOW_SIZE, c.WINDOW_SIZE))
    game_state = GameState()

    game_loop(screen, game_state)

    pygame.quit()


if __name__ == "__main__":
    main()


# TODO: Add tests for the game
"""
- game_state.py
- utils.py
- event_handler.py
"""
