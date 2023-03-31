class Music:
    def __init__(self, name: str, artists: str, spotify_link: str):
        """
        the initializer method for the Music class
        :param name: name of the music
        :param artists: artists of the music
        :param spotify_link: spotify link of the music
        """
        self.name = name
        self.artists = artists
        self.spotify_link = spotify_link
