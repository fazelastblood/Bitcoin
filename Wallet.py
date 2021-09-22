from hashlib import *
from bitcoin import *
import random
import json
import time
from Assets import *
import threading
from Account import *
import webbrowser

url = "https://www.blockchain.com/btc/address/"
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

def Start_Wallet():
    if login() == True:
        StartLearn(True)
    else:
        pass

def StartLearn(ya_na):
    if ya_na == True:
        print_slow("Now Creating A Private Key, Remember Keep This A Secret.\n This Will Get Your All Your Bitcoin.\n\n\n")
        private_key = random_key()
        print_slow("You Will Need This, If You Are Planing On Keeping The Wallet.\n")
        print(private_key + "\n\n")
        public_key = privtopub(private_key + "\n\n")
        print_slow("You Will Need This, If You Are Planing On Keeping The Wallet.\n")
        print(public_key + "\n\n")
        address = pubtoaddr(public_key)
        print_slow("You Will Need This, If You Are Planing On Keeping The Wallet.\n")
        print(address + "\n\n")
        webbrowser.open(url + address)
        f = open("./Real Wallet/Address.txt", "w")
        f.write(address)