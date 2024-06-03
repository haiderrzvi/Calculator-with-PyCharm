import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")

        self.current_track = ""
        self.paused = False

        self.initialize_player()
    
    def initialize_player(self):
        # Initialize Pygame mixer
        pygame.mixer.init()

        # Create buttons
        self.play_button = tk.Button(self.root, text="Play", command=self.play_pause)
        self.play_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.choose_button = tk.Button(self.root, text="Choose Track", command=self.choose_track)
        self.choose_button.pack()

    def choose_track(self):
        # Allow user to choose a music file
        self.current_track = filedialog.askopenfilename(filetypes=[("Music files", "*.mp3")])
        if self.current_track:
            pygame.mixer.music.load(self.current_track)

    def play_pause(self):
        if self.current_track:
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
                self.play_button.config(text="Pause")
            else:
                pygame.mixer.music.play()
                self.play_button.config(text="Pause")
    
    def stop(self):
        if self.current_track:
            pygame.mixer.music.stop()
            self.paused = False
            self.play_button.config(text="Play")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
