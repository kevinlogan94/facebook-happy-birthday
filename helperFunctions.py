# Created by Kevin Logan on 6/19/19

# functions to import into other files.
import pyautogui
import subprocess
import time

def click_all_images(png_name, callback=None, callback_arg=None):
    search_screen_for_image(png_name)
    for location in list(pyautogui.locateAllOnScreen(png_name)):
        image = pyautogui.center(location)
        x = image[0]
        y = image[1]
        # Check for a retina screen
        if computerData["RetinaScreen"]:
            x = x / 2
            y = y / 2
        pyautogui.moveTo(x, y)
        pyautogui.click()
        # pyautogui.click()
        if callback != None and callback_arg != None:
            callback(callback_arg)

def click_image(png_name):
    # In case, a page is loading...
    search_screen_for_image(png_name)

    image = pyautogui.locateCenterOnScreen(png_name)
    x = image[0]
    y = image[1]
    # Check for a retina screen
    if computerData["RetinaScreen"]:
        x = x / 2
        y = y / 2
    pyautogui.moveTo(x, y)
    pyautogui.click()
    # pyautogui.click()
    print("Clicked {0}".format(png_name))


def search_screen_for_image(png_name):
    location = None
    timeout = time.time() + 10   # 10 seconds from now
    print("Searching for " + png_name)
    while location == None:
        time.sleep(0.25)  # set a delay so this doesn't hog cpu
        location = pyautogui.locateOnScreen(png_name)
        # Kill this if it takes more than 10 seconds
        if time.time() > timeout:
            location = "Finish"
            print("Couldn't find " + png_name + " in 10 seconds")


def type_on_screen(text):
    pyautogui.typewrite(text)


def hit_enter_key():
    pyautogui.press('enter')

def move_mouse(xcoord, ycoord):
    pyautogui.moveTo(xcoord,ycoord)

def type_then_enter(text):
    type_on_screen(text)
    hit_enter_key()


def hit_key_binding(*keys):
    key_length = len(keys)
    if key_length == 3:
        pyautogui.hotkey(keys[0], keys[1], keys[2])
    elif key_length == 2:
        pyautogui.hotkey(keys[0], keys[1])
    elif key_length == 1:
        pyautogui.hotkey(keys[0])
    else:
        print("You didn't enter any keys.")

# Prints out what you want but keeps the content on  the same line.
def print_same_line(text):
    # Print it out but don't add the newline at the end.
    print(text, end='')
    # Remove the old printed location.
    print('\b' * len(text), end='', flush=True)

# Consider moving this to a different file.
def extractComputerData():
    print("Let me grab a few details from your computer...")
    RetinaScreen = False
    # https://medium.com/@tracy_blog/pyautogui-and-retina-displays-2d5c37a5aa5e
    if subprocess.call("system_profiler SPDisplaysDataType | grep Retina", shell=True) == 0:
        RetinaScreen = True
    data = {
        "RetinaScreen": RetinaScreen,
        "screenSize": pyautogui.size()
    }
    print("Done!")
    return data

# Global
computerData = extractComputerData()
