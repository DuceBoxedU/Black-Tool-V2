from pystyle import *
import random
import sys, os
from os import system
import time
import datetime
import string
from colorama import *
import requests

system('title Black Tool V2 - [3]Nitro Gen')
num = int(Write.Input(f'[>]Input an amount of nitro codes: ', Colors.blue_to_cyan, interval=0.000))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    Write.Print(f"""[>]Generating {num} of nitro codes!""", Colors.red_to_purple, interval=0.000)
    count = 0
    start = time.time()
    
    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    Write.Print(f"""
[{datetime.datetime.now()}]Generating {num} of nitro codes!\n""", Colors.red_to_yellow, interval=0.000)

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            Write.Print(f"""
[{datetime.datetime.now()}]I found a valid nitro code! | {nitro} """, Colors.green_to_red, interval=0.000)
            break
        else:
           count += 1
           print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}{count}{Fore.LIGHTMAGENTA_EX}]{Fore.RED}Invalid nitro code | {Fore.GREEN}{nitro}{Fore.RED} |{Fore.LIGHTBLACK_EX} Remaining Nitro Codes:{num-count}")

truncateyesorno = Write.Input(f"""
[>]Do you want to clear the file Nitro codes.txtY/N:""", Colors.cyan_to_blue, interval=0.000)  
if truncateyesorno == "Y":
  os.system('cls')
  with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
   file.truncate(0)
   exit = Write.Input(f'''
[>]Press ENTER to exit: ''', Colors.red_to_purple, interval=0.000)
   Write.Print(f"""
Exiting...""", Colors.green_to_yellow, interval=0.000)
   time.sleep(1.5)
   os.startfile('Component.py')
   os._exit(0)
elif truncateyesorno == "y":
  with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
   file.truncate(0)
   os.system('cls')
   exit = Write.Input(f'''
[>]Press ENTER to exit: ''', Colors.red_to_purple, interval=0.000)
   Write.Print(f"""
Exiting...""", Colors.green_to_yellow, interval=0.000)
   time.sleep(1.5)
   os.startfile('Component.py')
   os._exit(0) 
elif truncateyesorno == "N":
  os.system('cls')
  exit = Write.Input(f'''
[>]Press ENTER to exit: ''', Colors.red_to_purple, interval=0.000)
  Write.Print(f"""
Exiting...""", Colors.green_to_yellow, interval=0.000)
  time.sleep(1.5)
  os.startfile('Component.py')
  os._exit(0)      
elif truncateyesorno == "n":
  os.system('cls')
  exit = Write.Input(f'''[>]Press ENTER to exit: ''', Colors.red_to_purple, interval=0.000)
  Write.Print(f"""
Exiting...""", Colors.green_to_yellow, interval=0.000)
  time.sleep(1.5)
  os.startfile('Component.py')
  os._exit(0)     
 