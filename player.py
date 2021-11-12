import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint):
        super().__init__()
        run_1 = pygame.image.load('graphic/character/run/1.png').convert_alpha()
        run_2 = pygame.image.load('graphic/character/run/2.png').convert_alpha()
        run_3 = pygame.image.load('graphic/character/run/3.png').convert_alpha()
        run_4 = pygame.image.load('graphic/character/run/4.png').convert_alpha()
        run_5 = pygame.image.load('graphic/character/run/5.png').convert_alpha()
        run_6 = pygame.image.load('graphic/character/run/6.png').convert_alpha()
        run_7 = pygame.image.load('graphic/character/run/7.png').convert_alpha()
        run_8 = pygame.image.load('graphic/character/run/8.png').convert_alpha()
        run_9 = pygame.image.load('graphic/character/run/9.png').convert_alpha()
        run_10 = pygame.image.load('graphic/character/run/10.png').convert_alpha()
        self.run = [run_1, run_2, run_3, run_4, run_5, run_6, run_7, run_8, run_9, run_10]
        self.frame_index = 0

        self.image = self.run[self.frame_index]
        self.doing = self.run
        self.rect = self.image.get_rect(midbottom=pos)

        # player status
        self.facing_right = True

        # player movement
        self.max_constraint = constraint
        self.speed = 3

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.speed = 3
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.speed = -3
            self.facing_right = False

    def hit_wall(self):
        if self.rect.left == 0:
            self.facing_right = True
            self.speed = 3
        if self.rect.right == self.max_constraint:
            self.facing_right = False
            self.speed = -3

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.x = 0
        if self.rect.right >= self.max_constraint:
            self.rect.right = self.max_constraint

    def running(self):
        self.rect.x += self.speed
        self.frame_index += 0.1
        if self.frame_index >= len(self.doing):
            self.frame_index = 0
        if self.facing_right:
            self.image = self.doing[int(self.frame_index)]
        if not self.facing_right:
            self.image = pygame.transform.flip((self.doing[int(self.frame_index)]), True, False)

    def update(self):
        self.get_input()
        self.constraint()
        self.hit_wall()
        self.running()