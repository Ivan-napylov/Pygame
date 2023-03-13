# Импорт библиотек
from player import Player
from camera import Camera
import pygame
import random

# Сама игра
class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game")

        # Установим расширение экрана и частоту обновления
        self.visota = 700
        self.shirina = 1000
        self.FPS = 60

        # создание игры и окна
        self.screen = pygame.display.set_mode((self.shirina, self.visota))
        self.clock = pygame.time.Clock()


        # Игрок
        self.player = Player(self.screen, 'red', 20,  self.shirina / 2 - 10, self.visota / 2 - 10)


    def run(self):
        running = True
        while running:


            # Ввод процесса (события)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            
            # Рендеринг
            self.screen.fill((0, 0, 0))

            # Игрок
            self.player.move()
            self.player.draw()

            pygame.display.update()

            self.clock.tick(self.FPS)

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()