import os
import configparser
from typing import Union


class Config:

    class Skype:
        def __init__(self, enabled: bool, username: str, password: str):
            """
            the initializer method for Skype config

            :param enabled: update the status of the user or not
            :param username: the username of the Skype account
            :param password: the password of the Skype account
            """
            self.enabled = enabled
            self.username = username
            self.password = password

    class Spotify:
        def __init__(self, client_id: str, client_secret: str):
            """
            the initializer method for Spotify config

            :param client_id: the client id of the Spotify app
            :param client_secret: the client secret of the Spotify app
            """
            self.client_id = client_id
            self.client_secret = client_secret

    def __init__(self, config_path):
        """
        the initializer method for the Config class

        :param config_path: the path to the config file
        """
        if config_path == "":
            raise ValueError("Config path cannot be empty")
        __config = configparser.ConfigParser()
        __config.read(config_path)

        self.skype = self.Skype(
            enabled=bool(__config['skype']['enabled'] or 0),
            username=__config['skype']['username'] or "",
            password=__config['skype']['password'] or "",
        )

        self.spotify = self.Spotify(
            client_id=__config['spotify']['client_id'] or "",
            client_secret=__config['spotify']['client_secret'] or "",
        )


config: Union[Config] = Config(os.environ['CONFIG_PATH'])
