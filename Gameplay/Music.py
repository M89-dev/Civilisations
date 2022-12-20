import pygame, os, glob

pygame.mixer.init()

class Music_Manager():
    def __init__(self):
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]

    def play_playist(self, link_playist, volume_music):
        main_dir = self.main_dir + "\\" + "assets\\music"
        music_link = os.path.join(main_dir, link_playist)

        list_music = glob.glob(glob.escape(music_link) + "/*.wav")

        while len(list_music) > 0:
        
            pygame.mixer.music.load(list_music[0])
            pygame.mixer.music.set_volume(volume_music)
            pygame.mixer.music.play()
            list_music.pop(0)

            pygame.mixer.music.queue(list_music[0])
            list_music.pop(0)

    def play_music(self, link_music, volume_music, infinite_music = False):
        main_dir = self.main_dir + "\\" + "assets\\music"
        music_link = os.path.join(main_dir, link_music)

        pygame.mixer.music.load(music_link)
        pygame.mixer.music.set_volume(volume_music)

        if infinite_music:
            pygame.mixer.music.play(1)
        else:
            pygame.mixer.music.play(0)

    def set_volume(self, volume):
        self.link_music.set_volume(volume)
