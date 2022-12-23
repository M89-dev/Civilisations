import pygame
from Card import Card_Manager

card_list = []

class Player():
    def __init__(self):
        super().__init__()
        self.group_card_player = pygame.sprite.Group()
        self.index_bar = 0
        self.screen = pygame.display.get_window_size()

    def verify_color(self):
        for card in card_list:
            card.regain_color()

    def add_card(self, pos_x, pos_y):
        card = Card_Manager(pos_x, pos_y)
        card_list.append(card)

        self.group_card_player.add(card)

    def change_card(self):
        card_list[self.index_bar].regain_color()

        self.index_bar += 1

        if self.index_bar >= len(card_list):
            self.index_bar = 0

        card_list[self.index_bar].change_color()

    def get_card(self):
        pass

    def update_bar(self):
        pass

    def get_bar(self):
        pass

    def evolution_bar(self):
        pass

    def update(self):
        pass