import os
os.system("cls")
import pygame
import time

class Node:
    def __init__(self, song_name, song_path):
        self.song_name = song_name
        self.song_path = song_path
        self.next = None

class CircularPlaylist:
    def __init__(self):
        self.head = None
        self.current_song = None
        pygame.mixer.init()  
    def add_song(self, song_name, song_path):
        new_node = Node(song_name, song_path)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        print(f"Song '{song_name}' added to the playlist.")

    def display_playlist(self):
        if not self.head:
            print("Playlist is empty!")
            return
        temp = self.head
        print("Your Playlist:")
        while True:
            print(temp.song_name, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("... (Circular)")

    def play_song(self, position):
        if not self.head:
            print("Playlist is empty!")
            return
        temp = self.head
        count = 1
        while count < position:
            temp = temp.next
            count += 1
        self.current_song = temp
        print(f"Playing song: {self.current_song.song_name}")
        self.play_current_song()

    def play_current_song(self):
        if self.current_song:
            pygame.mixer.music.load(self.current_song.song_path)  
            pygame.mixer.music.play()  
            print(f"Now playing: {self.current_song.song_name}")

    def next_song(self):
        if self.current_song is None:
            print("No song is currently playing!")
            return
        self.current_song = self.current_song.next
        print(f"Playing next song: {self.current_song.song_name}")
        self.play_current_song()

    def previous_song(self):
        print("Error: You are using a Circular Singly Linked List. You cannot go back!")

    def show_current_song(self):
        if self.current_song:
            print(f"Currently playing: {self.current_song.song_name}")
        else:
            print("No song is currently playing!")

    def stop_song(self):
        pygame.mixer.music.stop()
        print("Music stopped.")


playlist = CircularPlaylist()

while True:
        song_add = input("Do you want to add a song to the playlist? (yes/no): ").lower()
        if song_add == 'yes':
            song_name = input("Enter the name of the song: ")
            song_path = input("Enter the path of the song file (e.g., C:/music/song.mp3): ")
            playlist.add_song(song_name, song_path)
        elif song_add == 'no':
            break
        else:
            print("Invalid choice, please enter 'yes' or 'no'.")
    
if not playlist.head:
        print("No songs in the playlist. Exiting program.")
        exit()

playlist.display_playlist()

while True:
        print("\nMenu:")
        print("1. Play song by position")
        print("2. Next song")
        print("3. Previous song")
        print("4. Show current song")
        print("5. Display playlist")
        print("6. Stop current song")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            pos = int(input("Enter the position of the song (starting from 1): "))
            playlist.play_song(pos)
        
        elif choice == 2:
            playlist.next_song()
        
        elif choice == 3:
            playlist.previous_song()  
        
        elif choice == 4:
            playlist.show_current_song()
        
        elif choice == 5:
            playlist.display_playlist()
        
        elif choice == 6:
            playlist.stop_song()  
        
        elif choice == 7:
            playlist.stop_song()  
            print("Exiting the music player.")
            break
        
        else:
            print("Invalid choice! Please select again.")
