import json
import spotipy.constants as const


class Song:
    def __init__(self, song_id: str, name: str, popularity: int):
        self.song_id = song_id
        self.name_of_song = name
        self.popularity = popularity

    def serialize(self, serializer):
        serializer.start_object(const.SONG, self.song_id)
        serializer.add_property(const.NAME, self.name)
        serializer.add_property(const.POPULARITY, self.popularity)

    def __str__(self):
        return "id is %s, name is %s, popularity is %s" % (self.song_id, self.name_of_song, self.popularity)


class SongSerializer:
    def serialize(self, song, format):
        serializer = self._get_serializer(format)
        return serializer(song)

    def _get_serializer(self, format):
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)

    def _serialize_to_json(self, song):
        if format == 'JSON':
            song_info = {
                'id': song.song_id,
                'name': song.name,
                'popularity': song.popularity
            }
            return json.dumps(song_info)
        else:
            raise ValueError(format)
