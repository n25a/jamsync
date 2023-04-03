import abc

from utils import Music


class Social(abc.ABC):

    @abc.abstractmethod
    def update(self, music: Music) -> None:
        """
        update the social media status of the current user with the current music playing
        on Spotify in the following format:
        <emoji> <song name> - <artist name> - <spotify link>
        :param music: the object containing the music information
        """
        raise NotImplemented