import argparse
import os

from PodcastDownloader.talkpython import TalkPythonPodcast
from PodcastDownloader.downloader import Downloader
from PodcastDownloader.porozmawiajmyoit import PorozmawiajmyOITPodcast
from PodcastDownloader.utils import print_error


podcasts = {
    'talkpython': TalkPythonPodcast(),
    'porozmawiajmyoit': PorozmawiajmyOITPodcast()
}


def parse_name_and_path() -> tuple:
    """Parse command line arguments specifying 
    name of desired podcast and path to download it to."""

    parser = argparse.ArgumentParser(description='Download desired podcast.')

    parser.add_argument(
        'Name',
        metavar='name',
        type=str,
        help='name of desired podcast'
    )
    parser.add_argument(
        'Path',
        metavar='path',
        type=str,
        help='path to download podcast to'
    )

    args = parser.parse_args()

    return args.Name, args.Path


def check_podcast_name(name: str) -> bool:
    """Check if given name is valid podcast name."""
    return name in podcasts.keys()


def check_path(path: str) -> bool:
    """Check if given path is valid directory path."""
    return os.path.isdir(path)


def main():
    """Main program function."""

    name, path = parse_name_and_path()

    if not check_podcast_name(name):
        print("Given podcast does not exist.")
        quit()

    if not check_path(path):
        print("Given path is incorrect.")
        quit()

    urls_and_names = podcasts[name].get_urls_and_names()

    if urls_and_names is None:
        print_error("Download failed.")
        quit()

    urls_and_paths = [
        (url, os.path.join(path, name)) for (url, name) in urls_and_names
        ]

    downloader = Downloader()
    downloader.download_podcasts(urls_and_paths, log=True)


if __name__ == "__main__":
    main()
