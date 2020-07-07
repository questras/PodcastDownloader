import bs4
import requests
from typing import List

from .utils import request_has_errors


class TalkPythonPodcast:
    """Class to get urls and names of all episodes
    of Talk Python podcast."""

    def get_urls_and_names(self) -> List[tuple]:
        """Return  urls and names of all episodes
        of Talk Python podcast"""

        episodes_url = 'https://talkpython.fm/episodes/all'
        urlbase = 'https://talkpython.fm'

        r = requests.get(episodes_url)
        if request_has_errors(r):
            return None

        soup = bs4.BeautifulSoup(r.text, features="html.parser")
        a_elements = soup.findAll('a')

        urls_and_names = []
        for element in a_elements:
            if 'episodes/show' in element['href']:
                url = urlbase + element['href'].replace('/show/', '/download/')
                name = url.split('/')[-1] + '.mp3'

                urls_and_names.append((url, name))
        
        return urls_and_names
