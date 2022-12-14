import os
import json
import time

class cards():
    def __init__(self,lien):
        self.lien = lien 


def open_cards(self):
    with open(self.lien) as json_file:
        data = json.load(json_file)
        print(data)


cards1=cards()
open_cards(cards1)