import pygame

class Heart(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        heart_1 = pygame.image.load('graphic/heart1.png').convert_alpha()
        heart_2 = pygame.image.load('graphic/heart2.png').convert_alpha()
        self.heart = [heart_1, heart_2]
        self.frame_index = 0

        self.image = self.heart[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        self.heart_speed = 3

    def heart_moving(self):
        self.rect.y += self.heart_speed
        self.frame_index += 0.05
        if self.frame_index >= len(self.heart):
            self.frame_index = 0
        self.image = self.heart[int(self.frame_index)]

    def heart_kill(self):
        if self.rect.y >= 350:
            self.kill()

    def update(self):
        self.heart_moving()
        self.heart_kill()