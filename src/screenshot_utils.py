from datetime import datetime
import os

import pygame


class ScreenshotManager:
    def __init__(self, base_path="assets/screenshots"):
        """Initialize the screenshot manager with a base directory path."""
        self.base_path = base_path
        self._ensure_directory_exists()

    def _ensure_directory_exists(self):
        """Create the screenshots directory if it doesn't exist."""
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    def capture(self, screen: pygame.Surface, name: str):
        """
        Capture a screenshot of the current game state.

        Args:
            screen: The pygame surface to capture
            name: Name for the screenshot (e.g., 'start_screen', 'game_in_progress')
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(self.base_path, filename)

        pygame.image.save(screen, filepath)
        print(f"Screenshot saved: {filepath}")

    def capture_game_state(self, screen: pygame.Surface, game_state):
        """
        Intelligent capture based on current game state.

        Args:
            screen: The pygame surface to capture
            game_state: Current GameState instance
        """
        if game_state.in_start_screen:
            self.capture(screen, "start_screen")
        elif game_state.game_over:
            if game_state.winner:
                self.capture(screen, f"{game_state.winner}_wins")
            else:
                self.capture(screen, "draw_game")
        else:
            moves = sum(row.count(1) + row.count(-1) for row in game_state.grid)
            if moves == 0:
                self.capture(screen, "empty_board")
            else:
                self.capture(screen, f"game_in_progress_moves_{moves}")
