# Created by Kevin Logan on 6/19/19

# Script to wish happy birthdays on facebook
from helperFunctions import click_image, type_on_screen, hit_enter_key, hit_key_binding, click_all_images, type_then_enter
from openBrave import open_brave
from openNewTab import open_new_tab
from typeInUrl import type_in_url

def wish_everyone_happy_birthday():
    click_all_images("images/birthday-text-area-her.png", send_happy_birthday_message)
    click_all_images("images/birthday-text-area-his.png", send_happy_birthday_message)

def send_happy_birthday_message():
    type_then_enter("Happy Birthday! I hope it's one for the books!")

open_brave()
open_new_tab()
type_in_url("https://www.facebook.com/events/birthdays/")
wish_everyone_happy_birthday()
print("Finished!")
