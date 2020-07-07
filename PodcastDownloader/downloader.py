import requests
import os
from typing import List

from .utils import print_error, print_info, print_success, request_has_errors


class Downloader:
    """Class to download and save podcasts."""

    def __init__(self):
        pass

    def download_podcast(self, url: str, filepath: str):
        """Download podcast in given url and save it to 
        given filepath."""

        r = requests.get(url, allow_redirects=True)
        if request_has_errors(r):
            print_error(f'Could not download {url}')
            return

        with open(filepath, 'wb') as file:
            file.write(r.content)

    def print_download_info(self, url: str, filepath: str):
        """Print downloading info."""

        print_info(f'Now downloading: {url}')
        print_info(f'Save in: {filepath}')

    def print_finished_info(self):
        """Print info about finished download."""

        print_success("Finished!\n")

    def download_podcasts(self, urls_and_filepaths: List[tuple],
                          log: bool = False):
        """Download podcasts in given urls and save them to 
        corresponding filepaths. Info about downloading is printed
        if log is set to True."""

        for url, filepath in urls_and_filepaths:
            if log:
                self.print_download_info(url, filepath)

            self.download_podcast(url, filepath)

            if log:
                self.print_finished_info()
