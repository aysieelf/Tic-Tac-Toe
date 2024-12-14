import pygame
from src import constants as c
from src.game_state import GameState
from src.game_logic import handle_click
from src.graphics import draw_grid

def main():
    pygame.init()
    screen = pygame.display.set_mode((c.WINDOW_SIZE, c.WINDOW_SIZE))
    game_state = GameState()

    run = True
    clicked = False
    while run:
        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                handle_click(pygame.mouse.get_pos(), game_state)

        # fill the screen with background color
        screen.fill(c.BACKGROUND_COLOR)

        # draw the grid
        draw_grid(screen)

        # update the display surface
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()