import requests, time, random, os, re, threading, base64
from colorama import *
from pystyle import *
from os.path import isfile, join
from tkinter.filedialog import *


def SpamServers():
 token=Write.Input("[>]Input the Token:", Colors.cyan_to_blue, interval=0.000)
 headers = {'authorization':token}
 nameguild = Write.Input("[>]Guild Names:", Colors.purple_to_blue, interval=0.000)
 def createguilds2():
        setup = {'name': f'{nameguild}', 'region': 'europe', 'icon': None , 'channels': None}
        r = requests.post("https://discord.com/api/v9/guilds", headers=headers, json=setup)
        for i in range(100):
         try:
          threading.Thread(target=createguilds2).start()
          Write.Print(f"""
Succesfully created the server:{nameguild}""", Colors.purple_to_blue, interval=0.000)
         except:
          Write.Print(f"""
[>]Error""", Colors.red_to_yellow, interval=0.000)
 createguilds2()


SpamServers()