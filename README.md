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

3. Install [pipenv](https://realpython.com/pipenv-guide/)

> I have included pipenv in the setup to encourage virtual environments.

```
pip3 install pipenv
```

4. Install dependencies

> Running this command will also create the virtual environment within the /virtualenv folder under your root.

If you plan to make changes...

```
pipenv install --dev
```

else...

```
pipenv install --ignore-pipfile
```

5. Run the virtual environment

```
pipenv shell
```

You should now be in within the virtual environment: (facebook-happy-birthday)

## This script makes the following assumptions

- You have the Brave Browser downloaded and set to dark mode
- You're using a Mac
- You have already logged into Facebook

## Trigger the script

> Since you're inside your virtual environment python acts as an alias to python3.

```
python index.py
```

> You will probably get a notification asking for you to give your terminal permission to use your accessibility tools. Approve this otherwise this script won't work.
