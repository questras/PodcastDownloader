import requests
import os
from typing import List


class Downloader:
    """Class to download and save podcasts."""

    def download_podcast(self, url: str, filepath: str):
        """Download podcast in given url and save it to 
        given filepath."""

        r = requests.get(url, allow_redirects=True)

        with open(filepath, 'wb') as file:
            file.write(r.content)

    def print_info(self, url: str, filepath: str):
        """Print downloading info."""

        print(f'Now downloading: \n{url}')
        print(f'Save in: \n{filepath}')

    def print_finished_info(self):
        """Print info about finished download."""

        print("Finished!")
        print()
    
    def download_podcasts(self, urls_and_filepaths: List[tuple], 
                          log: bool=False):
        """Download podcasts in given urls and save them to 
        corresponding filepaths. Info about downloading is printed
        if log is set to True"""

        for url, filepath in urls_and_filepaths:
            if log:
                self.print_info(url, filepath)

            self.download_podcast(url, filepath)

            if log:
                self.print_finished_info()