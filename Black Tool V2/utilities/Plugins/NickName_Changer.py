import threading, time, os, requests, json, sys, colorama
from os import system
from colorama import *
from pystyle import *

system("title Black Spammer - NickName Changer")
def changenick(server, nickname, token):
            headers = {'Authorization' : token}

            r = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                               json={"nick": nickname})
            if r.status_code == 200:
                Write.Print(f'''
[>]Nickname Changed Succesfully!''', Colors.purple_to_blue, interval=0.000)
            elif r.status_code != 200:
                Write.Print(f'''
[-]Error, Cant Change Nickname...''', Colors.red_to_yellow, interval=0.000)

tokens = open('tokens.txt', 'r').read().splitlines()
server = Write.Input("Server ID:", Colors.purple_to_blue, interval=0.000)
nick = Write.Input("Nickname:", Colors.purple_to_blue, interval=0.000)
for token in tokens:
  threading.Thread(target=changenick, args=(server, nick, token)).start()
Write.Input("""
[>]Press ENTER to exit:""", Colors.purple_to_blue, interval=0.000)
os.startfile('Component.py')
os._exit(0)


        