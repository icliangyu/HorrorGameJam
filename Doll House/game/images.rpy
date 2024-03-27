##Doll Sprites

image nicole = "images/Characters/nicole/nicole "
image doll = "images/Characters/doll/doll "
image mom = "images/Characters/mom/mom "
image emi = "images/Characters/emi/emi "
image bg = "images/Backgrounds/bg "

init: 
    image bg_nicole_blank = "images/Backgrounds/bg nicole_end.png"
    image bg_nicole_blood = "images/Backgrounds/bg nicole_end blood.png"
    image bg_nicole_void = "images/Backgrounds/bg nicole_end void.png"
    image bg bad_ending = "images/Ending Screens/Bad Ending.png"

    image menubg bad_ending = "images/"

init:
    transform PortraitDimensions:
        xysize (-500, 500)

    transform LeftPortrait:
        pos (000, 580)
        xysize (500, 500)

    transform RightPortrait:
        pos (1920, 580)
        xysize (-500, 500)
        matrixcolor BrightnessMatrix(0.0)

    transform TertiaryRightPortrait:
        pos (2120, 580)
        xysize (-500, 500)
        matrixcolor BrightnessMatrix(-0.50)

    transform BackgroundScale:
        pos(0,0)
        xysize(1920, 1080)
    
    transform BackgroundBlur:
        BackgroundScale
        blur 20
        