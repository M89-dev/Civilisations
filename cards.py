import os
import json
import time

class cards():
    def __init__(self,lien):
        self.lien = lien 


def open_cards(self):
    with open(self.lien) as json_file:
        data = json.load(json_file)
        for i in data[""]:
            print(i)

def open_class(self, age):
    with open(self.lien) as json_file:
        data = json.load(json_file)
        print(data[""][age]["class"])

def open_passif(self, age):
    with open(self.lien) as json_file:
        data = json.load(json_file)
        print(data[""][age]["passif"])

def open_civilisation(self, age):
    with open(self.lien) as json_file:
        data = json.load(json_file)
        print(data[""][age]["civilisation"])

def open_life(self, age):
    with open(self.lien) as json_file:
        data = json.load(json_file)
        print(data[""][age]["life"])

def open_resources(self, age):
    with open(self.lien) as json_file:
        data = json.load(json_file)
        print(data[""][age]["resources"])

def open_powers(self, age):
    with open(self.lien) as json_file:
        data = json.load(json_file)
        print(data[""][age]["powers"])

def open_unique(self, age):
    with open(self.lien) as json_file:
        data = json.load(json_file)
        print(data[""][age]["unique"])


cards1=cards("")
open_cards(cards1)
open_class(cards1,0)
open_passif(cards1,0)
open_civilisation(cards1,0)
open_life(cards1,0)
open_resources(cards1,0)
open_powers(cards1,0)
open_unique(cards1,0)