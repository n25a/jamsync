from utils.print import print_color, Colors
from spotify import Spotify
from social import Social, Skype
from config import config

# TODO : Add readme

if __name__ == '__main__':
    if not any([config.skype.enabled]):
        print_color(
            'Please enable at least one service in your config file',
            Colors.FAIL,
        )
        exit(1)

    social_medias: [Social] = []

    if config.skype.enabled:
        social_medias.append(Skype())

    spotify = Spotify()

    for music in spotify.monitor_playing():
        for social in social_medias:
            social.update(music)
