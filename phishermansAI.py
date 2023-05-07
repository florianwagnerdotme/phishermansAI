#author: Florian Wagner
#	 Ethical Hacker and Security Researcher
#	 DISCLAIMER: This tool is intended for research purposes only and should not be used for any malicious or illegal activities. The use of this tool for any unauthorized or unethical purposes is strictly prohibited. The creators of this tool are not responsible for any damages or losses caused by the misuse of this tool. By using this tool, you agree to use it only for legitimate research purposes and to comply with all applicable laws and regulations. This work was not created in any relation to my current employer.

import openai
import sys
import itertools
import argparse
import subprocess
import datetime

toolname= '''
 ____  _     _     _                                     _          _    ___ 
|  _ \| |__ (_)___| |__   ___ _ __ _ __ ___   __ _ _ __ ( )___     / \  |_ _|
| |_) | '_ \| / __| '_ \ / _ \ '__| '_ ` _ \ / _` | '_ \|// __|   / _ \  | | 
|  __/| | | | \__ \ | | |  __/ |  | | | | | | (_| | | | | \__ \  / ___ \ | | 
|_|   |_| |_|_|___/_| |_|\___|_|  |_| |_| |_|\__,_|_| |_| |___/ /_/   \_\___|
by Florian Wagner
'''

print(toolname)
print("Please wait while we prepare the bait, we don't want to give the fish any reason to carp about our service!\n")
openai.api_key = ""

parser = argparse.ArgumentParser()
parser.add_argument("--mwords", type=int, default=200, help="the number of words to use from the word scraping (default=200)")
parser.add_argument("--name", type=str, default="John Smith", help="put in a name to target in the mail (default=John Smith)")
parser.add_argument("--compname", type=str, default="Test Phishing LTD", help="put in a company name to target in the mail (default=Test Phishing LTD)")
parser.add_argument("--link", type=str, default="https://foobar.zyx", help="give a phishing link that will be displayed for the user to click on (default=https://foobar.zyx)")
parser.add_argument("--target", type=str, default="https://florianwagner.me", help="insert a target company website to create a phishing mail for (default=florianwagner.me)")
args = parser.parse_args()

now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
file_path="wordlist"+timestamp+".txt"

targetURL=args.target
subprocess.run(["cewl", "-d 2", "-m 5", "-w", file_path, targetURL], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

with open(file_path, 'r') as file:
    words = [line.strip() for line in file.readlines()][:args.mwords]

prompt_string = f"Write a personalised, logical and unsolicited email from a company to one of its employees. It should be no longer than 250 words. The email is urgent and needs to be resolved as soon as possible to avoid problems. Try to use promotional strategies to get the user to click on the link. Do not advertise or assume that the user will later use the products given to you as words. Check all words for validity against a dictionary and create an email based on the remaining words. Give a creative incentive to click on the link. Try to guess what the company's business is and what products it offers, and use this information. You do not have to use all of the words given."
comp_name = "The company is called and the sender of the mail is identified with: "+args.compname+". "
target_name = "The email recipient's name is: "+args.name+". "
prompt_string2 = "Here are the words to use for the email text, seperated by comma: "+', '.join(words)+". "
addlink="This is the link that you want the user to click on, so place it in a good position in relation to the body of the email: "+args.link+". "

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":prompt_string + target_name + comp_name + addlink + prompt_string2}])
print(completion.choices[0].message.content)
