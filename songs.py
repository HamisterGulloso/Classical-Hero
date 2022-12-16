from json import load
from play import play

from PPlay.sprite import Sprite

def songs(win, key):
    with open('songinfo.json') as file:
        songs = load(file)
    number_options = len(songs)
    OPTIONS_MAX = 5
    choose = 0
    top_option = 0

    up_arrow = Sprite('assets/arrow_up.png')
    up_arrow.x = win.width/2 - up_arrow.width/2
    up_arrow.y = 80
    down_arrow = Sprite('assets/arrow_down.png')
    down_arrow.x = win.width/2 - down_arrow.width/2
    down_arrow.y = win.height - 40

    while True:
        if key.key_pressed("down"):
            choose = (choose + 1) % number_options
            if choose > top_option + OPTIONS_MAX - 1:
                top_option = choose - OPTIONS_MAX + 1
            if choose < top_option:
                top_option = 0
        if key.key_pressed("up"):
            choose = (choose - 1) % number_options
            if choose < top_option:
                top_option = choose
            if choose > top_option + OPTIONS_MAX - 1:
                top_option = choose - OPTIONS_MAX + 1
        if key.key_pressed("enter") or key.key_pressed("enter") or key.key_pressed("space"):
            play(win, key, songs[choose]["song_dir"])
        if key.key_pressed("escape"):
            break

        win.set_background_color(0)        
        win.draw_text(
            "Músicas",
            500,
            20,
            size=50,
            color=(255, 255, 255),
            bold=1
        )
        for s in range(min(OPTIONS_MAX, number_options)):
            name_pos = 110 +100*s
            composer_pos = 160 + 100*s
            if top_option != 0:
                up_arrow.draw()
            if top_option != number_options - OPTIONS_MAX:
                down_arrow.draw()
            win.draw_text(songs[s + top_option]["name"], 20 , name_pos, size=50, color=(255, 255, 255), bold=1 if choose == s + top_option else 0)
            win.draw_text(songs[s + top_option]["composer"], 25, composer_pos, size=35, color=(255, 255, 255), bold=1 if choose == s + top_option else 0)
        win.update()