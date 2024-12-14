from src.game_state import GameState
from src.utils import get_cell_from_mouse
from src import constants as c


def handle_click(pos: tuple, game_state: GameState, player) -> int:
    row, col = get_cell_from_mouse(pos)
    if game_state.grid[row][col] == 0:
        game_state.grid[row][col] = player
        print(game_state.grid)
        player *= -1
        return player
    return player


def check_winner(game_state: GameState) -> bool:
    # Check rows
    for row in range(c.GRID_SIZE):
        if sum(game_state.grid[row]) == c.GRID_SIZE:  # X wins
            return True
        if sum(game_state.grid[row]) == c.GRID_SIZE * -1:  # O wins
            return True

    # Check columns
    for col in range(c.GRID_SIZE):
        column_sum = sum(game_state.grid[row][col] for row in range(c.GRID_SIZE))
        if column_sum == c.GRID_SIZE or column_sum == c.GRID_SIZE * -1:
            return True

    # Check diagonals
    diagonal1 = sum(game_state.grid[i][i] for i in range(c.GRID_SIZE))
    diagonal2 = sum(game_state.grid[i][c.GRID_SIZE - 1 - i] for i in range(c.GRID_SIZE))

    if diagonal1 == c.GRID_SIZE or diagonal1 == c.GRID_SIZE * -1:
        return True
    if diagonal2 == c.GRID_SIZE or diagonal2 == c.GRID_SIZE * -1:
        return True

    return False

def check_draw(game_state: GameState) -> bool:
    for row in game_state.grid:
        if any(num for num in row if num == 0):
            return False

    return True