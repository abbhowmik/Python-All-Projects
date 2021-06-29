import pygame
from pygame.locals import *
# import time
# pygame.init()
if __name__ == '__main__':

    pygame.display.set_mode((1000, 700))
    surface.fill((52, 235, 195))
    pygame.display.flip()
    time.sleep(4)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
            elif event.type == QUIT:
                running = False
