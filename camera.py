import pygame
from player import Player
class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.disp = pygame.display.get_surface()

        # Вектор камеры
        self.offset = pygame.math.Vector2()
        self.half_w = self.disp.get_size()[0] // 2
        self.half_h = self.disp.get_size()[1] // 2

        self.bg = pygame.transform.scale(pygame.image.load('graphics/bg.png').convert_alpha(), (320, 320))
        self.bg_rect = self.bg.get_rect(topleft = (0, 0))

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

        print(self.offset.x, self.offset.y)

    def custom_draw(self, player):

        self.center_target_camera(player)

        # Background
        bg_offset = self.bg_rect.topleft - self.offset
        self.disp.blit(self.bg, bg_offset)
        # for x in range(-self.bg.get_width(), self.disp.get_size()[0], self.bg.get_width()):
        #     for y in range(-self.bg.get_height(), self.disp.get_size()[1], self.bg.get_height()):
        #         self.disp.blit(self.bg, (bg_offset.x + x, bg_offset.y + y))


        # Активные элементы
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.disp.blit(sprite.image, offset_pos)
