import os
import json
import time

class cards():
    def __init__(self, classe=None, passif=True, civilisation=None, life=None, resources=None, powers=None, unique=True):
        self.classe = classe
        self.passif = passif
        self.civilisation= civilisation
        self.life = life
        self.resources = resources
        self.powers = powers
        self.unique = unique
        