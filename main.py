import requests
import json
from colorama import Fore

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = input(f"{Fore.BLUE}Insert text: {Fore.RESET}\n>")

if(data==""):
    print("Please enter something in the input.")
else:
    d = requests.get(f"https://openai-openai-detector.hf.space/?data", headers=headers)
    o = json.loads(d.text)
    real = o['real_probability']
    fake = o['fake_probability']
    
    if(real > fake):
        print(f"\n{Fore.GREEN}The input text is detected as written by a human.{Fore.RESET}")
    else :
        print(f"\n{Fore.RED}The input text is detected as written by an AI (ChatGPT). {Fore.RESET}")

