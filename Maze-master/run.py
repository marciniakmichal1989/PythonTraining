import pygame
import random
import time
import math
from Grid import GridDrawer


def init():
    pygame.init()
    pygame.display.set_caption("Maze Creator")

    display = pygame.display.set_mode((800, 600))
    display.fill(pygame.Color("White"))
    pygame.display.update()

    return display


display = init()

def main():
    grid = GridDrawer(20, 8)
    init()
    is_running = True
    while is_running:
        grid.drow_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()


if __name__ == "__main__":
    main()