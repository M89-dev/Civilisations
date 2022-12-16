
import json


class cards():
    def __init__(self,json_link):
        self.lien = json_link


    def open(self, cards, age, type):
        with open(self.lien) as json_file:
            data = json.load(json_file)
            print(data[cards][age][type])


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


cards1=cards("")
cards1.open_cards("Xan")
cards1.open_class("Xan",0)
cards1.open_passif("Xan",0)
cards1.open_civilisation("Xan",0)
cards1.open_life("Xan",0)
cards1.open_resources("Xan",0)
cards1.open_powers("Xan",0)
cards1.open_unique("Xan",0)
