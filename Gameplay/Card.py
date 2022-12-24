import pygame, random, json

class Card_Manager(pygame.sprite.Sprite):
    def  __init__(self, pos_x, pos_y):
        super().__init__()
        self.screen = pygame.display.get_window_size()
        self.image = pygame.Surface([100, 200])
        self.image.fill((0, 0, 0))
        self.belong_card = None

        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen[1] - pos_y

        self.rect.x = pos_x + self.screen[0] / 2 - 150

    def change_color(self):
        self.image.fill((0, 0, 255))

    def regain_color(self):
        self.image.fill((0, 0, 0))

    def click_card(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.change_color()

    def update(self):
        self.click_card()

class Cards():
    def __init__(self,json_link):
        self.lien = json_link

    def manager_link(self):
        link_list = str(self.lien).split("\\\\")
        new_link = ''

        for cell in range(len(link_list)):
            new_link += link_list[cell] + '\\'
            print(new_link)

    def open(self, cards, age, type):
        with open(self.lien) as json_file:
            data = json.load(json_file)
            if type(data[cards][age][type]) == dict or list:
                for element in data[cards][age][type]:
                    print(element)
            else:
                return data[cards][age][type]

    def open_cards(self, cards):
        with open(self.lien) as json_file:
            data = json.load(json_file)
            for i in data[cards]:
                print(i)

    def open_class(self, cards, age):
        self.open(cards, age, "class")


    def open_passif(self, cards, age):
        self.open(cards,age,"passif")


    def open_civilisation(self,cards, age):
        self.open(cards,age,"civilisation")


    def open_life(self,cards, age):
        self.open(cards,age,"life")


    def open_resources(self,cards, age):
        self.open(cards,age,"resources")


    def open_powers(self,cards, age):
        self.open(cards,age,"powers")


    def open_unique(self,cards, age):
        self.open(cards,age,"unique")