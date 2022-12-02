import sys
from colorama import Fore, Style
import os
from pystyle import *
import time
from disnake import Webhook
import requests
import dhooks

import colorama

choice = Write.Input(f"""
[%]Choice:""", Colors.green_to_yellow, interval=0.000)

if choice == "1":
    def webhook_spammer():
        colorama.init(autoreset=True)
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print(f"{Fore.GREEN}[+]{Fore.WHITE}Enter Webhook: ")
            webhook = input("")
            r_check = requests.get(webhook)
            r_check = str(r_check)
            if "200" in r_check:
                break
            if "200" not in r_check:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print(f"{Fore.GREEN}[+]{Fore.WHITE}Webhook Invalid, Please Enter A Valid One")
        except Exception:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print(f"{Fore.GREEN}[+]{Fore.WHITE}Webhook Invalid, Please Enter A Valid One")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print(f"{Fore.GREEN}[+]{Fore.WHITE}Enter Message: ")
    content = input("")
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print(f"{Fore.GREEN}[+]{Fore.WHITE}Want An Avatar (y/n): ")
        avatar_y_n = input("")
        if avatar_y_n == "n" or avatar_y_n == "y":
            break
        else:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print(f"{Fore.GREEN}[+]{Fore.WHITE}Enter A Valid Choice")
    if avatar_y_n == "y":
        while True:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print(f"{Fore.GREEN}[+]{Fore.WHITE}Enter Avatar Url: ")
            avatar_url = input("")
            if "http://" in avatar_url or "https://" in avatar_url:
                break
            else:
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print(f"{Fore.GREEN}[+]{Fore.WHITE}Enter A Valid Choice")
    if avatar_y_n == "n":
        avatar_url = ""
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print(f"{Fore.GREEN}[+]{Fore.WHITE}Enter Bot Username: ")
    username = input("")
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print(f"{Fore.GREEN}[+]{Fore.WHITE}Enter Limit (i for infinity): ")
        limit = input("")
        if limit == "i" or limit == "I":
            break
        try:
            limit = int(limit)
            break
        except Exception:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print(f"{Fore.GREEN}[+]{Fore.WHITE}Enter A Valid Choice")
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print(f"{Fore.GREEN}[+]{Fore.WHITE}Enter Delay (0 For None): ")
            delay = input("")
            delay = float(delay)
            break
        except:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print(f"{Fore.GREEN}[+]{Fore.WHITE}Enter A Valid Choice")
    if limit == "i" or limit == "I":
        limit = str(limit)
        
    den = 0
    if limit == "i" or limit == "I":
        while True:
            r = requests.post(webhook, json={"avatar_url": avatar_url, "username": username, "content": content})
            r = str(r)
            if "204" in r:
                den = int(den) + 1
                print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.CYAN}/{colorama.Fore.RESET}INFINITY{colorama.Fore.CYAN}]{colorama.Fore.RESET} Sent Message To The {colorama.Fore.CYAN}Webhook")
            if "429" in r:
                print(f"{colorama.Fore.RED}[{colorama.Fore.RESET}ERROR{colorama.Fore.RED}]{colorama.Fore.RESET} Rate Limited, {colorama.Fore.RED}Retrying")



    for u in range(int(limit)):
        while True:
            r = requests.post(webhook, json={"avatar_url": avatar_url, "username": username, "content": content})
            r = str(r)
            if "204" in r:
                den = int(den) + 1
                print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.CYAN}/{colorama.Fore.RESET}{str(limit)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Sent Message To The {colorama.Fore.CYAN}Webhook")
                break
            if "429" in r:
                print(f"{colorama.Fore.RED}[{colorama.Fore.RESET}ERROR{colorama.Fore.RED}]{colorama.Fore.RESET} Rate Limited, {colorama.Fore.RED}Retrying")


    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print(f"{Fore.GREEN}[+]{Fore.WHITE}Done Spamming Webhook, Press Enter To Close The Program")
    os.startfile('Component.py')
    os._exit(0)






elif choice == "2":
    hook = input(f"{Fore.GREEN}[+]{Fore.WHITE}Webhook URL:")
def delete(webhook):
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        input(f"\n {Fore.GREEN}[+]{Fore.WHITE}Success, webhook deleted, Press ENTER to exit:")
        os.startfile('Component.py')
        os._exit(0)
    elif check.status_code == 200:
        input(f"\n {Fore.RED}[-]{Fore.WHITE}Failed To delete the webhook, Press ENTER to exit:")
        os.startfile('Component.py')
        os._exit(0)

kingman_top = 1
if kingman_top == 1:
    delete(hook)


