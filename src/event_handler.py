import pygame

from src.graphics import draw_start_button, get_start_button_rect
from src.utils import get_cell_from_mouse


class EventHandler:
    def __init__(self, game_state):
        self.game_state = game_state
        self.clicked = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                self.handle_keyboard(event)

            self.handle_mouse(event)
        return True

    def handle_keyboard(self, event):
        if event.key == pygame.K_r:
            self.game_state.reset()

    def handle_mouse(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.clicked:
            self.clicked = True
        if event.type == pygame.MOUSEBUTTONUP and self.clicked:
            self.clicked = False
            self.process_click()

    def process_click(self):
        if self.game_state.in_start_screen:
            self.handle_start_screen_click()

        else:
            self.handle_game_click()

    def handle_start_screen_click(self):
        button_rect = get_start_button_rect()
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            self.game_state.start_game()

    def handle_game_click(self):
        row, col = get_cell_from_mouse(pygame.mouse.get_pos())
        self.game_state.make_move(row, col)
