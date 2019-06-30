# Created by Kevin Logan on 6/19/19

# Script to wish happy birthdays on facebook
from actions import check_for_browser_mac
from actions import close_tab
from actions import notification
from actions import open_brave
from actions import open_new_tab
from actions import type_in_url
from actions import clear_mouse
from actions import wish_everyone_happy_birthday
from actions import send_happy_birthday_message

try:
    notification("Your computer is being controlled by an automation script.","Facebook Happy Birthday")
    clear_mouse()
    open_brave()
    check_for_browser_mac()
    open_new_tab()
    type_in_url("https://www.facebook.com/events/birthdays/")
    notification("Writing your happy birthday messages.","Facebook Happy Birthday")
    wish_everyone_happy_birthday()
    close_tab()
    notification("Finished!","Facebook Happy Birthday")
except KeyboardInterrupt:
    notification("Cancelled!","Facebook Happy Birthday")
