# PodcastDownloader
Script to download IT podcasts. 
It downloads all episodes of given podcast to chosen directory.

Currently available podcasts:
- https://porozmawiajmyoit.pl/ - name: porozmawiajmyoit
- https://talkpython.fm/ - name: talkpython

## Usage
Go to main directory of the project and type in terminal:
```
python3 download.py <podcast_name> <path_to_store_episodes>
```
where 
- <podcast_name> is one of podcast names written above,
- <path_to_store_episodes> is path to directory where episodes will be stored.

## Requirements
All required python libraries are in *requirements.txt* file.

**Not tested on Windows.**
