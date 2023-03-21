# Импорт библиотек
from player import Player
from camera import Camera
from tree import Tree
import pygame
import random

# Сама игра
class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game")

        # Установим расширение экрана и частоту обновления
        self.visota = 720
        self.shirina = 1280
        self.FPS = 60

        # создание игры и окна
        self.screen = pygame.display.set_mode((self.shirina, self.visota))
        self.clock = pygame.time.Clock()


        # Камера
        self.camera_group = Camera()
        # Игрок
        self.player = Player((self.shirina / 2 - 32, self.visota / 2 - 32), self.camera_group)

        # Окружение        
        for i in range(20):
            random_x = random.randint(0, 1000)
            random_y = random.randint(0, 1000)
            Tree((random_x, random_y), self.camera_group)


    def run(self):
        running = True
        while running:


            # Ввод процесса (события)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            
            # Рендеринг
            self.screen.fill((50, 0, 0))

            # Камера
            self.camera_group.update()
            self.camera_group.custom_draw()

            pygame.display.update()

            self.clock.tick(self.FPS)

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()