import requests, time, json, sys, os, threading
from os import system
from pystyle import *
from colorama import *


system(f"title Black Tool V2 - Friend Request Spammer")
def friender(token, user):
            try:
                user = user.split("#")
                headers = {'Authorization' : token}
                payload = {"username": user[0], "discriminator": user[1]}
                src = requests.post('https://discord.com/api/v9/users/@me/relationships', headers=headers,
                                    json=payload)
                if src.status_code == 204:
                    Write.Print(f"""
[+]Friend Request Sent to {user[0]}#{user[1]} |  {token}""", Colors.purple_to_blue, interval=0.000)
            except:
                Write.Print(f"""
[-]Error | {token}""", Colors.red_to_yellow, interval=0.000)

user = Write.Input(f"Input the Username + Tag, (Example:.exe#5257): ", Colors.cyan_to_blue, interval=0.000)
tokens = open("tokens.txt", "r").read().splitlines()
for token in tokens:
            threading.Thread(target=friender, args=(token, user)).start()
Write.Input("[>]Done, Press enter to exit:", Colors.purple_to_blue, interval=0.000)
os.startfile('Component.py')
os._exit(0)



