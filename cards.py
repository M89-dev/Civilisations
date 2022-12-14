import os
import json
import time

class cards():
    def __init__(self, classe="", passif=True, civilisation="", life=0, resources=0, powers=0, unique=True):
        self.classe = classe
        self.passif = passif
        self.civilisation= civilisation
        self.life = life
        self.resources = resources
        self.powers = powers
        self.unique = unique

def open_cards(self,lien):
    with open(lien) as json_file:
        data = json.load(json_file)
        self.classe = []
        self.passif = 
        self.civilisation= 
        self.life = 
        self.resources = 
        self.powers = 
        self.unique = 