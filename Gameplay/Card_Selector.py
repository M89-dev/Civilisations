import pygame

class Card_Selector(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.screen = pygame.display.get_window_size()

        self.image = pygame.Surface([100, 300])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

        self.card_group = pygame.sprite.Group()

        self.rect.center = (pos_x, pos_y)

        self.name_card = None

    def add_card(self):
        card = Card_Selector(0, 0)
        self.card_group.add(card)