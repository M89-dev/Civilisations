import pygame, os, glob, asyncio

pygame.mixer.init()

class Music_Manager():
    def __init__(self):
        self.link_music = None
        self.infinite_music = None
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]

    def load_music(self, link_music, infinite = False):
        main_dir = self.main_dir + "\\" + "assets\\music"
        music_link = os.path.join(main_dir, link_music)

        self.infinite_music = infinite

        return pygame.mixer.Sound(music_link)

    async def load_playist(self, link_playist):
        main_dir = self.main_dir + "\\" + "assets\\music"
        music_link = os.path.join(main_dir, link_playist)

        list_music = glob.glob(glob.escape(music_link) + "/*.wav")

        for music in list_music:
            self.link_music = pygame.mixer.Sound(music)
            self.play_music()
            await asyncio.sleep(self.link_music.get_length())

    def play_music(self):
        if self.link_music:
            self.link_music.play()
        else:
            print("No music loaded")

    def set_volume(self, volume):
        self.link_music.set_volume(volume)
