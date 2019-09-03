# Created by Kevin Logan on 6/19/19

# Script to wish happy birthdays on facebook
from actions import check_for_browser
from actions import check_for_new_tab
from actions import close_tab
from actions import notification
from actions import open_browser
from actions import clear_mouse
from actions import open_new_window
from actions import send_happy_birthday_message
from actions import type_in_url
from actions import wait_for_browser_to_process_happy_birthdays
from actions import wish_everyone_happy_birthday

import schedule
import time

def job():
    try:
        notification(
            "Your computer is being controlled by an automation script.",
            "Facebook Happy Birthday",
        )
        clear_mouse()
        open_browser()
        check_for_browser()
        open_new_window()
        check_for_new_tab()
        type_in_url("https://www.facebook.com/events/birthdays/")
        wish_everyone_happy_birthday()
        wait_for_browser_to_process_happy_birthdays()
        close_tab()
        notification("Finished!", "Facebook Happy Birthday")
    except KeyboardInterrupt:
        notification("Cancelled!", "Facebook Happy Birthday")

schedule.every().day.at("08:00").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
