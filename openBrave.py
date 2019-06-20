# Created by Kevin Logan on 6/19/19

from helperFunctions import hit_key_binding, hit_enter_key, type_on_screen

def open_brave():
    hit_key_binding("command", "space")
    type_on_screen("Brave Browser")
    hit_enter_key()