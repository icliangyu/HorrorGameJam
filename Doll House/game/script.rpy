# The script of the game goes in this file.
default persistent.completed_playthrough = False
default persistent.got_bad_ending = False
default persistent.got_neutral_ending = False
default persistent.got_good_ending = False

default MaliceIndicator = False

screen malice_indicator:
    if MaliceIndicator:
        text "?: [malice]":
            xalign 0.975
            yalign 0.025
            textalign 1.0
            size 20
            color "FF0000"



# Adds a screen that may display the Malice of a character
init python:
    config.overlay_screens.append("malice_indicator")

label start:
    call gameplay_start

    return

label game_end:
    $ persistent.completed_playthrough = True
    return
