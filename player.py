import pygame
from camera import Camera

class Player():
    def __init__(self, surface, color, len, x, y):
        self.surface = surface
        self.Pl_color = color
        self.len = len

        self.rect = pygame.Rect(x, y, self.len, self.len)
        

    def draw(self):
        pygame.draw.rect(self.surface, self.Pl_color, self.rect)
        

    def move(self):
        dx = 0
        dy = 0

        self.speed = 5

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and keys[pygame.K_s] == False:
            dy = -1
        if keys[pygame.K_s] and keys[pygame.K_w] == False:
            dy = 1
        if keys[pygame.K_a] and keys[pygame.K_d] == False:
            dx = -1
        if keys[pygame.K_d] and keys[pygame.K_a] == False:
            dx = 1
        if keys[pygame.K_w] and keys[pygame.K_s]:
            dy = 0
        if keys[pygame.K_a] and keys[pygame.K_d]:
            dx = 0
            


        direction = pygame.math.Vector2(dx, dy)


        if direction.length() > 0:  
            direction.normalize()

        direction *= self.speed

        self.rect.move_ip(direction.x, direction.y)