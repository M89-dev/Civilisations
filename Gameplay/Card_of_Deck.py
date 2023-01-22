import pygame

class Card_of_Deck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_window_size()

        self.width = 50
        self.height = 100

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

        self.card_group = pygame.sprite.Group()

        self.name_card = None

        self.pos_x = (self.screen[0] // 2) - (self.width * 7)
        self.pos_y = 20 

    def add_card(self):

        for col in range(4):
            self.pos_y += 110

            for ligne in  range(10):
                new_card = Card_of_Deck()
                new_card.rect.center = (self.pos_x, self.pos_y)

                self.pos_x += 80

                self.card_group.add(new_card)

                if ligne >= 9:
                    self.pos_x = (self.screen[0] // 2) - (self.width * 7)

