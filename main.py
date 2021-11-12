import pygame,sys
from random import randint
from player import Player
from rain import Rain
from heart import Heart
from coin import Coin
from chick import Chick

class Game():
    def __init__(self):
        # backgrounnd
        self.bg_image = pygame.image.load('graphic/bg.png').convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (screen_width, screen_height))

        # player
        player_sprite = Player((screen_width/2, screen_height - 40), screen_width)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # rain
        rain_sprite = Rain((randint(20,screen_width-20),(-randint(100,300))))
        self.rain = pygame.sprite.Group(rain_sprite)
        self.rain_adding_time = 10

        # heart
        heart_sprite = Heart((randint(20,screen_width-20),(-randint(100,300))))
        self.heart = pygame.sprite.Group(heart_sprite)
        self.heart_adding_time = 1000

        # coin
        coin_sprite = Coin((randint(20,screen_width-20),(-randint(100,300))))
        self.coin = pygame.sprite.Group(coin_sprite)
        self.coin_adding_time = 100

        # life
        self.life = pygame.image.load('graphic/life.png').convert_alpha()
        self.player_live = 3
        self.life_pos = 20

        # score
        self.score = 0
        self.font1 = pygame.font.Font('graphic/font/Lucian Schoenschrift CAT.TTF', 50)
        self.font2 = pygame.font.Font('graphic/font/Lucian Schoenschrift CAT.TTF', 30)

        # audio
        music = pygame.mixer.Sound('audio/bg_music.wav')
        music.set_volume(0.2)
        music.play(loops=-1)
        self.coin_sound = pygame.mixer.Sound('audio/coin.wav')
        self.coin_sound.set_volume(1)
        self.heart_sound = pygame.mixer.Sound('audio/heart.wav')
        self.heart_sound.set_volume(0.5)
        self.hurt_sound = pygame.mixer.Sound('audio/hurt.wav')
        self.hurt_sound.set_volume(0.3)

    def adding_rain(self):
        self.rain_adding_time -= 1
        if self.rain_adding_time <= 0:
            self.rain.add(Rain((randint(10, screen_width - 10), -(randint(30, 100)))))
            self.rain_adding_time = (randint(20, 50))

    def adding_heart(self):
        self.heart_adding_time -= 1
        if self.heart_adding_time <= 0:
            self.heart.add(Heart((randint(10, screen_width - 10), -(randint(30, 100)))))
            self.heart_adding_time = (randint(300, 500))

    def adding_coin(self):
        self.coin_adding_time -= 1
        if self.coin_adding_time <= 0:
            self.coin.add(Coin((randint(10, screen_width - 10), -(randint(30, 100)))))
            self.coin_adding_time = (randint(40, 90))

    def collision(self):
        for each_rain in self.rain:
            if pygame.sprite.spritecollide(each_rain, self.player, False):
                each_rain.kill()
                self.player_live -= 1
                self.hurt_sound.play()

        for each_heart in self.heart:
            if pygame.sprite.spritecollide(each_heart, self.player, False):
                each_heart.kill()
                self.heart_sound.play()
                if self.player_live < 3:
                    self.player_live += 1

        for each_coin in self.coin:
            if pygame.sprite.spritecollide(each_coin, self.player, False):
                each_coin.kill()
                self.score += 10
                self.coin_sound.play()

    def display_lives(self):
        for each_life in range(self.player_live):
            x = self.life_pos + (each_life * (self.life.get_size()[0] + 10))
            screen.blit(self.life, (x, 15))

    def display_score(self):
        score_surf = self.font1.render(f'score: {self.score}', False, 'white')
        score_rect = score_surf.get_rect(midtop = (screen_width/2 ,5))
        screen.blit(score_surf, score_rect)

    def gameover(self):
        gameover_surf = self.font1.render('Game over', False, 'white')
        gameover_rect = gameover_surf.get_rect(center=(screen_width / 2, screen_height/2 - 30))
        screen.blit(gameover_surf, gameover_rect)

        press_quit_surf = self.font2.render('press "space" to quit the game', False, 'white')
        press_quit_rect = press_quit_surf.get_rect(center=(screen_width / 2, screen_height / 2 + 30))
        screen.blit(press_quit_surf, press_quit_rect)

    def check_life(self):
        if self.player_live <= 0:
            for each_rain in self.rain:
                each_rain.kill()
            for each_heart in self.heart:
                each_heart.kill()
            for each_coin in self.coin:
                each_coin.kill()
            for player in self.player:
                player.kill()
            self.gameover()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                pygame.quit()
                sys.exit()

    def run(self):
        self.player.update()
        self.rain.update()
        self.heart.update()
        self.coin.update()

        screen.blit(self.bg_image, (0, 0))
        self.player.draw(screen)
        self.rain.draw(screen)
        self.heart.draw(screen)
        self.coin.draw(screen)
        self.adding_rain()
        self.adding_heart()
        self.adding_coin()

        self.collision()
        self.display_lives()
        self.display_score()
        self.check_life()

class Background():
    def __init__(self):
        self.bg_image = pygame.image.load('graphic/bg.png').convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (screen_width, screen_height))
        chick_sprite = Chick((screen_width/2, screen_height - 40))
        self.chick = pygame.sprite.GroupSingle(chick_sprite)
        self.font1 = pygame.font.Font('graphic/font/Lucian Schoenschrift CAT.TTF', 70)
        self.font2 = pygame.font.Font('graphic/font/Lucian Schoenschrift CAT.TTF', 30)

    def game_name(self):
        game_name_surf = self.font1.render('Toxic Rain', False, 'white')
        game_name_rect = game_name_surf.get_rect(center=(screen_width / 2, screen_height/2 - 30))
        screen.blit(game_name_surf, game_name_rect)

    def my_name(self):
        my_name_surf = self.font2.render('press "space" to play', False, 'white')
        my_name_rect = my_name_surf.get_rect(center=(screen_width / 2, (screen_height / 2 )+ 25))
        screen.blit(my_name_surf, my_name_rect)

    def run(self):
        screen.blit(self.bg_image, (0,0))
        self.game_name()
        self.my_name()
        self.chick.update()
        self.chick.draw(screen)


if __name__ == '__main__':
    pygame.init()
    screen_width = 500
    screen_height = 350
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Toxic Rain")

    clock = pygame.time.Clock()
    game = Game()
    background = Background()
    game_active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

        if game_active == True:
            background.run()
            game.run()

        else:
            background.run()


        pygame.display.flip()
        clock.tick(60)