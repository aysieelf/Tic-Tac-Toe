from src import constants as c
from src.event_handler import EventHandler
from src.game_state import GameState
from src.graphics import draw_board, draw_title, draw_start_screen, draw_start_button
from src.renderer import Renderer
from src.utils import get_cell_from_mouse

import pygame


def game_loop(screen: pygame.Surface, game_state: GameState):
    event_handler = EventHandler(game_state)
    renderer = Renderer(screen)

    while True:
        if not event_handler.handle_events():
            break

        renderer.render(game_state)