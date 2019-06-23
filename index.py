# Created by Kevin Logan on 6/19/19

# Script to wish happy birthdays on facebook
from actions import open_brave
from actions import open_new_tab
from actions import type_in_url
from actions import clear_mouse
from actions import wish_everyone_happy_birthday
from actions import send_happy_birthday_message

try:
    clear_mouse()
    open_brave()
    open_new_tab()
    type_in_url("https://www.facebook.com/events/birthdays/")
    wish_everyone_happy_birthday()
    print("Finished!")
except KeyboardInterrupt:
    print("Cancelled!")
