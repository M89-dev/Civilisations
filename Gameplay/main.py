import pygame, os, sys
from Music import Music_Manager
from Player import Player
from Bot import Bot

pygame.init()
clock = pygame.time.Clock()
main_dir = os.path.split(os.path.abspath(__file__))[0] + "\\" + "assets\\image"

if not pygame.mixer:
    print("Missin Music module")
elif not pygame.font:
    print("Missing Font module")

class Game():
    def __init__(self):
        self.screen_widht = 1500
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_widht, self.screen_height))
        self.game_set = "intro"
        self.player = Player()
        self.bot = Bot()
        self.game_assets()

        # Background music
        self.music = Music_Manager()
        self.music.play_music("Audiomachine - By the Hand of the Mortal.wav", 0.1, False)

        # Playist music
        # self.music = Music_Manager()
        # self.music.play_playist("Playist1", 0.2)

    def game_assets(self):
        for i in range(3):
            self.player.add_card(120 * i, 0)

        for i in range(3):
            self.bot.add_card(120 * i, 300)

    def intro_assets(self):
        lien_bg = os.path.join(main_dir, "bg_image.jpg")
        self.imgae_bg = pygame.image.load(lien_bg)
        self.imgae_bg = pygame.transform.scale(self.imgae_bg, (1510, 790))

        lien_button = os.path.join(main_dir, "button_play.png")
        self.button_play = pygame.image.load(lien_button)
        self.button_play_rect = self.button_play.get_rect(center = (1500/2, 800/2 + 50))

        text_font = pygame.font.Font(None, 52)
        self.text_render = text_font.render("Civilisations", False, (255, 255, 255))

    def intro(self):
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse = pygame.mouse.get_pos()

                    if self.button_play_rect.collidepoint(pos_mouse):
                        self.game_set = "game_playing"
                        self.manager_game()

            self.intro_assets()

            self.screen.blit(self.imgae_bg, (0, 0))
            self.screen.blit(self.button_play, self.button_play_rect)
            self.screen.blit(self.text_render, (self.screen_widht/2 - 120, 50))
        
            pygame.display.update()
            clock.tick(60)

    def game_playing(self):
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if events.type == pygame.MOUSEBUTTONDOWN:
                    self.player.verify_color()
                    self.player.group_card_player.update()

            self.screen.fill((41, 25, 123))

            self.player.group_card_player.draw(self.screen)
            self.bot.group_card_bot.draw(self.screen)

            pygame.display.update()
            clock.tick(60)

    def manager_game(self):
        if self.game_set == "game_playing":
            self.game_playing()
        else:
            self.intro()

game_civilisation = Game()
game_civilisation.manager_game()