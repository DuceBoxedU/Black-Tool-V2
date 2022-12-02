import random, httpx

httpx.post(f"https://discord.com/api/v9/guilds/{guild}/roles",headers = {"authorization":f"Bot {TOKEN}"},json = {'name':ROLE_SPAM,"color":random.randint(0,0xffffff)})