import pygame;
import random;
from circleshape import CircleShape;
from constants import ASTEROID_MIN_RADIUS;

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius);

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2);

    def update(self,delta_time):
        self.position += (self.velocity * delta_time); 
        
    def split(self):            
        random_angle = random.uniform(20,50);
        velocity_a = self.velocity.rotate(random_angle);
        velocity_b = self.velocity.rotate(-random_angle); 

        smaller_radius = self.radius - ASTEROID_MIN_RADIUS;

        asteroid_a = Asteroid(self.position.x,self.position.y,smaller_radius);
        asteroid_b = Asteroid(self.position.x,self.position.y,smaller_radius);
        
        asteroid_a.velocity = velocity_a * 1.2;
        asteroid_b.velocity = velocity_b * 1.2;



