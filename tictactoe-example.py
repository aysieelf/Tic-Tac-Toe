import pygame

# initialize Pygame
pygame.init()


# CONSTANTS --------------------------------------------------------------------
WINDOW_SIZE = 300  # width and height of the window
GRID_SIZE = 3  # number of cells in the grid (3x3)
CELL_SIZE = WINDOW_SIZE // GRID_SIZE  # size of each cell
LINE_WIDTH = 4 # width of the lines that form the grid


# COLORS -----------------------------------------------------------------------
BACKGROUND_COLOR = (248, 237, 235)
GRID_COLOR = (244, 149, 149)


# DISPLAY SURFACE ----------------------------------------------------------------
# this is where the game is visible
# pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Tic-Tac-Toe')  # title of the window


# DRAWING FUNCTIONS -------------------------------------------------------------
def draw_grid():
    # draw vertical lines
    for x in range(1, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR,
                         (x * CELL_SIZE, 0),
                         (x * CELL_SIZE, WINDOW_SIZE),
                         LINE_WIDTH)

    # draw horizontal lines
    for y in range(1, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR,
                         (0, y * CELL_SIZE),
                         (WINDOW_SIZE, y * CELL_SIZE),
                         LINE_WIDTH)

# GAME LOOP ---------------------------------------------------------------------
# an endless loop that handles events; updates state of game; updates display surface
run = True
while run:
    # event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # fill the screen with background color
    screen.fill(BACKGROUND_COLOR)

    # draw the grid
    draw_grid()

    # update the display surface
    pygame.display.flip()

pygame.quit()

