from pynput import keyboard

def on_press(key):
    None
    # try:
    #     print('alphanumeric key {0} pressed'.format( key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(  key))

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


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()






if __name__ == "__main__":
    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()





