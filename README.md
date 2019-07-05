# facebook-happy-birthday

An Automation script designed to wish your friends a happy birthday on Facebook.

This script uses [pyAutoGui](https://pyautogui.readthedocs.io/en/latest/introduction.html) to take advantage of your computers Accessibility tools.

### Demo

Coming soon...

### Requirements:

- Python3

## Mac Setup

1. Clone the project

```
git clone https://github.com/kevinlogan94/facebook-happy-birthday.git
```

2. cd into your new project folder.

```
cd facebook-happy-birthday
```

3. Install the required dependencies
> I recommend using python virtual environments. You don't have to but highly recommend if you are planning on having multiple Python projects on your machine. 

```
pip3 install -r requirements.txt
```

## This script makes the following assumptions

- You have the Brave Browser downloaded and set to dark mode
- You're using a Mac
- You have already logged into Facebook

## Trigger the script

```
pip3 /path/to/facebook-happy-birthday/index.py
```

> Note: You will probably get a notification asking for you to give your terminal permission to use your accessibility tools. Approve this otherwise this script won't work.