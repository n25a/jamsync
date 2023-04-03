import logging

import skpy
from retry import retry

from utils import print_color, line, Music, Colors
from config import config

from .social import Social


class SkypeLoginException(skpy.SkypeAuthException, skpy.SkypeApiException):
    """
    all the exceptions related to the login process of the Skype account
    """
    ...


class Skype(Social):
    _emoji_index = 0
    emojis = [
        "(soccerball)", "(goldmedal)", "(lacrosse)", "(1f3b0_slotmachine)",
        "(eightball)", "(1f579_joystick)", "(1f3a3_fishingpoleandfish)",
        "(1f9e9_jigsaw)", "(hug)", "(games)", "(bowlingball)",
        "(1f3b2_gamedie)", "(1f399_studiomicrophone)"
    ]

    def __init__(self):
        """
        the initializer method for the Skype class
        """
        self.sk = skpy.Skype()
        self.__login()

    @retry(SkypeLoginException, tries=3, delay=0.5)
    def __login(self) -> None:
        """
        Login to the Skype account
        """
        try:
            self.sk.conn.soapLogin(
                config.skype.username,
                config.skype.password,
            )
            if self.sk.conn.userId is None:
                raise SkypeLoginException("Login failed.")
            print_color(
                line,
                Colors.OKCYAN,
            )
            print_color("You are now logged in as:",
                        [
                            Colors.HEADER,
                            Colors.BOLD,
                            Colors.UNDERLINE,
                            Colors.WARNING
                        ]
                        )
            print_color(self.sk.user, Colors.WARNING)
            print_color(
                line,
                Colors.OKCYAN,
            )
        except SkypeLoginException as e:
            logging.error(e)
            raise SkypeLoginException("Login failed.")

    def _update_bio(self, music: Music) -> None:
        """
        update the bio of the current user with the current music playing
        on Spotify in the following format:
        <emoji> <song name> - <artist name> - <spotify link>
        :param music: the object containing the music information
        """
        try:
            self._emoji_index = (self._emoji_index + 1) % len(self.emojis)
            self.__set_mood(self.emojis[self._emoji_index], music)
            print_color(
                line,
                Colors.OKBLUE,
            )
            print_color("Bio updated successfully. New Bio:", Colors.OKGREEN)
            print_color(self.sk.user.mood, Colors.OKGREEN)
        except ConnectionError as e:
            print_color(
                line,
                Colors.FAIL,
            )
            logging.error(e)
            self.__login()
        except Exception as e:
            print_color(
                line,
                Colors.FAIL,
            )
            logging.error(e)

    def __set_mood(self, emoji: str, music: Music) -> None:
        """
        Update the activity message for the current user.
        :param emoji: the emoji to be used in the activity message
        :param music: the object containing the music information
        """
        rich = f"'<ss type=\"{emoji.replace('(', '').replace(')', '')}\">" \
               f"{emoji}</ss> {music.name} - " \
               f"{music.artists} -" \
               f" <a href=\"{music.spotify_link}\">{music.spotify_link}</a>'"
        msg = f"{emoji} {music.name} - {music.artists} - {music.spotify_link}"
        self.sk.conn(
            "POST",
            f"{self.sk.conn.API_USER}/users/{self.sk.userId}/profile/partial",
            auth=skpy.SkypeConnection.Auth.SkypeToken,
            json={
                "payload": {
                    "mood": msg or "",
                    "richMood": rich or "",
                }
            }
        )

        self.sk.user.mood = skpy.SkypeUser.Mood(
            plain=msg,
            rich=rich
        ) if msg else None

    def update(self, music: Music) -> None:
        return self._update_bio(music)
