import time
import os
import logging
from typing import Optional

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from utils import Music
from skype import Skype
from config import config


class SpotifyLoginException(Exception):
    """
    all the exceptions related to the Spotify login
    """
    pass


class Spotify:

    def __init__(self, skype_client: Skype):
        """
        the initializer method for the Spotify class
        :param skype_client: the Skype client
        """
        url = "http://localhost:8080/callback"
        os.system(
            "export SPOTIPY_CLIENT_ID=" +
            config.spotify.client_id)
        os.system(
            "export SPOTIPY_CLIENT_SECRET=" +
            config.spotify.client_secret)
        os.system(
            "export SPOTIPY_REDIRECT_URI=" +
            url)

        scope = "user-library-read,user-read-currently-playing"
        oauth_manager = SpotifyOAuth(
            client_id=config.spotify.client_id,
            client_secret=config.spotify.client_secret,
            redirect_uri=url,
            scope=scope,
        )
        self.spotify_client = spotipy.Spotify(
            oauth_manager=oauth_manager,
            auth_manager=oauth_manager,
            client_credentials_manager=oauth_manager,
        )

        user = self.spotify_client.current_user()
        if user.get('display_name', "") == "":
            raise SpotifyLoginException(
                "Cannot get the username of the Spotify account"
            )
        self.skype_client = skype_client

    def __current_user_playing_track(self) -> Optional[Music]:
        """
        get the current playing track of the user
        :return: instance of Music class or None if there is no music playing
        """
        try:
            result = self.spotify_client.current_user_playing_track()
            music_name = result['item']['name']
            artists = ""

            for artist in result['item']['artists']:
                if artists == "":
                    artists += artist['name']
                else:
                    artists += "," + artist['name']

            link = result['item']['external_urls']['spotify'] or ""

            return Music(music_name, artists, link)
        except Exception as e:
            logging.error(e)
            return None

    def monitor_playing(self) -> None:
        """
        Monitor the current playing track of the user and
        update the bio of the user with the current playing track
        """
        last_music = None
        while True:
            music = self.__current_user_playing_track()
            if music is not None:
                if last_music is not None and \
                        music.spotify_link == last_music.spotify_link:
                    continue
                last_music = music
                self.skype_client.update_bio(music)
            time.sleep(8)
