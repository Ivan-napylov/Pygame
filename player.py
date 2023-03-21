import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load('graphics/player.png').convert_alpha(), (64, 64))

        self.rect = self.image.get_rect(center = pos)
        self.speed = 5
        

    def move(self):
        dx = 0
        dy = 0
        
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

        self.direction = pygame.math.Vector2(dx, dy)
        if self.direction.length() > 0:  
            self.direction.normalize()

    def update(self):
        self.move()
        self.rect.center += self.direction * self.speed