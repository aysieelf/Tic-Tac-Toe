from src.event_handler import EventHandler
from src.game_state import GameState
from src.renderer import Renderer

import pygame


def game_loop(screen: pygame.Surface, game_state: GameState):
    event_handler = EventHandler(game_state)
    renderer = Renderer(screen)

    while True:
        if not event_handler.handle_events():
            break

        renderer.render(game_state)
