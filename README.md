Circular Playlist Music Player
This Python program implements a Circular Playlist Music Player using a Circular Singly Linked List data structure. It allows users to add songs, navigate through them, and control playback with options to play the next song, stop the music, and display the current song.

Features
Add Songs: Add songs to the playlist by providing the name and file path of the song.
Circular Playlist: The playlist loops back to the first song after the last one, making it circular.
Play Songs: You can play any song by specifying its position in the playlist.
Next Song: Skip to the next song in the playlist.
Show Current Song: Display the currently playing song.
Stop Music: Stop the currently playing song.
Display Playlist: View the entire playlist in circular order.
How It Works
Circular Linked List:
The playlist is implemented as a circular linked list, where each node represents a song.
The next pointer of the last node points to the first node, ensuring the circular nature.
Pygame Library:
The program uses pygame.mixer to load and play .mp3 files. Make sure to install the pygame library before running the program.
How to Use
Add Songs:
When prompted, enter yes to add a song.
Provide the song's name and the full file path (e.g., C:/music/song.mp3).
Menu Options:
After adding songs, you'll be presented with a menu:
Play a song by its position (starting from 1).
Play the next song in the playlist.
Note: You cannot play the previous song since the list is a circular singly linked list.
Show the currently playing song.
Display the entire playlist.
Stop the currently playing song.
Exit the music player.
Dependencies
Make sure to install the following before running the program:

pygame for music playback: Install it using the command:
Copy code
pip install pygame
Running the Program
Clone the repository or download the source code.
Install pygame using the command above.
Run the program:
bash
Copy code
python circular_playlist.py
Follow the prompts to add songs and control playback.
Limitations
The player only supports forward navigation (no previous song functionality) due to the use of a circular singly linked list.
Only .mp3 files are supported for playback.
