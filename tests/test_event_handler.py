import unittest
from unittest.mock import Mock, patch

from src.event_handler import EventHandler
from src.game_state import GameState

import pygame


class EventHandlerShould(unittest.TestCase):
    def setUp(self):
        self.game_state = GameState()
        self.event_handler = EventHandler(self.game_state)

    def test_init_initializesSuccessfully(self):
        self.assertIsNotNone(self.event_handler)

    def test_init_setsClickedToFalse(self):
        self.assertFalse(self.event_handler.clicked)

    def test_handleEvents_returnsFalse_whenQuitEvent(self):
        mock_event = Mock()
        mock_event.type = pygame.QUIT

        with patch("pygame.event.get", return_value=[mock_event]):
            result = self.event_handler.handle_events()

            self.assertFalse(result)

    def test_handleEvents_returnsFalse_whenKeyboardEventFalse(self):
        mock_event = Mock()
        mock_event.type = pygame.KEYDOWN
        mock_event.key = pygame.K_q

        with (
            patch("pygame.event.get", return_value=[mock_event]),
            patch.object(EventHandler, "handle_keyboard", return_value=False),
        ):
            result = self.event_handler.handle_events()

            self.assertFalse(result)

    def test_handleEvents_returnsTrue_whenKeyboardEventTrue(self):
        mock_event = Mock()
        mock_event.type = pygame.KEYDOWN
        mock_event.key = pygame.K_q

        with (
            patch("pygame.event.get", return_value=[mock_event]),
            patch.object(EventHandler, "handle_keyboard", return_value=True),
        ):
            result = self.event_handler.handle_events()

            self.assertTrue(result)

    def test_handleKeyboard_resetsGameState_whenRKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_r

        with patch.object(self.game_state, "reset") as mock_reset:
            self.event_handler.handle_keyboard(mock_event)

            mock_reset.assert_called_once()

    def test_handleKeyboard_returnsTrue_whenRKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_r

        result = self.event_handler.handle_keyboard(mock_event)

        self.assertTrue(result)

    def test_handleKeyboard_quitsPygame_whenQKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_q

        with patch("pygame.quit") as mock_quit:
            self.event_handler.handle_keyboard(mock_event)

            mock_quit.assert_called_once()

    def test_handleKeyboard_returnsFalse_whenQKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_q

        result = self.event_handler.handle_keyboard(mock_event)

        self.assertFalse(result)

    def test_handleMouse_setsClickedToTrue_whenMouseDown(self):
        mock_event = Mock()
        mock_event.type = pygame.MOUSEBUTTONDOWN

        self.event_handler.handle_mouse(mock_event)

        self.assertTrue(self.event_handler.clicked)

    def test_handleMouse_setsClickedToFalse_whenMouseUpAndClicked(self):
        self.event_handler._clicked = True
        mock_event = Mock()
        mock_event.type = pygame.MOUSEBUTTONUP

        with patch.object(self.event_handler, "process_click"):
            self.event_handler.handle_mouse(mock_event)

        self.assertFalse(self.event_handler.clicked)

    def test_handleMouse_callsProcessClick_whenMouseUpAndClicked(self):
        self.event_handler._clicked = True
        mock_event = Mock()
        mock_event.type = pygame.MOUSEBUTTONUP

        with patch.object(self.event_handler, "process_click") as mock_process_click:
            self.event_handler.handle_mouse(mock_event)

            mock_process_click.assert_called_once()

    def test_processClick_callsHandleStartScreenClick_whenGameStateInStartScreenTrue(
        self,
    ):
        self.game_state._in_start_screen = True

        with patch.object(
            self.event_handler, "handle_start_screen_click"
        ) as mock_handle_start_screen_click:
            self.event_handler.process_click()

            mock_handle_start_screen_click.assert_called_once()

    def test_processClick_callsHandleGameClick_whenGameStateInStartScreenFalse(self):
        self.game_state._in_start_screen = False

        with patch.object(
            self.event_handler, "handle_game_click"
        ) as mock_handle_game_click:
            self.event_handler.process_click()

            mock_handle_game_click.assert_called_once()

    def test_handleStartScreenClick_setsInStartScreenToTrue_whenClickOnButton(self):
        self.game_state._in_start_screen = True
        mock_button_rect = Mock()
        mock_button_rect.collidepoint.return_value = True
        mock_pos = (0, 0)

        with (
            patch(
                "src.event_handler.get_start_button_rect", return_value=mock_button_rect
            ),
            patch("pygame.mouse.get_pos", return_value=mock_pos),
        ):
            self.event_handler.handle_start_screen_click()

            mock_button_rect.collidepoint.assert_called_once_with(mock_pos)
            self.assertFalse(self.game_state.in_start_screen)

    def test_handleStartScreenClick_doesNotSetInStartScreenToTrue_whenClickNotOnButton(
        self,
    ):
        self.game_state._in_start_screen = True
        mock_button_rect = Mock()
        mock_button_rect.collidepoint.return_value = False
        mock_pos = (0, 0)

        with (
            patch(
                "src.event_handler.get_start_button_rect", return_value=mock_button_rect
            ),
            patch("pygame.mouse.get_pos", return_value=mock_pos),
        ):
            self.event_handler.handle_start_screen_click()

            mock_button_rect.collidepoint.assert_called_once_with(mock_pos)
            self.assertTrue(self.game_state.in_start_screen)

    def test_handleGameClick_callsMakeMoveWithRowAndCol(self):
        mock_pos = (0, 0)
        with (
            patch("pygame.mouse.get_pos", return_value=mock_pos),
            patch("src.utils.get_cell_from_mouse", return_value=mock_pos),
            patch.object(self.game_state, "make_move") as mock_make_move,
        ):
            self.event_handler.handle_game_click()

            mock_make_move.assert_called_once_with(0, 0)
