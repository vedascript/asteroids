from circleshape import CircleShape;
from constants import PLAYER_SHOOT_SPEED, SHOT_RADIUS;
import pygame;

class Shot(CircleShape):
    def __init__(self,x,y,):
        super().__init__(x,y,SHOT_RADIUS);
     
    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,SHOT_RADIUS,2);

    def update(self,delta_time):
        self.position += self.velocity * delta_time;