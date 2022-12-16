class Key:
    def __init__(self, win):
        self.k = win.get_keyboard()
        self.keys_down = []

    def key_pressed(self, key):
        if self.k.key_pressed(key) and key not in self.keys_down:
            self.keys_down.append(key)
            return True
        if key in self.keys_down and not self.k.key_pressed(key):
            self.keys_down.remove(key)
        return False