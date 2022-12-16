from PPlay.window import Window

from keyboard import Key
from songs import songs
from sync import sync

WINS = 75
WINW = 16*WINS
WINH = 9*WINS

OPTIONS = 3

def main():
    win = Window(WINW, WINH)
    win.set_title("Título desse jogo maravilhoso!")

    key = Key(win)

    choose = 0
    while True:
        if key.key_pressed("up"):
            choose = (choose - 1) % OPTIONS
        if key.key_pressed("down"):
            choose = (choose + 1) % OPTIONS
        if key.key_pressed("enter") or key.key_pressed("space"):
            if choose == 0:
                songs(win, key)
            if choose == 1:
                sync()
            if choose == 2:
                break

        win.set_background_color(0)
        win.draw_text("Classical Hero", 430, 20, 50, (255, 255, 255))
        win.draw_text("Jogar", 530, 100, size=50, color=(255, 255, 255), bold=1 if choose == 0 else 0)
        win.draw_text("Sincronizar Acervo", 380, 300, size=50, color=(255, 255, 255), bold=1 if choose == 1 else 0)
        win.draw_text("Sair", 540, 500, size=50, color=(255, 255, 255), bold=1 if choose == 2 else 0)
        win.update()



if __name__ == "__main__":
    main()
