import pygame

class Chick(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        idle_1 = pygame.image.load('graphic/character/idle/1.png').convert_alpha()
        idle_2 = pygame.image.load('graphic/character/idle/2.png').convert_alpha()
        idle_3 = pygame.image.load('graphic/character/idle/3.png').convert_alpha()
        idle_4 = pygame.image.load('graphic/character/idle/4.png').convert_alpha()
        idle_5 = pygame.image.load('graphic/character/idle/5.png').convert_alpha()
        idle_6 = pygame.image.load('graphic/character/idle/6.png').convert_alpha()
        self.idle = [idle_1, idle_2, idle_3, idle_4, idle_5, idle_6]
        self.frame_index = 0

        self.image = self.idle[self.frame_index]
        self.doing = self.idle
        self.rect = self.image.get_rect(midbottom=pos)

        # player status
        self.facing_right = True

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.kill()

    def running(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.doing):
            self.frame_index = 0
        if self.facing_right:
            self.image = self.doing[int(self.frame_index)]
        if not self.facing_right:
            self.image = pygame.transform.flip((self.doing[int(self.frame_index)]), True, False)


    def update(self):
        self.get_input()
        self.running()
