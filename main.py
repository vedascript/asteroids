import pygame;
from constants import * ;
from player import Player;
from asteroid import Asteroid;
from asteroidfield import AsteroidField;
from shot import Shot;

def main():
    print('Starting Asteroids!');
    print(f"Screen width: {SCREEN_WIDTH}");
    print(f"Screen height: {SCREEN_HEIGHT}");

    pygame.init();
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT));
    clock =  pygame.time.Clock();
    delta_time = 0;

    updatable_group = pygame.sprite.Group();
    drawable_group = pygame.sprite.Group();
    asteroids_group = pygame.sprite.Group();
    shot_group = pygame.sprite.Group();

    Player.containers = (updatable_group, drawable_group);
    Asteroid.containers = (asteroids_group,updatable_group,drawable_group);
    AsteroidField.containers = (updatable_group);
    Shot.containers = (updatable_group, drawable_group, shot_group);
    
    asteroidfield = AsteroidField();
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2);    

    # game loop
    while(1):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return;
    
        screen.fill((0,0,0));

        for drawable in drawable_group:
            drawable.draw(screen);
        
        for updatable in updatable_group:
            updatable.update(delta_time);

        for asteroid in asteroids_group:
            if(not (asteroid.is_not_colliding(player))):
                print('Game over!');
                return;
            
            for bullet in shot_group:
                if(not(asteroid.is_not_colliding(bullet))):
                    pygame.sprite.Sprite.kill(asteroid);
                    pygame.sprite.Sprite.kill(bullet);

        pygame.display.flip();
        delta_time = (clock.tick(60)/1000);
        
if __name__ == "__main__":
    main();