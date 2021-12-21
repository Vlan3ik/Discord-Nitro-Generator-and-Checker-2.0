

webhook = "https://discord.com/api/webhooks/webhook" #You webhook


import ctypes
import string
import os
import time
from discord_webhook import DiscordWebhook
import requests
import numpy

# Create by VLAN#9796
url = "https://github.com"
response = requests.get(url)
DiscordWebhook(url=webhook,content=f"```Start```").execute()

def quickChecker(self, nitro:str, notify=None):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    if response.status_code == 200:
        print(f" Valid | {nitro} ")
        DiscordWebhook(url=webhook,content=f"Valid Nito Code ! @everyone \n{nitro}").execute() # webhook say if Valid Nito
        return True


valid = []
invalid = 0
chars = []
chars[:0] = string.ascii_letters + string.digits
sch = 0
print("start")
while True:
    c = numpy.random.choice(chars, size=[1000, 19])
    for s in c:
        try:
            code = ''.join(x for x in s)
            url = f"https://discord.gift/{code}"
            result = quickChecker(url, webhook)
            if result:
                valid.append(url)
            else:
                invalid += 1
                sch += 1
                print(f" invalid | {invalid}")
                if sch == 10000: #  invalid | 10000 , invalid | 20000
                    DiscordWebhook(url=webhook,content=f"```invalid | {invalid}```").execute()
                    sch = 0
        except KeyboardInterrupt:
            print("\nInterrupted by user")
            break