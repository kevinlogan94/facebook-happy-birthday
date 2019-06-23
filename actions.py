##
# Created by Kevin Logan on 06/23/19
##

from helperFunctions import click_all_images
from helperFunctions import computerData
from helperFunctions import move_mouse
from helperFunctions import hit_enter_key
from helperFunctions import hit_key_binding
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


def open_new_tab():
    hit_key_binding("command", "t")


def type_in_url(text):
    hit_key_binding("command", "l")
    type_on_screen(text)
    hit_enter_key()


def wish_everyone_happy_birthday(text):
    click_all_images("images/birthday-text-area-her.png",
                     send_happy_birthday_message, text)
    click_all_images("images/birthday-text-area-his.png",
                     send_happy_birthday_message, text)


def send_happy_birthday_message(text):
    type_then_enter(text)
