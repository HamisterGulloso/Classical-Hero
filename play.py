from PPlay.sprite import Sprite

from tile import Tile
from pick import Pick
from music import Music, NoSongError
from songreader import read

SPEED = 300
DELAY = 0

PADDBTW = 30
PADDBOT = 120

def play(win, key, song_dir):
    TX = [
        (win.width/2) - (PADDBTW*3/2) - 2*Pick.W,
        (win.width/2) - (PADDBTW/2) - Pick.W,
        (win.width/2) + (PADDBTW/2),
        (win.width/2) + (PADDBTW*3/2) + Pick.W
    ]

    back = Sprite("assets/fundo3.jpg")
    back.y = -120

    p1 = Pick(
        "a",
        TX[0],
        win.height - PADDBOT
    )
    p2 = Pick(
        "b",
        TX[1],
        win.height - PADDBOT
    )
    p3 = Pick(
        "c",
        TX[2],
        win.height - PADDBOT
    )
    p4 = Pick(
        "d",
        TX[3],
        win.height - PADDBOT
    )

    hits = 0
    
    tiles = read(song_dir, win, SPEED, DELAY)
    miss_tiles = []

    # Almost acceptable
    try:
        music = Music(song_dir)
    except NoSongError:
        class NoMusic:
            def play(self):
                pass
            def stop(self):
                pass
            def mute(self):
                pass
            def unmute(self):
                pass
        music = NoMusic()
    
    fps_cooldown = 2

    exit_cooldown = 0

    win.update()
    win.update()
    music.play()
    while True:
        if key.key_pressed("esc"):
            break
        
        fps = 0 if win.delta_time() == 0 else 1/win.delta_time()
        fps_cooldown -= win.delta_time()
        if fps_cooldown <= 0:
            fps_cooldown = 2
            win.set_title(f"Título desse jogo maravilhoso!, FPS:{fps:.2f}")
        back.draw()


            
        if not len(tiles):
            exit_cooldown += win.delta_time()
            if exit_cooldown >= 2:
                break
        
        if len(tiles) and tiles[0].y > win.height - PADDBOT + Tile.H:
            miss_tiles.append(
                Tile(
                    'G',
                    tiles[0].x,
                    tiles[0].y
                )
            )
            tiles.pop(0)
            music.mute()

        i = 0
        while True:
            if i >= len(tiles):
                i = len(tiles) - 1
                break
            if tiles[i].overscreen():
                break
            tiles[i].draw()
            i += 1
        
        if len(miss_tiles) and miss_tiles[0].underscreen(win.height):
            miss_tiles.pop(0)

        for t in tiles:
            t.move(SPEED, win)
        
        for m in miss_tiles:
            m.move(SPEED, win)
            m.draw()

        if key.key_pressed("a"):
            for j in range(0, i):
                if p1.collided(tiles[j]):
                    hits += 1
                    tiles.pop(j)
                    music.unmute()
                    break
            else:
                hits -= 1
                music.mute()

        if key.key_pressed("s"):
            for j in range(0, i):
                if p2.collided(tiles[j]):
                    hits += 1
                    tiles.pop(j)
                    music.unmute()
                    break
            else:
                hits -= 1
                music.mute()
            
        if key.key_pressed("d"):
            for j in range(0, i):
                if p3.collided(tiles[j]):
                    hits += 1
                    tiles.pop(j)
                    music.unmute()
                    break
            else:
                hits -= 1
                music.mute()

        if key.key_pressed("f"):
            for j in range(0, i):
                if p4.collided(tiles[j]):
                    hits += 1
                    tiles.pop(j)
                    music.unmute()
                    break
            else:
                hits -= 1
                music.mute()
            
        p1.draw()
        p2.draw()
        p3.draw()
        p4.draw()
        # print(hits)
        win.update()

    music.stop()
