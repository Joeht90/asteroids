# this allows us to use code from
# the open_source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    Shot.containers = (updatable, drawable, bullets)


    Player.containers = (updatable, drawable)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    player1 = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for obj in asteroids:
            if obj.collision(player1) == True:
                print("Game over!")
                pygame.quit()
            for bullet in bullets:
                if obj.collision(bullet) == True:
                    obj.split ()
                    bullet.kill()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        
        
if __name__ == "__main__":
    main()
    
