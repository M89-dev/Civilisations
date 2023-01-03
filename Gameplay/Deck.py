import pygame

class DeckCard(pygame.sprite.Sprite):
    def __init__(self, card_name):
        super().__init__()
        self.number_deck = card_name
        self.image = pygame.Surface([100, 300])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

