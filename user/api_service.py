import flask
from spotipy.objects.build_the_spotipy import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/getAllArtists/', methods=['GET'])
def get_all_artists():
    set_artists, set_albums = load_to_objects(list_of_tracks(const.SONGS_DIRECTORY_PATH))
    artists = {}
    artists["artists"] = set_artists
    return artists


@app.route('/getAllAlbumsOf/artist_id/', methods=['GET'])
def get_albums_by_id():
    albums = get_albums_by_artist_id('5EgEUxXi9uTYYN4cQwmLPy')
    albums_of_artist = {}
    albums_of_artist["albums"] = albums
    return albums_of_artist

if __name__ == "__main__":
     app.run(debug=True ,port=8080,use_reloader=False)
