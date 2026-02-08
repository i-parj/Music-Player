import tkinter as tk
from tkinter import filedialog
import pygame
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Music Player")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Initialize Pygame Mixer
        pygame.mixer.init()

        # Variables
        self.playlist = []
        self.current_song = ""
        self.paused = False

        # --- GUI Setup ---
        
        # Title Label
        title_label = tk.Label(self.root, text="Music Player", font=("Helvetica", 20, "bold"), bg="darkgrey", fg="white")
        title_label.pack(fill=tk.X)

        # Playlist Listbox
        self.song_listbox = tk.Listbox(self.root, bg="black", fg="cyan", width=60, height=12, font=("Helvetica", 10))
        self.song_listbox.pack(pady=20)

        # Control Buttons Frame
        control_frame = tk.Frame(self.root)
        control_frame.pack()

        # Buttons
        play_btn = tk.Button(control_frame, text="Play", command=self.play_music, width=10, bg="green", fg="white")
        play_btn.grid(row=0, column=0, padx=10)

        pause_btn = tk.Button(control_frame, text="Pause", command=self.pause_music, width=10, bg="orange", fg="white")
        pause_btn.grid(row=0, column=1, padx=10)

        stop_btn = tk.Button(control_frame, text="Stop", command=self.stop_music, width=10, bg="red", fg="white")
        stop_btn.grid(row=0, column=2, padx=10)

        # Menu
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        add_song_menu = tk.Menu(menu)
        menu.add_cascade(label="Add Songs", menu=add_song_menu)
        add_song_menu.add_command(label="Add Folder", command=self.add_songs)

        # Volume Slider
        volume_frame = tk.LabelFrame(self.root, text="Volume")
        volume_frame.pack(pady=20)
        
        self.volume_slider = tk.Scale(volume_frame, from_=0, to=1, orient=tk.HORIZONTAL, resolution=0.1, command=self.set_volume, length=300)
        self.volume_slider.set(0.5)  # Set default volume to 50%
        self.volume_slider.pack()

    def add_songs(self):
        """Opens a directory selector and adds all MP3s to the playlist."""
        directory = filedialog.askdirectory()
        if directory:
            os.chdir(directory)
            songs = os.listdir(directory)
            
            for song in songs:
                if song.endswith(".mp3"):
                    self.playlist.append(song)
                    self.song_listbox.insert(tk.END, song)

    def play_music(self):
        """Plays the selected song or unpauses if paused."""
        try:
            # Check if paused, then unpause
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                # Play selected song
                selected_song_index = self.song_listbox.curselection()
                if selected_song_index:
                    selected_song = self.song_listbox.get(selected_song_index)
                    
                    # Only load if it's a new song
                    if selected_song != self.current_song:
                        self.current_song = selected_song
                        pygame.mixer.music.load(selected_song)
                        pygame.mixer.music.play()
                else:
                    print("No song selected.")
        except Exception as e:
            print(f"Error playing song: {e}")

    def pause_music(self):
        """Pauses the currently playing song."""
        pygame.mixer.music.pause()
        self.paused = True

    def stop_music(self):
        """Stops the music completely."""
        pygame.mixer.music.stop()
        self.paused = False
        # Reset selection (optional)
        # self.song_listbox.selection_clear(tk.ACTIVE)

    def set_volume(self, val):
        """Sets the volume of the mixer."""
        volume = float(val)
        pygame.mixer.music.set_volume(volume)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
