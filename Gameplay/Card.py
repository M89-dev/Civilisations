import pygame, random, json, os

class Card_Manager(pygame.sprite.Sprite):
    def  __init__(self, pos_x, pos_y):
        super().__init__()
        self.screen = pygame.display.get_window_size()
        self.image = pygame.Surface([100, 200])
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen[1] - pos_y
        self.rect.x = pos_x + self.screen[0] / 2 - 150

        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.json_dir = os.path.join(self.main_dir, "assets\\evolution")

        self.link_evolve_file = os.path.join(self.json_dir, "Civilisation_Evolve.json")
        self.link_card = os.path.join(self.json_dir, "cards.json")

    def change_color(self):
        self.image.fill((0, 0, 255))

    def regain_color(self):
        self.image.fill((0, 0, 0))

    def click_card(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.change_color()

    def random_cards(self):
     with open(self.link_card) as json_file:
            data_file = json.load(json_file)
            nb_type = random.choice(list(data_file.keys()))

            return(random.choice(list(data_file[nb_type][0].keys())))

    def update(self):
        self.click_card()

class Cards():
    def __init__(self, name_file):
        self.json_dir = os.path.join(os.getcwd(), "cards")
        self.name_card = name_file

        self.name_json = ""
        self.link_json = os.path.join(self.manager_link(name_file), self.name_json)

    def manager_link(self, name_file):
        self.name_json = f"c-{name_file}.json"
        return os.path.join(self.json_dir, name_file)

    def open(self, age_card, type):
        with open(self.link_json) as json_file:
            data_file = json.load(json_file)

            return data_file[self.name_card][age_card][type]

    def open_cards(self):
        with open(self.link_json) as json_file:
            data_file = json.load(json_file)

            return json.dumps(data_file, indent=4)

    def open_class(self, age_card):
        return self.open(age_card, "class")

    def open_passif(self, age_card):
        return self.open(age_card,"passif")

    def open_civilisation(self, age_card):
        return self.open(age_card,"civilisation")

    def open_life(self, age_card):
        return self.open(age_card,"life")

    def open_resources(self, age_card):
        return self.open(age_card,"resources")

    def open_powers(self, age_card):
        return self.open(age_card,"powers")

    def open_unique(self, age_card):
        return self.open(age_card,"unique")