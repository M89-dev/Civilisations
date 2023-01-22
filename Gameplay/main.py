import pygame, os, sys
from Music import Music_Manager
from Player import Player
from Bot import Bot
from Deck import DeckCard, deck_list
from Card_of_Deck import Card_of_Deck

# Pygame initial command (True)
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Civilisations")

main_dir = os.path.split(os.path.abspath(__file__))[0]
image_dir = main_dir + "\\" + "assets\\image"
music_dir = main_dir + "\\" + "assets\\music"
font_dir = main_dir + "\\" + "assets\\font"

card_deck = ["deck_2", "deck_1", "deck_3"]

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
        self.game_set = "_deck"

        # Initilization of bot and player
        self.player = Player()
        self.bot = Bot()
        self.deck = DeckCard(card_deck)

        self.card_of_deck = Card_of_Deck()
        self.card_of_deck.add_card()

        # Generate the principle card of game
        self.game_card()

        # Generate the game assets
        self.intro_assets()
        self.deck_assets()
        self.game_assets()

        # Playist music
        self.playist_bg = Music_Manager()
        self.playist_bg.play_playist("Playist_bg", 0.2)

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

        link_button_start = os.path.join(image_dir, "button_display.png")
        link_button_return = os.path.join(image_dir, "button_display.png")

        self.button_start = pygame.image.load(link_button_start)
        self.button_return = pygame.image.load(link_button_return)

        self.button_start_rect = self.button_start.get_rect()
        self.button_return_rect = self.button_return.get_rect()

        self.button_start_rect.topleft = (100, self.screen_height - 350)
        self.button_return_rect.topright = (self.screen_widht - 100, self.screen_height - 350)  

        self.deck.add_card()

    def deck_draw(self):
        for deck in deck_list:
            self.screen.blit(deck.text_render, (deck.rect.x + 20, deck.rect.y + 130))

    def game_deck(self):
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if events.type == pygame.MOUSEBUTTONDOWN:
                    self.deck.recovery_color()
                    self.deck.deck_group.update()

            self.screen.blit(self.imgae_board, (0, 0))
            self.deck.deck_group.draw(self.screen)

            self.deck_draw()

            pygame.display.update()
            clock.tick(60)

    def _deck(self):
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if events.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse = pygame.mouse.get_pos()

                    if self.button_start_rect.collidepoint(pos_mouse):
                        self.game_set = "game_playing"
                        self.manager_game()
                    
                    elif self.button_return_rect.collidepoint(pos_mouse):
                        self.game_set = "game_deck"
                        self.manager_game()

            self.screen.blit(self.imgae_board, (0, 0))
            self.card_of_deck.card_group.draw(self.screen)

            self.screen.blit(self.button_start, self.button_start_rect)
            self.screen.blit(self.button_return, self.button_return_rect)

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
                        self.game_set = "game_deck"
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
        elif self.game_set == "game_deck":
            self.game_deck()
        elif self.game_set == "_deck":
            self._deck()
        else:
            self.game_menu()

if __name__ == "__main__":
    game_civilisation = Game()
    game_civilisation.manager_game()