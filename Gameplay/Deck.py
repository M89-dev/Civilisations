import pygame, os, json
from Card_Selector import Card_Selector

deck_list = []
main_dir = os.path.split(os.path.abspath(__file__))[0]
font_dir = main_dir + "\\" + "assets\\font"

class DeckCard(pygame.sprite.Sprite):
    def __init__(self, list_deck):
        super().__init__()
        self.screen = pygame.display.get_window_size()

        self.image = pygame.Surface([100, 300])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

        self.list_deck = list_deck
        self.deck_group = pygame.sprite.Group()

        self.right_deck = 0
        self.left_deck = 0
        
        self.rect.center = (self.screen[0] // 2, self.screen[1] // 2)

        self.double_click_duration = 500
        self.now_click = 0
        self.last_click = 0

        self.name_card = None
        self.position_list = 0
        self.all_card = None

        self.text_render = None

        self.json_dir = os.path.join(os.getcwd(), "cards")
        self.link_json = os.path.join(self.json_dir, "decks.json")

    def get_card(self, name_deck):
        with open(self.link_json) as json_file:
            data_file = json.load(json_file)

            return data_file[name_deck]

    def text_deck(self):
        font_link = os.path.join(font_dir, "PressStart2P-Regular.ttf")
        intro_text_font = pygame.font.Font(font_link, 10)
        self.text_render = intro_text_font.render(self.name_card, False, (255, 255, 255))

    def change_color(self):
        self.image.fill((0, 0, 255))

    def regain_color(self):
        self.image.fill((0, 0, 0))

    def click_deck(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.now_click = pygame.time.get_ticks()

            if self.now_click - self.last_click <= self.double_click_duration:
                self.all_card_deck()
            else:
                self.change_color()
    
            self.last_click = pygame.time.get_ticks()

    def pos_deck(self, number_card):
        deck = DeckCard(self.list_deck)
        deck.name_card = self.list_deck[self.position_list]
        deck.text_deck()

        if self.get_indice(number_card):
            deck.rect.right += self.right_deck
            self.right_deck += 150
        else:
            deck.rect.left += self.left_deck
            self.left_deck -= 150

        deck_list.append(deck)
        self.deck_group.add(deck)
        self.position_list += 1

    def get_indice(self, number):
        if number % 2 == 0:
            return True
        else:
            return False

    def add_card(self):
        if self.get_indice(len(self.list_deck)):
            self.right_deck = 80
            self.left_deck = -80

            for deck_number in range(len(self.list_deck)):
                self.pos_deck(deck_number)
        else:
            self.right_deck = 150
            self.left_deck = -150

            deck = DeckCard(self.list_deck)
            deck.name_card = self.list_deck[self.position_list]
            deck.text_deck()

            self.position_list += 1

            deck_list.append(deck)
            self.deck_group.add(deck)

            for deck_number in range(len(self.list_deck) - 1):
                self.pos_deck(deck_number)

    def recovery_color(self):
        for deck in deck_list:
            deck.regain_color()

    def all_card_deck(self):
        # Delete deck
        self.deck_group.empty()

        dict_card = self.get_card(self.name_card)
        all_card = dict_card[0]
        
        for card in all_card.values():
            card_of_deck = Card_Selector(0, 0)
            card_of_deck.add_card()

    def update(self):
        self.click_deck()