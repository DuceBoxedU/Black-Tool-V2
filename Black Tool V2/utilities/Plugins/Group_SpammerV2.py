import requests, time, json, colorama, os, random, sys
from os import system
from colorama import *
from pystyle import *

system(f"title Black Tool - GroupChat Spammer")

UserID = Write.Input('[>]User ID: ', Colors.purple_to_blue, interval=0.000)
group = Write.Input('Group Names: ', Colors.purple_to_blue, interval=0.000)
manygr = int(Write.Input('How Many Groups: ', Colors.purple_to_blue, interval=0.000))
tokens = open('tokens.txt', 'r').read().splitlines()
for token in tokens:
 headers = {'Authorization' : token}
 for i in range(manygr):
            try:
                r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers,
                                  json={"recipients": []})

                jsr = json.loads(r.content)
                groupID = jsr['id']
                r1 = requests.patch(f'https://discord.com/api/v9/channels/{groupID}', headers=headers,
                                    json={'name': group})
                if r1.status_code == 200:
                    print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Group created')

                with open("utilities/Components/groups.txt", "w") as groupID:
                    groupID.write(jsr['id'] + '\n')

            except:
                print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] RateLimited')

            scrIds = random.choice(open('utilities/Components/groups.txt').readlines())
            grID = scrIds.strip('\n')
            r2 = requests.put(f'https://discord.com/api/v9/channels/{grID}/recipients/{UserID}',
                              headers={'Authorization': token})
            if r2.status_code == 204:
                print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Group Members: {UserID}')

time.sleep(1)
exit = Write.Input('Press ENTER to exit: ', Colors.purple_to_blue, interval=0.000)
os.startfile('Component.py')
os._exit(0)