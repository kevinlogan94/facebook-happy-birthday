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

def check_for_browser_mac():
    search_screen_for_image("images/redxicon.png")

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
    click_all_images("images/birthday-text-area-her.png",
                     send_happy_birthday_message, get_birthday_quote)
    click_all_images("images/birthday-text-area-his.png",
                     send_happy_birthday_message, get_birthday_quote)


def send_happy_birthday_message(text):
    type_then_enter(text)
    # In case the first didn't go through.
    hit_enter_key()
