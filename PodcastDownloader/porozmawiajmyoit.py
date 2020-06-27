import bs4
import requests
from typing import List


class PorozmawiajmyOITPodcast:
    """Class to get urls and names of all episodes
    of Porozmawiajmy o IT podcast."""

    def get_download_url(self, podcast_url: str) -> str:
        """Get podcast download link from given podcast url."""

        r = requests.get(podcast_url)
        r.raise_for_status()

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
        of Porozmawiajmy o IT podcast"""

        episodes_url = 'https://porozmawiajmyoit.pl/'

        r = requests.get(episodes_url)
        r.raise_for_status()

        soup = bs4.BeautifulSoup(r.text, features="html.parser")
        a_elements = soup.findAll('a', class_='podcast-button')
        podcast_urls = [element['href'] for element in a_elements]
        podcast_names = [url.split('/')[-2] + '.mp3' for url in podcast_urls]
        download_urls = [self.get_download_url(url) for url in podcast_urls]
        
        return list(zip(download_urls, podcast_names))
