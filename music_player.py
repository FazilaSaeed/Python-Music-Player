import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.init()
        self.music_folder = music_folder
        self.music_files = []
        self.current_index = 0
        self.load_music_files()
        self.play_music()

    def load_music_files(self):
        # Load music files from the specified folder
        for file in os.listdir(self.music_folder):
            if file.endswith(".mp3"):
                self.music_files.append(os.path.join(self.music_folder, file))

    def play_music(self):
        # Initialize the mixer
        pygame.mixer.init()
        
        # Load the first music file
        pygame.mixer.music.load(self.music_files[self.current_index])

        # Start playing the music
        pygame.mixer.music.play()

        # Event loop to control music playback
        while pygame.mixer.music.get_busy():
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.stop()
                        self.next_song()

    def next_song(self):
        # Play the next song in the list
        self.current_index = (self.current_index + 1) % len(self.music_files)
        pygame.mixer.music.load(self.music_files[self.current_index])
        pygame.mixer.music.play()

if __name__ == "__main__":
    music_folder = "path/to/your/music/folder"
    player = MusicPlayer(music_folder)
