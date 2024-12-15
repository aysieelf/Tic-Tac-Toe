import pygame

from src import constants as c
from src.game_loop import game_loop
from src.game_state import GameState


def main():
    pygame.init()
    screen = pygame.display.set_mode((c.WINDOW_SIZE, c.WINDOW_SIZE))
    game_state = GameState()

    game_loop(screen, game_state)

    pygame.quit()


if __name__ == "__main__":
    main()
