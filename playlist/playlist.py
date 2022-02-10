from spotipy.exceptions import *


class Playlist:
    def __init__(self, name, is_premium=None):
        self.name = name
        if is_premium is None:
            self.is_premium = False
        else:
            self.is_premium = is_premium
        self.songs_ids = []

    def add_song(self, song_id: str):
        if self.is_premium == False:
            if len(self.songs_ids) < 20:
                self.songs_ids.append(song_id)
            else:
                raise BasicUserCanHaveOnly20Songs
