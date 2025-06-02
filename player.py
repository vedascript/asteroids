import pygame;
from circleshape import CircleShape;
from constants import *;
from shot import Shot;

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS);
        self.rotation = 0;
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self,screen):
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),2);

    def rotate(self,delta_time):
        self.rotation += delta_time * PLAYER_TURN_SPEED;
    
    def move(self,delta_time):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time;

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1);

        if keys[pygame.K_d]:
            self.rotate(dt);

        if keys[pygame.K_w]:
            self.move(dt);

        if keys[pygame.K_s]:
            self.move(dt * -1);
    
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
       


 