
import json


class cards():
    def __init__(self,json_link):
        self.lien = json_link


    def open(self, cards, age, type:str):
        with open(self.lien) as json_file:
            data = json.load(json_file)
            return (data[cards][age][type])


    def open_cards(self):
        with open(self.lien) as json_file:
            data = json.load(json_file)
            return data



cards1=cards("C:\\Users\\lduma\\Documents\\GitHub\\Civilisations\\cards\\Xan\\c-Xan.json")
print(cards1.open_cards())
print(cards1.open("Xan", 0, "class"))
print(cards1.open("Xan",0, "passif"))
print(cards1.open("Xan", 0, "civilisation"))
print(cards1.open("Xan", 0, "life"))
print(cards1.open("Xan", 0, "resources"))
print(cards1.open("Xan", 0, "powers"))
print(cards1.open("Xan", 0, "unique"))

