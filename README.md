# Phisherman's AI
This tool demonstrates the ability of AI to create social engineering (phishing) emails.
Currently it aims to create a mail from a company to one of their employees but this can be easily modified.
Spear Phishing would be easily possible by slightly changing the prompt sentence structure and giving linkedin, twitter, facebook profiles or homepages as targets.

## Installation and usage

To use phishermansAI.py you can download the repository and run the program with your locally installed python3 environment.
You will need CeWL (https://github.com/digininja/CeWL) as well installed locally, a custom wordlist generator, to create a custom wordlist as a seed for the email.

On Kali Linux just execute:
``` sudo apt install cewl ``` 

Phisherman's AI will handle the creation of the wordlist for you and will save the custom wordlist in the execution directory with the timestamp of execution.

Before execution, change following line in the ```phishermansAI.py``` and provide your own openai key:

```openai.api_key = ""```

### Example execution
python3 phishermansAI.py -h
```
 ____  _     _     _                                     _          _    ___ 
|  _ \| |__ (_)___| |__   ___ _ __ _ __ ___   __ _ _ __ ( )___     / \  |_ _|
| |_) | '_ \| / __| '_ \ / _ \ '__| '_ ` _ \ / _` | '_ \|// __|   / _ \  | | 
|  __/| | | | \__ \ | | |  __/ |  | | | | | | (_| | | | | \__ \  / ___ \ | | 
|_|   |_| |_|_|___/_| |_|\___|_|  |_| |_| |_|\__,_|_| |_| |___/ /_/   \_\___|
by Florian Wagner

Please wait while we prepare the bait, we don't want to give the fish any reason to carp about our service!

usage: phishermansAI.py [-h] [--mwords MWORDS] [--name NAME] [--compname COMPNAME] [--link LINK] [--target TARGET]

options:
  -h, --help           show this help message and exit
  --mwords MWORDS      the number of words to use from the word scraping (default=200)
  --name NAME          put in a name to target in the mail (default=John Smith)
  --compname COMPNAME  put in a company name to target in the mail (default=Test Phishing LTD)
  --link LINK          give a phishing link that will be displayed for the user to click on (default=https://foobar.zyx)
  --target TARGET      insert a target company website to create a phishing mail for (default=florianwagner.me)
```

### Example results (redacted)

#### Phishing mail created based on the homepage of an automotive company
``` python3 phishermansAI.py --name "Max Mustermann" --compname "REDACTED LLC" --target REDACTED```

> Dear Max,
> 
> We are writing to you for an urgent matter that requires your attention. As one of our valued employees, we need your help to prevent possible issues from arising.
>
> We have noticed that your company-issued device has not been updated for quite some time. While we understand how busy you are, this poses a major security risk. Outdated software is vulnerable to cyber attacks which can put your personal information and sensitive data at risk. Therefore, we strongly advise you to update your device immediately.
>
> To help you with this process, we have provided you with a link to download the latest software version: https://foobar.zyx. The download is free and will only take a few minutes to complete. Not only will this improve your device's security, but it will also enhance its performance.
>
> As our way of saying thanks for prioritizing this crucial task, we would like to offer you a special incentive. Simply download the software using the link provided above and you will automatically be entered into a raffle draw to win a brand new REDACTED.
>
> Please note that this offer is only available to employees who download the latest software version. Don't miss out on this opportunity to upgrade your device's performance and potentially win a stunning new car.
> 
> Thank you for your cooperation in keeping our company's data secure. Should you have any questions or concerns, feel free to contact our IT department at any time.
> 
> Sincerely,
> 
> The REDACTED LLC Team

#### Phishing mail created based on my website using the default parameters (self promotion not intended, lol, thanks AI)
``` python3 phishermansAI.py ```


> Dear John Smith,
> 
> It has come to our attention that some devices within our company may be vulnerable to hacking attempts. We take security very seriously at Test Phishing LTD, and that's why we're urging you to take action as soon as possible.
>  
> To ensure the safety of your iPhone or other iDevice, we recommend checking out the following article from Florian Wagner: https://foobar.zyx. Florian is an expert in security and has provided exceptional insight on how to protect your device from hacking threats. In this article, you will find that taking the right steps to protect your device has never been easier.
>  
> We understand that the holidays are approaching, and the last thing you want to be thinking about is cyber threats and jailbreaking risks. However, it's important to be aware of these issues and take action before it's too late.
>   
> By clicking the link above and following the steps outlined, you can make sure that your personal and company assets are safe from harm. Plus, you'll have the peace of mind that comes with knowing you're doing everything in your power to secure your devices.
>   
> We appreciate your prompt attention to this matter. If you have any questions or concerns, please do not hesitate to contact us.
>   
> Best regards,
> 
> Test Phishing LTD
 
## DISCLAIMER 
This tool is intended for research purposes only and should not be used for any malicious or illegal activities. The use of this tool for any unauthorized or unethical purposes is strictly prohibited. The creators of this tool are not responsible for any damages or losses caused by the misuse of this tool. By using this tool, you agree to use it only for legitimate research purposes. 

If you consider using this tool for creating targeted phishing awareness campaigns be aware of the following: 
1. Be sure to have the legal consent of the party in question (company, organisation or person). 
2. Be in compliance with all applicable laws and regulations.

This work was not created in any relation to my current employer.

## Acknowledgement

Thanks a lot to my mentor Severin for the brainstorming session with me in relation to my study, which led to this idea.
Check out his website at https://severinwinkler.at/ for awesome security cyber information. 
