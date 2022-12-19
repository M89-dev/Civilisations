import pygame, os, sys
from Music import Music_Manager

pygame.init()
clock = pygame.time.Clock()

if not pygame.mixer:
    print("Missin Music module")
elif not pygame.font:
    print("Missing Font module")

class Game():
    def __init__(self):
        self.screen_widht = 1500
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_widht, self.screen_height))

        # Background music
        # self.music = Music_Manager("bg_music.wav")
        # self.music.play_music()
        # self.music.set_volume(0.2)

        self.music = Music_Manager()
        self.music.load_playist("Playist1")

    def run(self):

        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            pygame.display.update()
            clock.tick(60)

game_civilisation = Game()
game_civilisation.run()