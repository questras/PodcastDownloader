import bs4
import requests
from typing import List

from .utils import request_has_errors, print_error, print_info, print_success


class PorozmawiajmyOITPodcast:
    """Class to get urls and names of all episodes
    of Porozmawiajmy o IT podcast."""

    def get_download_url(self, podcast_url: str) -> str:
        """Get podcast download link from given podcast url or None
        if request failed.
        """

        r = requests.get(podcast_url)
        if request_has_errors(r):
            print_error(f'Could not get {podcast_url} download link.')
            return None

        soup = bs4.BeautifulSoup(r.text, features="html.parser")
        a_elements = soup.findAll('a')
        download_url = None

        for element in a_elements:
            if 'href' in element.attrs and 'download=true' in element['href']:
                download_url = element['href']
                break

        return download_url

    def get_urls_and_names(self) -> List[tuple]:
        """Return  urls and names of all episodes
        of Porozmawiajmy o IT podcast that could be
        obtained from the website."""

        episodes_url = 'https://porozmawiajmyoit.pl/'

        r = requests.get(episodes_url)
        if request_has_errors(r):
            return None

        soup = bs4.BeautifulSoup(r.text, features="html.parser")
        a_elements = soup.findAll('a', class_='podcast-button')
        podcast_urls = [element['href'] for element in a_elements]
        podcast_names = [url.split('/')[-2] + '.mp3' for url in podcast_urls]

        print_info('Getting download urls.')
        download_urls = [self.get_download_url(url) for url in podcast_urls]
        print_success('Download urls obtained.')

        # Remove all None values.
        download_urls = [url for url in download_urls if url]

        return list(zip(download_urls, podcast_names))
