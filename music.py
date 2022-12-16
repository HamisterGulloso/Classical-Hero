from PPlay.sound import Sound

ALLOW_NO_MUSIC = True

class NoSongError(Exception):
    pass

class Music:
    def __init__(self, song):
        try:
            self.back = Sound(f"./songs/{song}/back.ogg")
            self.main = Sound(f"./songs/{song}/main.ogg")
        except FileNotFoundError:
            raise NoSongError

    def play(self):
        _, __ = self.back.play(), self.main.play()

    def mute(self):
        self.main.set_volume(0)
    
    def unmute(self):
        self.main.set_volume(50)

    def stop(self):
        self.main.stop()
        self.back.stop()

    def is_playing(self):
        return self.main.is_playing() or self.back.is_playing()
