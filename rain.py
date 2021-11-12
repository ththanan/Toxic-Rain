import pygame

class Rain(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        rain1 = pygame.image.load('graphic/rain1.png').convert_alpha()
        rain2 = pygame.image.load('graphic/rain2.png').convert_alpha()
        self.rain = [rain1, rain2]
        self.frame_index = 0

        self.image = self.rain[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        self.rain_speed = 3

    def raining(self):
        self.rect.y += self.rain_speed
        self.frame_index += 0.1
        if self.frame_index >= len(self.rain):
            self.frame_index = 0
        self.image = self.rain[int(self.frame_index)]

    def rain_kill(self):
        if self.rect.y >= 350:
            self.kill()

    def update(self):
        self.raining()
        self.rain_kill()