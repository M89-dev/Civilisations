
import json
import random 


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


    def name(self):
        with open(self.lien) as json_file:
            data = json.load(json_file)
            for l in data.keys():
                return l



def random_cards():
     with open("cards\\cards.json") as json_file:
            data = json.load(json_file)
            nb_type = random.choice(list(data.keys()))
            return(random.choice(list(data[nb_type][0].values())))


cards1=cards(random_cards())
print(cards1.open_cards())
print(cards1.open(cards1.name(), 0, "class"))
print(cards1.open(cards1.name(),0, "passif"))
print(cards1.open(cards1.name(), 0, "civilisation"))
print(cards1.open(cards1.name(), 0, "life"))
print(cards1.open(cards1.name(), 0, "resources"))
print(cards1.open(cards1.name(), 0, "unique"))
