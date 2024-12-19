from src.game_state import GameState
from src.graphics import get_start_button_rect
from src.utils import get_cell_from_mouse

import pygame


class EventHandler:
    """
    Class to handle all the events in the game

    Args:
        game_state (GameState): The current game state

    Attributes:
        game_state (GameState): The current game state
        clicked (bool): Whether the mouse is clicked or not
    """
    def __init__(self, game_state: GameState) -> None:
        self.game_state = game_state
        self.clicked: bool = False

    def handle_events(self) -> bool:
        """
        Handle all the events in the game

        Returns:
            bool: True if the game should continue, False if the game should end
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                self.handle_keyboard(event)
                if not self.handle_keyboard(event):
                    return False

            self.handle_mouse(event)
        return True

    def handle_keyboard(self, event: pygame.event.Event) -> bool:
        """
        Handle the keyboard events

        Args:
            event (pygame.event): The event to handle
                - R key: Resets the game
                - Q key: Exits the game

        Returns:
            bool: True if the game should continue, False if the game should end
        """
        if event.key == pygame.K_r:
            self.game_state.reset()
        elif event.key == pygame.K_q:
            pygame.quit()
            return False
        return True

    def handle_mouse(self, event: pygame.event.Event) -> None:
        """
        Handle the mouse events

        Args:
            event (pygame.event): The event to handle
        """
        if event.type == pygame.MOUSEBUTTONDOWN and not self.clicked:
            self.clicked = True
        if event.type == pygame.MOUSEBUTTONUP and self.clicked:
            self.clicked = False
            self.process_click()

    def process_click(self) -> None:
        """
        Process the click event
        """
        if self.game_state.in_start_screen:
            self.handle_start_screen_click()

        else:
            self.handle_game_click()

    def handle_start_screen_click(self) -> None:
        """
        Handle the click event in the start screen
        """
        button_rect = get_start_button_rect()
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            self.game_state.start_game()

    def handle_game_click(self):
        """
        Handle the click event in the game
        """
        row, col = get_cell_from_mouse(pygame.mouse.get_pos())
        self.game_state.make_move(row, col)
