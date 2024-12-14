from src import constants as c


def get_cell_from_mouse(pos: tuple) -> tuple:
    x, y = pos
    row = y // c.CELL_SIZE
    col = x // c.CELL_SIZE
    return row, col
