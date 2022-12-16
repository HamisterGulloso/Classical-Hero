from PPlay.sprite import Sprite

class Pick(Sprite):
    W = 50
    H = 50

    def __init__(self, l, posx, posy):
        Sprite.__init__(self, f"assets/Pick{l.upper()}.png")
        self.x = posx
        self.y = posy