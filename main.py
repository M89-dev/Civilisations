import os
import json
import time

class GamePlay():
    def __init__(self, nombre_joueur, nombre_carte, nombre_tour):
        self.nombre_joueur = nombre_joueur
        self.nombre_carte = nombre_carte
        self.nombre_tour = nombre_tour
        self.progress_bar = 0
        
    def get_nombre_joueur(self):
        return self.nombre_joueur
    
    def get_nombre_carte(self):
        return self.nombre_carte
    
    def get_nombre_tour(self):
        return self.nombre_tour
    
    def Game_Main(self):
        print("La partie va se derouler en ->")
        print(f"Nombre de joueur {self.nombre_joueur}")
        print(f"Nombre de tour {self.nombre_tour}")
        
        while self.nombre_tour > 0:
            self.Percent_Bar(10)
            time.sleep(2)
            self.nombre_tour -= 1
            
    def Game_Rule(self):
        print("")
        
    def Percent_Bar(self , tour, bar_len=50, title='Please wait'):
        percent_done = (bar_len / tour) + self.progress_bar
        percent_done = round(percent_done, 1)
        
        percent_finish = bar_len - percent_done
        self.progress_bar += (bar_len / tour)
    
        done_str = '█'*int(percent_done)
        togo_str = '░'*int(percent_finish)

        print(f'\t⏳{title}: [{done_str}{togo_str}] {percent_done}% done', end='\r')
        
game = GamePlay(3, 2, 10)
game.Game_Main()

        
    
        