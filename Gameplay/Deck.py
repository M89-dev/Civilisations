import pygame, math

class DeckCard(pygame.sprite.Sprite):
    def __init__(self, list_deck):
        super().__init__()
        self.screen = pygame.display.get_window_size()

        self.image = pygame.Surface([100, 300])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

        self.list_deck = list_deck
        self.deck_group = pygame.sprite.Group()

        # self.middle_deck = self.get_middle()

        self.right_deck = 0
        self.left_deck = 0
        
        self.rect.center = (self.screen[0] // 2, self.screen[1] // 2)

    def change_color(self):
        self.image.fill((0, 0, 255))

    def regain_color(self):
        self.image.fill((0, 0, 0))

    def click_card(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.change_color()

    def pos_deck(self, number_card):
        deck = DeckCard(self.list_deck)
        
        if self.get_indice(number_card):
            deck.rect.right += self.right_deck
            self.right_deck += 150
        else:
            deck.rect.left += self.left_deck
            self.left_deck -= 150

        self.deck_group.add(deck)

    def get_indice(self, number):
        if number % 2 == 0:
            return True
        else:
            return False

    def add_card(self):
        if len(self.list_deck) % 2 == 0:
            self.right_deck = 80
            self.left_deck = -80

            for deck_number in range(len(self.list_deck)):
                self.pos_deck(deck_number)
        else:
            self.right_deck = 150
            self.left_deck = -150

            deck = DeckCard(self.list_deck)
            self.deck_group.add(deck)

            for deck_number in range(len(self.list_deck) - 1):
                self.pos_deck(deck_number)

    
    

