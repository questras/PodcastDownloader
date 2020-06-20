import requests
import os
from typing import List

class Downloader:
    """Class to download and save podcasts."""

    def download_podcast(url: str, filepath: str):
        """Download podcast in given url and save it to 
        given filepath."""

        r = requests.get(url, allow_redirects=True)

        with open(filepath, 'wb') as file:
            file.write(r.content)
    
    def download_podcasts(urls_and_filepaths: List(tuple)):
        """Download podcasts in given urls and save them to 
        corresponding filepaths."""

        for url, filepath in urls_and_filepaths:
            download_podcast(url, filepath)