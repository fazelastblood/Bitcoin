from hashlib import sha256
from bitcoin import *
import random
import json
import time
from Assets import *
import threading
from Account import *
from Wallet import *

def Start():
    if login() == True:
        Menu()
    else:
        pass


def Menu():
    print(Menue)
    print("\n\n")

    input_check = input("Enter Selection>>> ")

    if input_check == "1" or  input == "one":
        print_slow(Wallet_Learn)
        input("Press Enter To Continue>>> ")
        Start_Wallet()
    elif input_check == "2" or  input == "two":
        pass
    elif input_check == "3" or  input == "three":
        pass
    elif input_check == "4" or  input == "four":
        pass
    elif input_check == "5" or  input == "five":
        pass
    elif input_check == "6" or  input == "six":
        pass
    else:
        print("Did Not Understand")

if __name__ == "__main__":
    Start()