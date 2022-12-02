from requests import get, post
from random import randint
from pystyle import *
import os, sys

def variant1(token):
    response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})#Bad variant for mass token check due to the rate limit.
    return True if response.status_code == 200 else False

def variant2(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True

def variant2_Status(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'

if __name__ == "__main__":
    try:
        checked = []
        with open('tokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and variant2(token) == True:
                    Write.Print(f'''
[+]Token: {token} | Valid Token''', Colors.blue_to_purple, interval=0.000)
                    checked.append(token)
                else:
                    Write.Print(f'''
[+]Token: {token} | Invalid Token''', Colors.red_to_yellow, interval=0.000)
        if len(checked) > 0:
            save = Write.Input(f'''
{len(checked)} valid tokens founded!\nDo you want to save the valid tokens in the file "valid.txt" (y/n)''', Colors.yellow_to_green, interval=0.000).lower()
            if save == 'y':
                name = open("valid.txt")
                with open(f'valid.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
                Write.Print(f'I have succesfully saved the valid tokens to valid.txt File!', Colors.black_to_white, interval=0.000)
        Write.Input('''
[>>]Press Enter For Exit...''', Colors.cyan_to_blue, interval=0.000)
        os.startfile('Component.py')
        os._exit(0)
    except:
        Write.Input('''
[+]Unknow error, you are probably offline. Press ENTER to exit:''', Colors.red_to_yellow, interval=0.000)
        os.startfile('Component.py')
        os._exit(0)
        