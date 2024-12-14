from src import constants as c
from src.game_logic import handle_click, check_winner, check_draw
from src.game_state import GameState
from src.graphics import draw_board

import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((c.WINDOW_SIZE, c.WINDOW_SIZE))
    game_state = GameState()

    run = True
    clicked = False
    player = 1
    game_over = False
    winner = "No one"

    while run:
        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked:
                clicked = False
                player = handle_click(pygame.mouse.get_pos(), game_state, player)

                if check_winner(game_state):
                    winner = "X" if player == -1 else "O"
                    game_over = True

                if check_draw(game_state):
                    game_over = True

                if game_over:
                    print(f"Game Over! {winner} wins!")
        screen.fill(c.BACKGROUND_COLOR)
        draw_board(screen, game_state)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
