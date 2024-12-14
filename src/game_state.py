from src import constants as c

class GameState:
    def __init__(self):
        self.grid = [[None] * c.GRID_SIZE for _ in range(c.GRID_SIZE)]
        self.current_player = 'X'