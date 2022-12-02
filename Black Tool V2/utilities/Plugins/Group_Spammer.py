import pystyle, sys, os, time, colorama, requests, json, random
from colorama import *
from pystyle import *
from os import system
system("title Black Spammer - Group Spammer")
token = Write.Input('[>]Token: ', Colors.purple_to_blue, interval=0.000)
group = Write.Input('[>]Group Names: ', Colors.purple_to_blue, interval=0.000)
manygr = int(Write.Input('[>]Input an amount of groups: ', Colors.purple_to_blue, interval=0.000))

headers = {'Authorization' : token}

for i in range(manygr):
            count = 0
            try:
                r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers,
                                  json={"recipients": []})

                jsr = json.loads(r.content)
                groupID = jsr['id']
                time.sleep(0.5)
                r1 = requests.patch(f'https://discord.com/api/v9/channels/{groupID}', headers=headers,
                                    json={'name': group})
                if r1.status_code == 200:
                    count += 1
                    Write.Print(f'''
[>]Successfully created the group''', Colors.purple_to_blue, interval=0.000)

                with open("utilities/Components/groups.txt", "w") as groupID:
                    boh=groupID.write(jsr['id'] + '\n')

            except:
                print(f'{Fore.LIGHTRED_EX}[-]{Fore.LIGHTWHITE_EX}Error, The token has been RateLimited')
            scrIds = random.choice(open('utilities/Components/groups.txt').readlines())
            grID = scrIds.strip('\n')

time.sleep(1)
exit = input('Press ENTER to exit: ')
system("title Exiting...")
Write.Print("Exiting...", Colors.green_to_yellow, interval=0.000)
time.sleep(1.5)
os.system('cls')
os.startfile('Component.py')
os._exit(0)