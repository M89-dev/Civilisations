import pygame
from Card import Card_Manager, Cards, Pile, Trash

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

        self.health_bar = 500
        self.lenght_health = 500

        self.wood = 0
        self.stone = 0
        self.gold = 0

    def card_not_visible(self, screen):
        pile = Pile()
        screen.blit(pile.image, pile.rect)
        pile.text_card()

    def card_visible(self, screen):
        trash = Trash()
        screen.blit(trash.image, trash.rect)

    def get_card(self):
        card_class = Card_Manager(100, 100)
        value_card = card_class.random_cards()
        card_info = Cards(value_card)

        return value_card

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

    def health_bar_assest(self, screen):
        rect_bar = pygame.Rect(0, 0, 500, 20)
        rect_bar.right = self.screen[0] - 20
        rect_bar.bottom = self.screen[1] - 30
        color_bar = (255, 0, 0)
        pygame.draw.rect(screen, color_bar, rect_bar)

    def evolution_bar_assest(self, screen):
        # text_font = pygame.font.Font(None, 50)
        # text_render = text_font.render(f"{self.name_civilisation}", False, "white")
        # screen.blit(text_render, (20, 20))

        rect_bar = pygame.Rect(20, 0, 500, 20)
        rect_bar.bottom = self.screen[1] - 30
        color_bar = (255, 0, 0)
        pygame.draw.rect(screen, color_bar, rect_bar)

        rect_evolution = pygame.Rect(20, 0, self.evolution_bar, 20)
        rect_evolution.bottom = self.screen[1] - 30
        color_evolution = (0, 255, 0)
        pygame.draw.rect(screen, color_evolution, rect_evolution)

    def update(self):
        pass