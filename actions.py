##
# Created by Kevin Logan on 06/23/19
##

from helperFunctions import click_all_images
from helperFunctions import computerData
from helperFunctions import get_birthday_quote
from helperFunctions import hit_enter_key
from helperFunctions import hit_key_binding
from helperFunctions import move_mouse
from helperFunctions import notify
from helperFunctions import search_screen_for_image
from helperFunctions import type_on_screen
from helperFunctions import type_then_enter

# designed to simply move the mouse of the way so it doesn't interfere with anything.
def clear_mouse():
    width = computerData["screenSize"][0]
    move_mouse(width, 0)


def open_brave():
    hit_key_binding("command", "space")
    type_on_screen("Brave Browser")
    hit_enter_key()

def check_for_brave_dark_mode():
    search_screen_for_image("images/brave-bookmark-dark.png", 10)

def check_for_brave_new_tab_dark_mode():
    search_screen_for_image("images/brave-new-tab-dark.png", 10)

def open_new_tab():
    hit_key_binding("command", "t")

def close_tab():
    hit_key_binding("command", "w")


def type_in_url(text):
    hit_key_binding("command", "l")
    type_on_screen(text)
    hit_enter_key()

def notification(message, title):
    notify(message, title)


def wish_everyone_happy_birthday():
    click_all_images("images/birthday-text-area.png", send_happy_birthday_message)

def wait_for_browser_to_process_happy_birthdays():
    # may be wise to change this and have it look if there is no more focused text boxes instead.
    search_screen_for_image("images/birthday-text-area.png", 3, False)
    print("Finished wishing everyone a happy birthday.")


def send_happy_birthday_message():
    type_then_enter(get_birthday_quote())
    # In case the first didn't go through.
    hit_enter_key()
