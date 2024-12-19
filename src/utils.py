from src import constants as c


def get_cell_from_mouse(pos: tuple) -> tuple[int, int]:
    """
    Get the cell from the mouse position.
    The cell is represented by the row and column of the cell.

    Args:
        pos (tuple): The position of the mouse

    Returns:
        tuple: The row and column of the cell
    """
    x, y = pos
    row = y // c.CELL_SIZE
    col = x // c.CELL_SIZE
    return row, col
