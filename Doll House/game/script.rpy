# The script of the game goes in this file.
default persistent.completed_playthrough = False
default persistent.got_bad_ending = False
default persistent.got_neutral_ending = False
default persistent.got_good_ending = False

label start:
    call gameplay_start

    return

label game_end:
    $ persistent.completed_playthrough = True
    return
