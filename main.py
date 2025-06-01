import pygame;
from constants import * ;
from player import Player;

def main():
    print('Starting Asteroids!');
    print(f"Screen width: {SCREEN_WIDTH}");
    print(f"Screen height: {SCREEN_HEIGHT}");

    pygame.init();
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT));
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2);

    clock =  pygame.time.Clock();
    delta_time = 0;


    # game loop
    while(1):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return;
    
        screen.fill((0,0,0));
        player.draw(screen);
        player.update(delta_time);
        pygame.display.flip();
        delta_time = (clock.tick(60)/1000);
        
if __name__ == "__main__":
    main();