# Design a musical jukebox using object-oriented principles.

class Song:

    def __init__(self, song_id, title, artist, duration):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist}"


class Album:

    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)


class Playlist:

    def __init__(self):
        self.queue = []
        self.current_index = 0

    def add_song(self, song):
        self.queue.append(song)

    def get_next_song(self):

        if self.current_index < len(self.queue):
            song = self.queue[self.current_index]
            self.current_index += 1
            return song

        return None


class Player:

    def play_song(self, song):
        print(f"Now playing: {song}")

class User:

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class Jukebox:

    def __init__(self, user):
        self.user = user
        self.playlist = Playlist()
        self.player = Player()
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def select_song(self, song):
        self.playlist.add_song(song)

    def play_next(self):

        song = self.playlist.get_next_song()

        if song:
            self.player.play_song(song)

        else:
            print("Playlist empty")


song1 = Song(1, "Shape of You", "Ed Sheeran", 4)
song2 = Song(2, "Believer", "Imagine Dragons", 3)

album = Album("Hits", "Various")
album.add_song(song1)
album.add_song(song2)

user = User(1, "Gary")

jukebox = Jukebox(user)

jukebox.add_album(album)

jukebox.select_song(song1)
jukebox.select_song(song2)

jukebox.play_next()
jukebox.play_next()