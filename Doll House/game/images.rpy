##Doll Sprites

image nicole = "images/Characters/nicole/nicole "
image doll = "images/Characters/doll/doll "
image mom = "images/Characters/mom/mom "
image emi = "images/Characters/emi/emi "
image bg = "images/Backgrounds/bg "

init: 
    image bg_nicole = "nicole fear cut in"

init:
    transform PortraitDimensions:
        xysize (-500, 500)

    transform LeftPortrait:
        pos (500, 580)
        xysize (-500, 500)

    transform RightPortrait:
        pos (1320, 580)
        xysize (500, 500)

    transform BackgroundScale:
        pos(0,0)
        xysize(1920, 1080)