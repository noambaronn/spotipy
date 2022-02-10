import os
import sys
from spotipy.objects.build_the_spotipy import *
from spotipy.user.user import User


def register():
    spotify_client_key = input("Put your username : ")
    is_premium = int(input("Would you like to have a premium user? "))
    if is_premium == 1:
        const.IS_PREMIUM = True
    elif is_premium == 0:
        const.IS_PREMIUM = False
    else:
        print("1 = True, 0 =False" + "\n" + "Try Again")
        menu()
    is_artist = int(input("Are you an artist? "))
    if is_artist == 1:
        const.IS_ARTIST_USER = True
    elif is_artist == 0:
        const.IS_ARTIST_USER = False
    else:
        print("1 = True, 0 =False" + "\n" + "Try Again")
        menu()
    user = User(spotify_client_key, is_premium, is_artist)
    print("Hello " + spotify_client_key)

#TODO
def login():
    pass


def menu():
    print("************Welcome to Spotipy**************")
    print()
    option = input("""
                              A: Please Register 
                              B: Login
                              C: Logout

                              Please enter your choice: """)
    if option == "A" or option == "a":
        register()
    elif option == "B" or option == "b":
        login()
    elif option == "C" or option == "c":
        sys.exit
    else:
        print("You must only select either A, B or C")
        print("Please try again")
        menu()

    choice = input("""
    
                      A: Get all artists
                      B: Get all the albums of an artist
                      C: Get the most popular songs of an artist
                      D: Get all songs in Album
                      E: Exit
                    
                      Please enter your choice: """)

    if choice == "A" or choice == "a":
        set_artists, aet_albums = load_to_objects(list_of_tracks(const.SONGS_DIRECTORY_FOR_MENU))
        for artist in set_artists:
            print(artist.__str__())
            print("")
        menu()
    elif choice == "B" or choice == "b":
        artist_id = input("Put the artist id: ")
        albums = get_albums_by_artist_id(artist_id)
        for album in albums:
            print(album.__str__())
            print("")
        menu()
    elif choice == "C" or choice == "c":
        id = input("Put the artist id: ")
        popular_songs = get_the_best_songs_by_popularity(id, const.IS_PREMIUM)
        for song in popular_songs:
            print(song.__str__())
            print("")
        menu()
    elif choice == "D" or choice == "d":
        album_id = input("Put the artist id: ")
        songs_in_album = get_songs_in_album(album_id)
        for song in songs_in_album:
            print(song.__str__())
            print("")
        os.system('clear')
        menu()
    elif choice == "E" or choice == "e":
        sys.exit()
    else:
        print("You must only select either A, B, C, D or E")
        print("Please try again")
        menu()


if __name__ == '__main__':
    menu()