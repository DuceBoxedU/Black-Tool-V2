from sqlite3 import enable_shared_cache
import time, requests, websocket
from websocket import *
import easygui
from threading import *
import os
import re
import sys
import time
import emoji
import ctypes
import random
import string
import shutil
import zipfile
import datetime
import colorama
import requests
from pystyle import *
import threading
import easygui, os
from os import system
import random, string
from json import loads
from time import sleep
from json import dumps
from colorama import *
import base64, pyperclip
from typing import Union
import webbrowser, base64
from colorama import Fore
import requests, threading
from tasksio import TaskPool
from tqdm import tqdm, trange
from websocket import WebSocket
from os.path import isfile, join
from disnake.ext import commands
from colorama import Back, Fore, Style
from concurrent.futures import ThreadPoolExecutor



tokenlist = open('tokens.txt', 'r').read().splitlines()
channel = int(Write.Input("[>]Voice Channel ID: ", Colors.cyan_to_blue, interval=0.000))
server = int(Write.Input("[>]Server ID: ", Colors.cyan_to_blue, interval=0.000))
message = Write.Input("[>]Spam Message (y/n)?:", Colors.cyan_to_blue, interval=0.000)
deaf = Write.Input("[>]Defean the tokens: (y/n)? ", Colors.blue_to_purple, interval=0.000)
if deaf == "y":
          deaf = True
elif deaf == "n":
            deaf = False
mute = Write.Input("[>]Mute: (y/n)? ", Colors.blue_to_purple, interval=0.000)
if mute == "y":
          mute = True
elif mute == "n":
            mute = False
stream = Write.Input("[>]Stream: (y/n)? ", Colors.blue_to_purple, interval=0.000)
if stream == "y":
          stream = True
elif stream == "n":
            stream = False
video = Write.Input("[>]Video: (y/n)? ", Colors.blue_to_purple, interval=0.000)
if video == "y":
          video = True
elif video == "n":
            video = False

executor = ThreadPoolExecutor(max_workers=int(1000))
def run(token):
          while True:
            ws = WebSocket()
            ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
            hello = loads(ws.recv())
            heartbeat_interval = hello['d']['heartbeat_interval']
            ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
            ws.send(dumps({"op": 4,"d": {"guild_id": server,"channel_id": channel,"self_mute": mute,"self_deaf": deaf, "self_stream": stream, "self_video": video}}))
            ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": server,"channel_id": channel,"preferred_region": "singapore"}}))
            ws.send(dumps({"op": 1,"d": None}))
            time.sleep(0.1)

if message == "104":
    print("[>]No")

elif message == "y":
   smessage=Write.Input("[>]Message to spam:", Colors.purple_to_blue, interval=0.000)
   for token in tokenlist: 
  #Write.Print(f"""
#[+]Succesfully Joined the VC | {token}""", Colors.red_to_yellow, interval=0.000)
 # while True:
    executor.submit(run, token)
    Write.Print(f"""
[+]Succesfully Joined the VC | {token}""", Colors.red_to_yellow, interval=0.000)

   msg = "https://discord.com/api/v9/channels/"+str(channel)+"/messages" 
   m = {
    'content': smessage
    }
   headers22 = {'Authorization': token}
   with open('tokens.txt','r') as handle:
    tokens = handle.readlines()
    for x in tokens:
     token = x.rstrip()
     while True:
      for i in range(1):
       r=requests.post(msg, headers=headers22, json=m)
       if r.status_code == 200:
         Write.Print(f"""
[+]Message:{smessage} Sended Sucessfully to the channel:{channel} """, Colors.purple_to_blue, interval=0.000)
       else:
        Write.Print("""
[>]Error""", Colors.red_to_yellow, interval=0.000)
      for token in tokenlist: 
        for i in range(1):
         r=requests.post(msg, headers=headers22, json=m)
         if r.status_code == 200:
          Write.Print(f"""
[+]Message:{smessage} Sended Sucessfully to the channel:{channel} """, Colors.purple_to_blue, interval=0.000)
         else:
          Write.Print("""
[>]Error""", Colors.red_to_yellow, interval=0.000)
elif message == "n":
 for token in tokenlist: 
  #Write.Print(f"""
#[+]Succesfully Joined the VC | {token}""", Colors.red_to_yellow, interval=0.000)
 # while True:
   executor.submit(run, token)
   Write.Print(f"""
[+]Succesfully Joined the VC | {token}""", Colors.red_to_yellow, interval=0.000)

