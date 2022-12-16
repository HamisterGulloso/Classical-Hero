import os
from json import dump

SONGINFOFILE = 'songinfo.json'

def sync():
    songs = []
    for song_dir in os.listdir("songs"):
        with open(f"songs/{song_dir}/song") as file:
            songs.append({
                "song_dir": song_dir,
                "name": file.readline()[:-1],
                "composer": file.readline()[:-1]
            })
    with open(SONGINFOFILE, 'w') as file:
        dump(songs, file)
