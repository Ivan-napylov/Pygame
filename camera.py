import pygame
from player import Player
class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.disp = pygame.display.get_surface()
        self.bg = pygame.image.load('graphics/bg.png').convert_alpha()
        self.bg_rect = self.bg.get_rect(topleft = (0, 0))
        self.width = 0
        self.height = 0

    def custom_draw(self):
        # Background
        self.disp.blit(self.bg, self.bg_rect)
        # Активные элементы
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            self.disp.blit(sprite.image, sprite.rect)
