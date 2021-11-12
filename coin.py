import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        coin_1 = pygame.image.load('graphic/coins/1.png').convert_alpha()
        coin_2 = pygame.image.load('graphic/coins/2.png').convert_alpha()
        self.coin = [coin_1, coin_2]
        self.frame_index = 0

        self.image = self.coin[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        self.coin_speed = 3

    def coin_moving(self):
        self.rect.y += self.coin_speed
        self.frame_index += 0.05
        if self.frame_index >= len(self.coin):
            self.frame_index = 0
        self.image = self.coin[int(self.frame_index)]

    def coin_kill(self):
        if self.rect.y >= 350:
            self.kill()

    def update(self):
        self.coin_moving()
        self.coin_kill()