import websocket,threading,random,json,time,os,sys
from pystyle import *
from colorama import *
tokens=open('tokens.txt','r').read().splitlines()
randomstatus=['online','idle','dnd']
count=0

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        Write.Print(f"Time Until Re-Online: {timer}",Colors.purple_to_blue, interval=0.000, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Onlining Tokens')

t = Write.Input("[+]Write how long you want the tokens to be online in seconds:", Colors.purple_to_blue, interval=0.000)

def websocket_token(token):
    ws=websocket.WebSocket();ws.connect('wss://gateway.discord.gg/?v=6&encording=json');response=ws.recv();event=json.loads(response);heartbeat_interval=event['d']['heartbeat_interval']/1000;auth={'op':2,'d':{'token':token,'capabilities':61,'properties':{'os':'Windows','browser':'Chrome','device':'','system_locale':'en-GB','browser_user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36','browser_version':'90.0.4430.212','os_version':'10','referrer':'','referring_domain':'','referrer_current':'','referring_domain_current':'','release_channel':'stable','client_build_number':'85108','client_event_source':'null'},'presence':{'status':random.choice(randomstatus),'since':0,'activities':[],'afk':False},'compress':False,'client_state':{'guild_hashes':{},'highest_last_message_id':'0','read_state_version':0,'user_guild_settings_version':-1}}};ws.send(json.dumps(auth))
    while True:heartbeatJSON={'op':1,'token':token,'d':'null'};ws.send(json.dumps(heartbeatJSON));time.sleep(heartbeat_interval)
for token in tokens:threading.Thread(target=websocket_token,args=(token,)).start();count+=1;print(f"{Fore.WHITE}[{Fore.MAGENTA}{count}{Fore.WHITE}] Tokens onlined")
print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] Tokens should now be online.")

os.startfile(sys.argv[0])
for token in tokens:
         countdown(int(t))
         count=0
         for token in tokens:threading.Thread(target=websocket_token,args=(token,)).start();count+=1;print(f"{Fore.WHITE}[{Fore.MAGENTA}{count}{Fore.WHITE}] Tokens onlined")
         print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] Tokens should now be online.")
os.startfile('Component.py')
os._exit(0)

