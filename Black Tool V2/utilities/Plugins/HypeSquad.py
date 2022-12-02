import json, requests, colorama, os, sys, time, threading
from os import system
from colorama import *
from pystyle import *

system('title Black Tool V2 - Hypesquad')
Write.Print("""
[1]Bravery
[2]Brilliance
[3]Balance
[4]Leave the HypeSquad""", Colors.purple_to_blue, interval=0.000)
house = Write.Input("""
[>>>]Select an option:""", Colors.purple_to_blue, interval=0.000)

def hype(token):
            headers = {'Authorization' : token}

            if house == "1":
                housefinal = '1'

            if house == "2":
                housefinal = '2'

            if house == "3":
                housefinal = '3'

            if house == '4':
                housefinal = None

            if house == '1' or '2' or '3':
                payload = {
                    'house_id': housefinal
                }
                rep = requests.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
                if rep.status_code == 204:
                    Write.Print(f'''[>]Done''', Colors.cyan_to_blue, interval=0.000)
                else:
                    Write.Print(f'''[!]Failed, Retrying.''', Colors.red_to_yellow, interval=0.000)

            if house == '4':
                payload = {
                    'house_id': housefinal
                }
                req = requests.delete('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload)
                if req.status_code == 204:
                    Write.Print(f'''
[>]Done''', Colors.cyan_to_blue, interval=0.000)
                    return
                else:
                    pass

            else:
                pass

tokens = open('tokens.txt', 'r').read().splitlines()
for token in tokens:
            threading.Thread(target=hype(token)).start()


exit = Write.Input('''
[>>>]Press ENTER to exit:''', Colors.purple_to_blue, interval=0.000)
os.startfile('Component.py')
os._exit(0)