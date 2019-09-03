##
# Created by Kevin Logan on 06/23/19
##

from helperFunctions import click_all_images
from helperFunctions import click_image
from helperFunctions import computerData
from helperFunctions import get_birthday_quote
from helperFunctions import hit_enter_key
from helperFunctions import hit_key_binding
from helperFunctions import move_mouse
from helperFunctions import notify
from helperFunctions import search_screen_for_image
from helperFunctions import type_on_screen
from helperFunctions import type_then_enter
from helperFunctions import wait_for_image_to_vanish

# designed to simply move the mouse of the way so it doesn't interfere with anything.
def clear_mouse():
    width = computerData["screenSize"][0]
    move_mouse(width, 0)


def open_brave():
    hit_key_binding("command", "space")
    type_on_screen("Brave Browser")
    hit_enter_key()


def open_browser():
    if computerData["OS"] == "Darwin":
        open_brave()
    else:
        open_chromium()


def open_chromium():
    click_image("images/raspian/browser.png")


def check_for_brave_dark_mode():
    search_screen_for_image("images/brave-bookmark-dark.png", 10)


def check_for_chromium():
    search_screen_for_image("images/raspian/chromium-bookmark.png", 10)


def check_for_browser():
    if computerData["OS"] == "Darwin":
        check_for_brave_dark_mode()
    else:
        search_screen_for_image("images/raspian/chromium-bookmark.png", 10)


def check_for_brave_new_tab_dark_mode():
    search_screen_for_image("images/brave-new-tab-dark.png", 10)


def check_for_chromium_new_tab():
    search_screen_for_image("images/raspian/chromium-tab.png", 10)


def check_for_new_tab():
    if computerData["OS"] == "Darwin":
        check_for_brave_new_tab_dark_mode()
    else:
        check_for_chromium_new_tab()


def open_new_window():
    hit_key_binding("command", "n")


def close_tab():
    hit_key_binding("command", "w")


def type_in_url(text):
    hit_key_binding("command", "l")
    type_on_screen(text)
    hit_enter_key()


def notification(message, title):
    if computerData["OS"] == "Darwin":
        notify(message, title)
    else:
        print(title + ": " + message)


def wish_everyone_happy_birthday():
    click_all_images("images/birthday-text-area.png", send_happy_birthday_message)


def wait_for_browser_to_process_happy_birthdays():
    wait_for_image_to_vanish("images/focused-text-area-bottom.png")
    print("Finished wishing everyone a happy birthday.")


def send_happy_birthday_message():
    type_then_enter(get_birthday_quote())
    # In case the first didn't go through.
    hit_enter_key()
