import pygame
from Card import Card_Manager, Cards

card_list = []

class Player():
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_window_size()
        self.group_card_player = pygame.sprite.Group()

        self.list_name = ["Stone Age", "Iron Age"]
        self.name_civilisation = self.list_name[0]

        self.evolution_bar = 0
        self.lenght_bar = 500

        self.wood = 0
        self.stone = 0
        self.gold = 0

        self.get_card()

    def get_card(self):
        card1 = Card_Manager(100, 100)
        value_card = card1.random_cards()

        card_info = Cards(value_card)

    def recovery_color(self):
        for card in card_list:
            card.regain_color()

    def add_card(self, pos_x, pos_y):
        card = Card_Manager(pos_x, pos_y)
        card_list.append(card)

        self.group_card_player.add(card)

    def update_bar(self):
        self.evolution_bar += 1

        if self.evolution_bar >= self.lenght_bar:
            self.list_name.pop(0)

            if len(self.list_name) < 0:
                print("Evoluition max")
            else:
                self.name_civilisation = self.list_name[0]
                self.evolution_bar = 0

    def evolution_bar(self, screen):
        text_font = pygame.font.Font(None, 50)
        text_render = text_font.render(f"{self.name_civilisation}", False, "white")
        screen.blit(text_render, (20, 20))

        rect_bar = pygame.Rect(0, 0, 500, 20)
        color_bar = (255, 0, 0)
        pygame.draw.rect(screen, color_bar, rect_bar, border_radius= 100)

        rect_evolution = pygame.Rect(10, 5, self.evolution_bar_, 10)
        color_evolution = (0, 255, 0)
        pygame.draw.rect(screen, color_evolution, rect_evolution, border_radius= 100)

    def update(self):
        pass