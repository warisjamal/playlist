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

# Tests
playlist = Playlist(3)
playlist.add_song("S1")
playlist.add_song("S2")
playlist.add_song("S3")
assert playlist.get_playlist() == ["S1", "S2", "S3"], "Song list not matched"
playlist.add_song("S4")
assert playlist.get_playlist() == ["S1", "S3", "S4"], "Song list not matched"
playlist.add_song("S2")
assert playlist.get_playlist() == ["S3", "S4", "S2"], "Song list not matched"
playlist.add_song("S1")
assert playlist.get_playlist() == ["S4", "S2", "S1"], "Song list not matched"
