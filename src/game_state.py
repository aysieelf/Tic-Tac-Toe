from src import constants as c


class GameState:
    def __init__(self):
        self.grid = [[0] * c.GRID_SIZE for _ in range(c.GRID_SIZE)]
        self._current_player = 1
        self._game_over = False
        self._winner = None
        self._in_start_screen = True

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

    def start_game(self):
        self._in_start_screen = False

    def make_move(self, row: int, col: int) -> bool:
        if self._game_over or self.grid[row][col] != 0:
            return False

        self.grid[row][col] = self.current_player
        self._current_player *= -1
        self._check_game_end()
        return True

    def _check_winner(self) -> bool:
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
        for row in self.grid:
            if any(num == 0 for num in row):
                return False
        return True

    def _check_game_end(self):
        if self._check_winner():
            self._game_over = True
            self._winner = "X" if self.current_player == -1 else "O"

        if self._check_draw():
            self._game_over = True

    def reset(self):
        self.grid = [[0] * c.GRID_SIZE for _ in range(c.GRID_SIZE)]
        self._current_player = 1
        self._game_over = False
        self._winner = None
        self._in_start_screen = True
