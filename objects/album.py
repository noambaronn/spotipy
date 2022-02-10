class Album:
    def __init__(self, id: str, name_of_album: str):
        self.id_of_album = id
        self.name_of_album = name_of_album
        self.songs = []

    def __str__(self):
        st = "id is %s, name is %s " % (self.id_of_album, self.name_of_album)
        st += " the songs in the albums are : "
        for song in self.songs:
            st += str(song)
            st += " , "
        return st
