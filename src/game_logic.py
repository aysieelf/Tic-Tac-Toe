from src import constants as c
from src.game_state import GameState
from src.utils import get_cell_from_mouse

def handle_click(pos: tuple, game_state: GameState) -> bool:
    row, col = get_cell_from_mouse(pos)
    if game_state.grid[row][col] is None:
        game_state.grid[row][col] = "X"
        print('X')
        return True
    return False
