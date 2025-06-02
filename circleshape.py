import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self):  
        pass

    def update(self, dt):
        pass

    def is_not_colliding(self,target):
      total_distance =  pygame.math.Vector2.distance_to(self.position,target.position);
      return  total_distance > (self.radius + target.radius); 