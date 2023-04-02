class Playlist:
    def __init__(self, capacity):
        self.capacity = capacity
        self.songs = []

    def add_song(self, song):
        if len(self.songs) == self.capacity:
            self.songs.pop(0)
        self.songs.append(song)

    def get_playlist(self):
        return self.songs

# Take user input and test
capacity = 3
playlist = Playlist(capacity)
for i in range(5):
    song = input(f"Enter song {i+1}: ")
    playlist.add_song(song)
    print(f"Current playlist: {playlist.get_playlist()}")
