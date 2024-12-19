from src.event_handler import EventHandler
from src.game_state import GameState
from src.renderer import Renderer

import pygame


def game_loop(screen: pygame.Surface, game_state: GameState) -> None:
    """
    Handles the game loop

    Params:
        screen (pygame.Surface): The screen to render
        game_state (GameState): The current game state
    """
    event_handler = EventHandler(game_state)
    renderer = Renderer(screen)

    while True:
        if not event_handler.handle_events():
            break

        renderer.render(game_state)
