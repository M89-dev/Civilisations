import pygame
from Card import Card_Manager

card_list = []

class Bot():
    def __init__(self):
        super().__init__()
        self.group_card_bot = pygame.sprite.Group()
        self.index_bar = 0
        self.screen = pygame.display.get_window_size()

    def verify_color(self):
        for card in card_list:
            card.regain_color()

    def add_card(self, pos_x, pos_y):
        card = Card_Manager(pos_x, pos_y)
        card_list.append(card)

        self.group_card_bot.add(card)