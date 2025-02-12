import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *

def main():

    # initialize game, clock and screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # create sprite groups and assign classes
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # create game objects and 
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    
    dt = 0

    # start game loop
    while True:

        # end loop if window is exited
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # render changes to game objects
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # set game to 60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
