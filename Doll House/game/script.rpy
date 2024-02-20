# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nadeshiko", image="nadeshiko")


# The game starts here.

label start:


    scene bg_attic

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

    n neutral "Where am I?"

    n "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
