from utils.print import print_color, Colors
from spotify import Spotify
from skype import Skype
from config import config

# TODO : Add readme

if __name__ == '__main__':
    if not any([config.skype.enabled]):
        print_color(
            "Please enable at least one service in your config file",
            Colors.FAIL
        )
        exit(1)

    if config.skype.enabled:
        _skype = Skype()
        spotify = Spotify(skype_client=_skype)
        spotify.monitor_playing()
