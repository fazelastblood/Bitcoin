from hashlib import sha256
from bitcoin import *
import random
import json
import time
from Assets import *
import threading
from Account import *
import getpass
from Setup import *



def signup():
    X = getpass.getpass("Please Enter A Secure Password>>> ")
    X_verify = getpass.getpass("Re-Enter Password>>> ")
    if str(X_verify) == str(X) and X.__len__() >= 8:
        encryption = hashlib.sha256(X.encode("utf-8")).hexdigest()
        set = open("./Dont_Touch/Key.txt", "a")
        set.write(encryption)
        set.close()
        print("This Will Now Create Files To Store Your Information,\n There Is No Creating A new PassWord If You Forget You Forget.")
        return True
    else:
        print("Incorrect")
        return False

def login():
    x = getpass.getpass("Please Enter Your Password>>> ")
    set = open("./Dont_Touch/Key.txt", "r")
    read = set.read()
    set.close()
    encrypt = hashlib.sha256(x.encode("utf-8")).hexdigest() 
    if encrypt == read:
        return True
    else:
        return False