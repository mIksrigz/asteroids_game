import pygame
from constants import *

def main():
    pygame.init()
    # print(pygame.get_init())
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # print(screen)
    # pygame.display.get_surface()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.quit()
    # print(pygame.get_init())

if __name__ == "__main__":
    main()
