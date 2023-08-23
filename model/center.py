#!/usr/bin/python3

import os

def center_text(text):
    screen_width = os.get_terminal_size().columns
    centered_text = text.center(screen_width)
    return centered_text