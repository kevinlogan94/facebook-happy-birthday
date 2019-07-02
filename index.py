# Created by Kevin Logan on 6/19/19

# Script to wish happy birthdays on facebook
from actions import check_for_brave_dark_mode
from actions import check_for_brave_new_tab_dark_mode
from actions import close_tab
from actions import notification
from actions import open_brave
from actions import open_new_tab
from actions import type_in_url
from actions import clear_mouse
from actions import wait_for_browser_to_process_happy_birthdays
from actions import wish_everyone_happy_birthday
from actions import send_happy_birthday_message

try:
    notification("Your computer is being controlled by an automation script.","Facebook Happy Birthday")
    clear_mouse()
    open_brave()
    check_for_brave_dark_mode()
    open_new_tab()
    check_for_brave_new_tab_dark_mode()
    type_in_url("https://www.facebook.com/events/birthdays/")
    wish_everyone_happy_birthday()
    wait_for_browser_to_process_happy_birthdays()
    close_tab()
    notification("Finished!","Facebook Happy Birthday")
except KeyboardInterrupt:
    notification("Cancelled!","Facebook Happy Birthday")
