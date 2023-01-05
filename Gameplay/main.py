import pygame, os, sys
from Music import Music_Manager
from Player import Player
from Bot import Bot
from Deck import DeckCard

# Pygame initial command (True)
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Civilisations")

main_dir = os.path.split(os.path.abspath(__file__))[0]
image_dir = main_dir + "\\" + "assets\\image"
music_dir = main_dir + "\\" + "assets\\music"
font_dir = main_dir + "\\" + "assets\\font"

card_deck = ["card1", "card2", "card3", "card4", "card5"]

# Check import of initial package pygame (True)
if not pygame.mixer:
    print("Missin Music module")
elif not pygame.font:
    print("Missing Font module")

# Class Game display pygame
class Game():
    def __init__(self):
        self.screen_widht = 1500
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_widht, self.screen_height))
        self.game_set = "deck_assets"

        # Initilization of bot and player
        self.player = Player()
        self.bot = Bot()
        self.deck = DeckCard(card_deck)

        # Generate the principle card of game
        self.game_card()

        # Generate the game assets
        self.intro_assets()
        self.deck_assets()
        self.game_assets()

        # Playist music
        # self.playist_bg = Music_Manager()
        # self.playist_bg.play_playist("Playist_bg", 0.2)

    # Function create the card for Player and Bot
    def game_card(self):
        for number_card in range(3):
            self.player.add_card(120 * number_card, 0)
            self.bot.add_card(120 * number_card, 600)     

    # Function create the principle game assets
    def game_assets(self):
        link_board = os.path.join(image_dir, "test.jpg")
        self.imgae_board = pygame.image.load(link_board)
        self.imgae_board = pygame.transform.scale(self.imgae_board, (1500, 800))

    # Function create the principle intro assets
    def intro_assets(self):
        link_bg = os.path.join(image_dir, "bg_image.jpg")
        self.imgae_bg = pygame.image.load(link_bg)
        self.imgae_bg = pygame.transform.scale(self.imgae_bg, (1510, 790))

        link_button = os.path.join(image_dir, "button_play.png")
        self.button_play = pygame.image.load(link_button)
        self.button_play = pygame.transform.scale(self.button_play, (600, 100))
        self.button_play_rect = self.button_play.get_rect(center = (1500/2, 800/2 + 50))

        font_link = os.path.join(font_dir, "PressStart2P-Regular.ttf")
        intro_text_font = pygame.font.Font(font_link, 80)
        self.text_render = intro_text_font.render("Civilisations", False, (255, 255, 255))

    def deck_assets(self):
        link_board = os.path.join(image_dir, "test.jpg")
        self.imgae_board = pygame.image.load(link_board)
        self.imgae_board = pygame.transform.scale(self.imgae_board, (1500, 800))

        self.deck.add_card()

    def game_deck(self):
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.imgae_board, (0, 0))
            self.deck.deck_group.draw(self.screen)

            pygame.display.update()
            clock.tick(60)
                
    # Function create the game Menu
    def game_menu(self):
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

            self.screen.blit(self.imgae_bg, (0, 0))

            self.screen.blit(self.button_play, self.button_play_rect)
            self.screen.blit(self.text_render, (self.screen_widht/2 - 500, 50))
        
            pygame.display.update()
            clock.tick(60)

    # Function create the game Playning
    def game_playing(self):
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if events.type == pygame.MOUSEBUTTONDOWN:
                    self.player.recovery_color()
                    self.player.group_card_player.update()

            self.screen.blit(self.imgae_board, (0, 0))

            self.player.group_card_player.draw(self.screen)
            self.bot.group_card_bot.draw(self.screen)

            self.player.evolution_bar_assest(self.screen)
            self.player.health_bar_assest(self.screen)

            self.player.card_not_visible(self.screen)
            self.player.card_visible(self.screen)

            pygame.display.update()
            clock.tick(60)

    def manager_game(self):
        if self.game_set == "game_playing":
            self.game_playing()
        elif self.game_set == "deck_assets":
            self.game_deck()
        else:
            self.game_menu()

if __name__ == "__main__":
    game_civilisation = Game()
    game_civilisation.manager_game()