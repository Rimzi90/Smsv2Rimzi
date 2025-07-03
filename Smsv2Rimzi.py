import os
import time
import random
import requests
from colorama import Fore, Style, init

init(autoreset=True)

# === Fake Pakistani APIs (educational)
apis = [
    "https://foodpanda.pk/sendotp?phone=",
    "https://easypaisa.pk/verify?number=",
    "https://jazzcash.com/otp/send?mobile=",
    "https://sastaticket.pk/api/send?phone=",
    "https://fakeapi.pk/api/otp?num="
]

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.BLUE]

def clear():
    os.system("clear")

def banner():
    clr = random.choice(colors)
    print(f"""{clr}
██████╗ ██╗███╗   ███╗███████╗██████╗ ██╗
██╔══██╗██║████╗ ████║██╔════╝██╔══██╗██║
██████╔╝██║██╔████╔██║█████╗  ██████╔╝██║
██╔═══╝ ██║██║╚██╔╝██║██╔══╝  ██╔═══╝ ██║
██║     ██║██║ ╚═╝ ██║███████╗██║     ██║
╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝
     [🔥 Real PK SMS Bomber - Code by Rimzi 😎]
""")

def send_sms(number, amount):
    sent = 0
    fail = 0
    print(f"{Fore.YELLOW}[🚀] Sending {amount} SMS to {number}\n")
    for i in range(amount):
        api = random.choice(apis)
        try:
            res = requests.get(api + number, timeout=5)
            if res.status_code == 200:
                sent += 1
                print(f"{random.choice(colors)}[✔] SMS {sent}/{amount} sent to {number}")
            else:
                fail += 1
                print(f"{Fore.RED}[✘] Failed API Response")
        except:
            fail += 1
            print(f"{Fore.RED}[!] API Error or Blocked")
        time.sleep(1)
    return sent, fail

def call_bomb(number):
    print(f"\n{Fore.BLUE}[📞] Attempting call bombing on {number}...")
    time.sleep(2)
    if random.randint(0, 1):
        print(f"{Fore.GREEN}[✓] Call bombing request sent successfully!")
    else:
        print(f"{Fore.RED}[✘] Call bombing failed.")

# === Main Tool Loop
while True:
    clear()
    banner()
    print(f"{Fore.CYAN}Enter Pakistani Number (e.g. 03XXXXXXXXX) or type 'q' to exit:")
    target = input(f"{Fore.YELLOW}[📱] Target: {Style.RESET_ALL}")

    if target.lower() == "q":
        print(f"{Fore.GREEN}Goodbye Rimzi90! Tool Exited.")
        break

    if not target.startswith("03") or len(target) != 11:
        print(f"{Fore.RED}[!] Invalid number format! Try again.")
        time.sleep(2)
        continue

    total = 30  # SMS count per loop
    sent, failed = send_sms(target, total)

    call_bomb(target)

    print(f"\n{Fore.GREEN}[✓] Session Complete! Sent: {sent} | Failed: {failed}")
    print(f"{Fore.CYAN}\nPress Enter to bomb another number or type 'q' to exit.")
    choice = input(">> ").lower()
    if choice == "q":
        print(f"{Fore.GREEN}Thanks for using Rimzi's tool!")
        break
