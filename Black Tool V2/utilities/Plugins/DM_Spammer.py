import requests
import colorama 
import os
from os import system
import time
import randstr
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

async def screen5(self):
        try:
            await self.rpc.update(state="DM Spammer Screen", details="Black Spammer", large_image="default")
        except:
            pass
        os.system('cls')
        self.sendText('screen5')
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide user id: ',
              end='')
        userId = input()
        if userId == '0':
            await self.start()
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide message: ',
              end='')
        msg = input()
        if msg == '0':
            await self.start()
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN + 'Amount: ',
              end='')
        amount = input()
        if amount == '0':
            await self.start()
        try:
            await self.rpc.update(state="Using DM Spammer", details="Exe Spammer", large_image="default")
        except:
            pass
        async with TaskPool(5_000) as pool:
            for token in self.tokens:
                await pool.put(self.dmSpammer(token, userId, msg, amount))
        await asyncio.sleep(5)
        await self.start()

async def dmSpammer(self, token, userId, msg, amount="100000"):
        headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        tk = token
        try:
            tk = token[:25] + "*" * 34
        except:
            tk = "*" * len(token)

        async with ClientSession(headers=headers) as session:
            for i in range(int(amount)):

                randomProxy = ''
                if self.proxyless == False:
                    randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

                async with session.post(
                        "https://discord.com/api/v9/users/@me/channels",
                        json={"recipient_id": userId}, proxy=randomProxy) as r:
                    if r.status == 200:
                        json = await r.json()
                        id = json["id"]
                        async with session.post(
                                "https://discord.com/api/v9/channels/%s/messages"
                                % (id),
                                json={"content": msg}) as r:
                            text = await r.text()
                            if "content" in text:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} successfully sent message!\n' +
                                    Fore.RESET)
                            elif "You need to verify your account" in text:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} is unverified and removed from list!\n'
                                    + Fore.RESET)
                                if token in self.tokens:
                                    self.tokens.remove(token)
                            elif "Unauthorized" in text:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} is invalid and removed from list!\n'
                                    + Fore.RESET)
                                if token in self.tokens:
                                    self.tokens.remove(token)
                            else:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} failed to send message!\n' +
                                    Fore.RESET)
                    else:
                        print('\n                                       ' +
                              Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                              '] ' + Fore.CYAN +
                              f'{tk} Failed to send message!\n' + Fore.RESET)

tokens = open("tokens.txt", "r").read().splitlines()
while True:
 dmSpammer(token=tokens, userId=Write.Input("[>]Victim ID:", Colors.purple_to_blue, interval=0.000), msg=Write.Input("[>]Message:", Colors.purple_to_blue, interval=0.000))