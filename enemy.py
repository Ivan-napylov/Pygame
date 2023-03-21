import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.transform.scale(pygame.image.load('graphics/enemy.png').convert_alpha(), (64, 64))

        self.rect = self.image.get_rect(center = pos)
        self.speed = 5


    # def move(self, target):
