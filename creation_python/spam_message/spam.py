from pynput.keyboard import Key, Controller
import time

message = "@fuck"
keyboard = Controller ()

time.sleep(0)

for num in range(20):
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0)
