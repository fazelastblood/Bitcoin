from hashlib import *
from bitcoin import *
import random
import json
import time
from Assets import *
import threading
from Account import *

Loged_In = False

def Setup():
    Start = signup()
    if Start == True:
        print("Successfuly Signed Up")
        input("Press Enter To Continue>>> ")
    else:
        print("A Fatal Error Has Ocured")

if __name__ == "__main__":
    Setup()