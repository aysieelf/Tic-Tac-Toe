from src import constants as c


class GameState:
    """
    Class to represent the state of the game

    Attributes:
        grid (list[list[int]]): The grid of the game
        _current_player (int): The current player
        _game_over (bool): Whether the game is over or not
        _winner (str): The winner of the game
        _in_start_screen (bool): Whether the game is in the start screen or not
        _scores (dict[str, int]): The scores of the game
    """
    def __init__(self):
        self.grid: list[list[int]] = [[0] * c.GRID_SIZE for _ in range(c.GRID_SIZE)]
        self._current_player: int = 1
        self._game_over: bool = False
        self._winner: str | None = None
        self._in_start_screen: bool = True
        self._scores: dict[str, int] = {"X": 0, "O": 0, "Draws": 0}

    @property
    def current_player(self) -> int:
        return self._current_player

    @property
    def game_over(self) -> bool:
        return self._game_over

    @property
    def winner(self) -> str | None:
        return self._winner

    @property
    def in_start_screen(self) -> bool:
        return self._in_start_screen

    @property
    def scores(self) -> dict[str, int]:
        return self._scores.copy()

    def start_game(self) -> None:
        """
        Start the game. Set the in_start_screen attribute to False
        """
        self._in_start_screen = False

    def make_move(self, row: int, col: int) -> bool:
        """
        Make a move in the game. If the move is valid, update the grid,
        current player, and check if the game has ended.

        Args:
            row (int): The row of the cell
            col (int): The column of the cell

        Returns:
            bool: True if the move is valid, False otherwise
        """
        if self._game_over or self.grid[row][col] != 0:
            return False

        self.grid[row][col] = self.current_player
        self._current_player *= -1
        self._check_game_end()
        return True

    def _check_winner(self) -> bool:
        """
        Check if there is a winner in the game. A player wins if they have
        a row, column, or diagonal with the same value.

        Returns:
            bool: True if there is a winner, False otherwise
        """
        # Check rows
        for row in range(c.GRID_SIZE):
            if sum(self.grid[row]) == c.GRID_SIZE:  # X wins
                return True
            if sum(self.grid[row]) == c.GRID_SIZE * -1:  # O wins
                return True

        # Check columns
        for col in range(c.GRID_SIZE):
            column_sum = sum(self.grid[row][col] for row in range(c.GRID_SIZE))
            if column_sum == c.GRID_SIZE or column_sum == c.GRID_SIZE * -1:
                return True

        # Check diagonals
        diagonal1 = sum(self.grid[i][i] for i in range(c.GRID_SIZE))
        diagonal2 = sum(self.grid[i][c.GRID_SIZE - 1 - i] for i in range(c.GRID_SIZE))

        if diagonal1 == c.GRID_SIZE or diagonal1 == c.GRID_SIZE * -1:
            return True
        if diagonal2 == c.GRID_SIZE or diagonal2 == c.GRID_SIZE * -1:
            return True

        return False

    def _check_draw(self) -> bool:
        """
        Check if the game is a draw. The game is a draw if all cells are filled.

        Returns:
            bool: True if the game is a draw, False otherwise
        """
        for row in self.grid:
            if any(num == 0 for num in row):
                return False
        return True

    def _check_game_end(self) -> None:
        """
        Check if the game has ended. If there is a winner or a draw,
        update the game_over attribute and the scores.
        """
        if self._check_winner():
            self._game_over = True
            self._winner = "X" if self.current_player == -1 else "O"
            self._scores[self._winner] += 1

        if self._check_draw():
            self._game_over = True
            self._scores["Draws"] += 1

    def reset(self) -> None:
        """
        Reset the game state. Set the grid to all zeros, current player to 1,
        game_over to False, and winner to None.
        """
        self.grid = [[0] * c.GRID_SIZE for _ in range(c.GRID_SIZE)]
        self._current_player = 1
        self._game_over = False
        self._winner = None
