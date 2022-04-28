

import os
from pynput import keyboard

from time import sleep
import MyChessBoard

'''
    *
* * * * *
    *
    *
  * * *
▏▎▍▌▋▊▉✈▲▬
▁▂▃▄▅▆▇█
▏▏▏▏▏▏▏
▉▉▉▉▉▉▉
▆▆▆▆▆▆
'''

def on_press(key):
    None
def on_release(key):
    # print('{0} released'.format( key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    if key == keyboard.Key.up:
        print("up")
    if key == keyboard.Key.down:
        print("down")
    if key == keyboard.Key.left:
        print("left")
    if key == keyboard.Key.right:
        print("right")

def init_key():
    with keyboard.Listener( on_press=on_press, on_release=on_release) as listener:
    listener.join()
    listener = keyboard.Listener( on_press=on_press, on_release=on_release)
    listener.start()



board = MyChessBoard(10,10)
listener = ''

if __name__ == "__main__":

    print("Welcome to Guess-Plane-War !!! @firestaradmin")
    board.show_board()
    for i in range(0,10):
        board.chose(0,i)
        os.system('cls')
        board.show_board()
        sleep(0.2)