import requests
import colorama 
import os
from os import system
import time
import threading
from pystyle import *
from tkinter import *
import datetime
from aiohttp.client import ClientSession
import sys, os, asyncio, shutil, colorama, encodings.idna, time, random
from colorama import Fore
import pymongo
from pymongo.errors import OperationFailure
from pypresence.presence import AioPresence
from tasksio import TaskPool
from aiohttp import client_exceptions
from sys import exit
import asyncio
from tkinter.filedialog import *
from colorama import Fore, Back, Style  


choichespammer = Write.Input(f'''
[+]Choice: ''', Colors.blue_to_cyan, interval=0.000)

#JOINER
if choichespammer == '1':
        link = input(f"{Fore.MAGENTA}[{Fore.WHITE}+{Fore.MAGENTA}]{Fore.WHITE}Server link:")
        if len(link) > 8:
            invite = link[19:]
        else:
            invite = link
        apilink = f"https://discord.com/api/v9/invites/" + invite
        with open('tokens.txt','r') as handle:
            tokens = handle.readlines()
            for x in tokens:
                token = x.rstrip()
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                    'Accept': '/',
                    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Content-Type': 'application/json',
                    'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                    'Authorization': token,
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                    'X-Discord-Locale': 'en-US',
                    'X-Debug-Options': 'bugReporterEnabled',
                    'Origin': 'https://discord.com/',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Referer': 'https://discord.com/',
                    'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'TE': 'trailers',
                    }
                requests.post(apilink, headers=headers, json = {})
                r = requests.get(apilink)
                if r.status_code == 200:
                    Write.Print(f"[+]{token} Joined succesfully \n", Colors.blue_to_purple, interval=0.000)
                    
                else:
                    Write.Print(f"[-]{token} Failed to join \n", Colors.blue_to_red, interval=0.000)
#LEAVER       
elif choichespammer == "2":
 Write.Print("[!]Open tokens.txt file...", Colors.blue_to_red, interval=0.000)
 Tk().withdraw()
 token = askopenfilename()
 with open(token) as handle:
    txtf = handle.read()

 f = open("tokens.txt","w+")
 f.write(txtf)
 f.close()

 ID = Write.Input('''
[+]Discord Server ID to leave: ''', Colors.blue_to_cyan, interval=0.000)
 
 apilink = "https://discordapp.com/api/v9/users/@me/guilds/" + str(ID)

 with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            rl=requests.delete(apilink, headers=headers)
        Write.Print("""
[+]All valid tokens have left that server.""", Colors.blue_to_purple, interval=0.000)
#SPAMMER
elif choichespammer == '3':
    channel_id = Write.Input(f"[>]Channel id:", Colors.blue_to_purple, interval=0.000)
    messages = Write.Input(f"[>]Message:", Colors.blue_to_purple, interval=0.000)
    with open('tokens.txt','r') as handle:
            tokens = handle.readlines()
            for x in tokens:
             token = x.rstrip()
             while True:
              payload={"content": messages, "tts": False}
              header = {"authorization": token, "content-type": "application/json"}
              r = requests.post(f"https://discordapp.com/api/v8/channels/{channel_id}/messages", headers=header, data=json.dumps(payload))
              if r.status_code == 200:
                    Write.Print(f"""
[+]Message Sent succesfully | {token}""", Colors.blue_to_purple, interval=0.000)
                    
              else:
                    Write.Print(f"""
[-]Failed to send the message | {token}""", Colors.red_to_yellow, interval=0.000) 



elif choichespammer == "4":
 exec(open('utilities/Plugins/DM_Spammer.py').read()) 

#Coming Soon... (Thread Spammer)
elif choichespammer == "5":
 exec(open('utilities/Plugins/HypeSquad.py').read()) 
elif choichespammer == "6":
 system('title Black Spammer - [6]Token Onliner')
 exec(open('utilities/Plugins/Token-OnlinerV2.py').read())    
elif choichespammer == "7":
    exec(open('utilities/Plugins/NickName_Changer.py').read())   
elif choichespammer == "8":
    exec(open('utilities/Plugins/PFP_Changer.py').read())
elif choichespammer == "9":
    exec(open('utilities/Plugins/Group_SpammerV2.py').read())
elif choichespammer == "10":
    exec(open('utilities/Plugins/Friend_Request.py').read())
elif choichespammer == "11":
    exec(open('utilities/Plugins/About.Activity_Changer.py').read())
elif choichespammer == "12":
    exec(open('utilities/Plugins/VC_Spammer.py').read())
elif choichespammer == "13":
    system('title [13]Exiting...')
    os.system('cls')
    Write.Print("Exiting...", Colors.green_to_yellow, interval=0.000)
    time.sleep(1.5)
    os.startfile('Component.py')
    os._exit(0)