from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> any:
        pass

class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass

class Playlist(IterableCollection):
    def __init__(self):
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def create_iterator(self) -> Iterator:
        return PlaylistIterator(self)


class PlaylistIterator(Iterator):
    def __init__(self, playlist: Playlist):
        self.playlist = playlist
        self.index = 0

    def has_next(self) -> bool:
        return self.index < len(self.playlist.songs)

    def next(self) -> any:
        if self.has_next():
            song = self.playlist.songs[self.index]
            self.index += 1
            return song
        return None