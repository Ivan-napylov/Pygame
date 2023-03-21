import pygame
class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load('graphics/tree.png').convert_alpha(), (256, 256))
        self.rect = self.image.get_rect(topleft = pos)