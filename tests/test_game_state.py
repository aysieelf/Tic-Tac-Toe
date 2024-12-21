import unittest

from src.game_state import GameState


class GameStateShould(unittest.TestCase):
    def test_init_initializesSuccessfully(self):
        game_state = GameState()
        self.assertIsNotNone(game_state)

    def test_init_createsPlayerOne(self):
        game_state = GameState()
        self.assertEqual(game_state.current_player, 1)

    def test_init_createsGrid(self):
        game_state = GameState()
        self.assertEqual(
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            game_state.grid,
        )

    def test_init_createsGameOverFalse(self):
        game_state = GameState()
        self.assertFalse(game_state.game_over)

    def test_init_createsWinnerNone(self):
        game_state = GameState()
        self.assertIsNone(game_state.winner)

    def test_init_createsInStartScreenTrue(self):
        game_state = GameState()
        self.assertTrue(game_state.in_start_screen)

    def test_init_createsScores(self):
        game_state = GameState()
        self.assertEqual(
            {"X": 0, "O": 0, "Draws": 0},
            game_state.scores,
        )

    def test_startGame_setsInStartScreenFalse(self):
        game_state = GameState()
        game_state.start_game()
        self.assertFalse(game_state.in_start_screen)

    def test_makeMove_returnsFalseWhenGameOver(self):
        game_state = GameState()
        game_state._game_over = True
        self.assertFalse(game_state.make_move(0, 0))

    def test_makeMove_returnsFalseWhenCellOccupied(self):
        game_state = GameState()
        game_state.grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertFalse(game_state.make_move(0, 0))

    def test_makeMove_updatesGridForValidMove(self):
        game_state = GameState()
        game_state.make_move(0, 0)
        self.assertEqual([[1, 0, 0], [0, 0, 0], [0, 0, 0]], game_state.grid)

    def test_makeMove_updatesCurrentPlayerForValidMove(self):
        game_state = GameState()
        game_state.make_move(0, 0)
        self.assertEqual(-1, game_state.current_player)

    def test_makeMove_returnsTrueForValidMove(self):
        game_state = GameState()
        self.assertTrue(game_state.make_move(0, 0))

    def test_checkWinner_returnsTrueWhenRowWin(self):
        game_state = GameState()
        game_state.grid = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
        self.assertTrue(game_state._check_winner())

    def test_checkWinner_returnsTrueWhenColWin(self):
        game_state = GameState()
        game_state.grid = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
        self.assertTrue(game_state._check_winner())

    def test_checkWinner_returnsTrueWhenDiagonalOneWin(self):
        game_state = GameState()
        game_state.grid = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertTrue(game_state._check_winner())

    def test_checkWinner_returnsTrueWhenDiagonalTwoWin(self):
        game_state = GameState()
        game_state.grid = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
        self.assertTrue(game_state._check_winner())

    def test_checkWinner_returnsFalseWhenNoWin(self):
        game_state = GameState()
        game_state.grid = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertFalse(game_state._check_winner())

    def test_checkDraw_returnsTrueWhenDraw(self):
        game_state = GameState()
        game_state.grid = [[1, 1, -1], [-1, -1, 1], [1, -1, 1]]
        self.assertTrue(game_state._check_draw())

    def test_checkDraw_returnsFalseWhenNotDraw(self):
        game_state = GameState()
        game_state.grid = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertFalse(game_state._check_draw())

    def test_checkGameEnd_setsGameOverToTrue(self):
        game_state = GameState()
        game_state.grid = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
        game_state._check_game_end()
        self.assertTrue(game_state.game_over)

    def test_checkGameEnd_setsWinnerToX(self):
        game_state = GameState()
        game_state.grid = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
        game_state._current_player = -1
        game_state._check_game_end()

        self.assertEqual("X", game_state.winner)
        self.assertTrue(game_state.game_over)
        self.assertEqual(1, game_state.scores["X"])

    def test_checkGameEnd_setsWinnerToO(self):
        game_state = GameState()
        game_state.grid = [[-1, -1, -1], [0, 0, 0], [0, 0, 0]]
        game_state._current_player = 1
        game_state._check_game_end()

        self.assertEqual("O", game_state.winner)
        self.assertTrue(game_state.game_over)
        self.assertEqual(1, game_state.scores["O"])

    def test_checkGameEnd_setsWinnerToNone(self):
        game_state = GameState()
        game_state.grid = [[1, 1, -1], [-1, -1, 1], [1, -1, 1]]
        game_state._check_game_end()
        self.assertIsNone(game_state.winner)

    def test_reset_setsGridToZeros(self):
        game_state = GameState()
        game_state.grid = [[1, 1, -1], [-1, -1, 1], [1, -1, 1]]
        game_state.reset()
        self.assertEqual([[0, 0, 0], [0, 0, 0], [0, 0, 0]], game_state.grid)

    def test_reset_setsCurrentPlayerToOne(self):
        game_state = GameState()
        game_state._current_player = -1
        game_state.reset()
        self.assertEqual(1, game_state.current_player)

    def test_reset_setsGameOverToFalse(self):
        game_state = GameState()
        game_state._game_over = True
        game_state.reset()
        self.assertFalse(game_state.game_over)

    def test_reset_setsWinnerToNone(self):
        game_state = GameState()
        game_state._winner = "X"
        game_state.reset()
        self.assertIsNone(game_state.winner)
