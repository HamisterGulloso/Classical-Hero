from tile import Tile
from pick import Pick

PADDBTW = 30
PADDBOT = 120

def read(dir, win, speed, delay):
    tx = [
        (win.width/2) - (PADDBTW*3/2) - 2*Pick.W,
        (win.width/2) - (PADDBTW/2) - Pick.W,
        (win.width/2) + (PADDBTW/2),
        (win.width/2) + (PADDBTW*3/2) + Pick.W
    ]

    ret = []
    with open(f"./songs/{dir}/song") as file:
        for _ in range(3):
            file.readline()
        for line in file:
            if len(line) <= 1:
                break
            pos, n = map(int, line.split(';'))
            pos = pos * speed / 1000
            ret.append(
                Tile(
                    n,
                    tx[n-1],
                    win.height - delay - pos - PADDBOT - Pick.H
                )
            )
    
    return ret
