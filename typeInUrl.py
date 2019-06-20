# Created by Kevin Logan on 6/19/19

from helperFunctions import hit_enter_key, type_on_screen, hit_key_binding

# This is assuming you are already focusing the url bar
def type_in_url(text):
    hit_key_binding("command", "l")
    type_on_screen(text)
    hit_enter_key()