
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
    
    def manager_link(self):
        link_list = str(self.lien).split("\\\\")
        new_link = ''

        for cell in range(len(link_list)):
            new_link += link_list[cell] + '\\'
            print(new_link)

cards1=cards("Cards\Xan\c-Xan.json")
cards1.manager_link()
print(cards1.open_cards())
print(cards1.open("Xan", 0, "class"))
print(cards1.open("Xan",0, "passif"))
print(cards1.open("Xan", 0, "civilisation"))
print(cards1.open("Xan", 0, "life"))
print(cards1.open("Xan", 0, "resources"))
print(cards1.open("Xan", 0, "powers"))
print(cards1.open("Xan", 0, "unique"))

