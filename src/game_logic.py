from src.game_state import GameState
from src.utils import get_cell_from_mouse


def handle_click(pos: tuple, game_state: GameState, player) -> int:
    row, col = get_cell_from_mouse(pos)
    if game_state.grid[row][col] is None:
        game_state.grid[row][col] = player
        print([row for row in game_state.grid])
        player *= -1
        return player
    return player
