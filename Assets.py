import sys
import time
import hashlib

Menue = (
    "1: Wallet\n"
    "2: Logout"
)
x = hashlib.sha256("Matt".encode("utf-8")).hexdigest()

Wallet_Learn = (
    "So, You Want To Start Learning About Bitcoin?\n"
    "Starting With Wallets Was Good Choice, A Wallet Is\n"
    "A Place To Hold All Your Riches... Well Bitcoin.\n"
    "There Are 3 Part's To A Wallet, 1: Private Key, \n"
    "2: Public Key, 3: Wallet Address.  Lets Start With\n"
    "The Private Key, A private Key Is A Randomly Genirated\n"
    "Encryption Key, Just Think Of A Private Key As A 64 Digit Random Hash Wich Looks Like           |\n"
    "" + x + "                             <-/\n"
    "The Private Key Generates A So Called PublicKey.\n"
    "If You Are Familiyer With Public Key Cryptography This Is Called,\n"
    "A Hash. If You Mix The Public And Private Key, You Get A WALLET ADRESS.\n"
    "The Wallet Address and Public Key Is How People Send Bitcoin To You\n"
    "Lets Get Started...\n"
    "\n"
    "\n"
    "\n"
)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)

print(Wallet_Learn)