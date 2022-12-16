from PPlay.sprite import Sprite

class Tile(Sprite):
    W = 50
    H = 50

    def __init__(self, l, posx, posy):
        if type(l) == int:
            l = chr(0x40 + l)
        elif type(l) == str and len(l) == 1:
            l = l.upper()
        else:
            raise ValueError(l)
        if l not in ('A', 'B', 'C', 'D', 'G'):
            raise ValueError(l)
        Sprite.__init__(self, f"assets/Tile{l}.png")
        self.x = posx
        self.y = posy
    
    def move(self, songspeed, win):
        self.move_y(songspeed * win.delta_time())
    
    def underscreen(self, wheight):
        return self.y > wheight

    def overscreen(self):
        return self.y + Tile.H < 0
    