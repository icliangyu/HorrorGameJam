##Doll Sprites

image nicole = "images/Characters/nicole/nicole "
image doll = "images/Characters/doll/doll "
image mom = "images/Characters/mom/mom "
image emi = "images/Characters/emi/emi "
image bg = "images/Backgrounds/bg "


init:
    transform PortraitDimensions:
        xysize (-500, 500)

    transform LeftPortrait:
        pos (450, 555)
        xysize (-500, 500)

    transform RightPortrait:
        pos (1395, 555)
        xysize (500, 500)

    transform BackgroundScale:
        pos(0,0)
        xysize(1920, 1080)