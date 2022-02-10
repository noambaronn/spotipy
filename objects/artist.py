class Artist:
    def __init__(self, id: str, name: str):
        self.id_of_artist = id
        self.name_of_artist = name
        self.albums_of_artist = []

    def __str__(self):
        st = "id is %s, name is %s " % (self.id_of_artist, self.name_of_artist)
        st += "the albums are: "
        for album in self.albums_of_artist:
            st += str(album)
            st += " , "
        return st
