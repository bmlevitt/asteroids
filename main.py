import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run_game = True
    print("Starting asteroids!")

    while run_game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()

    # print (f"Screen width: {SCREEN_WIDTH}")
    # print (f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
