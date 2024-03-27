##Point and Click Screens

init:
    define HighContrast = False
    transform HighContrastTransform:
        matrixcolor ContrastMatrix(10.0)
    transform NormalContrastTransform:
        matrixcolor ContrastMatrix(1.0)

init python:
    class PointOfInterestImageSet:
        def __init__(self, base_image: str):
            self.idle_image = base_image+"_Idle.png"
            self.hover_image = base_image+"_Hover.png"

    class PointOfInterest:
        def __init__(self, name: str, exposition_label: str, image_set: store.PointOfInterestImageSet, transformation):
            self.name = name
            self.image_set : store.PointOfInterestImageSet = image_set
            self.exposition_label = exposition_label
            self.transformation = transformation
            self.active = True
            self.seen = False

    def MakeTransformFromPicker(pos_size):
        return Transform(xpos = pos_size[0], ypos = pos_size[1], xsize = pos_size[2], ysize = pos_size[3])

    def GetAccessibilityTransform():
        if HighContrast:
            return HighContrastTransform
        else:
            return NormalContrastTransform
    #PointOfInterest = namedtuple('PointOfInterest', ['name', 'exposition_label', 'image_set', 'transformation', 'active'])

screen point_and_click_screen(PointsOfInterest):
    zorder -1
    for pointOfInterest in PointsOfInterest:
        use point_of_interest_screen(pointOfInterest)
    if False and persistent.completed_playthrough or sum(pointOfInterest.seen == True for pointOfInterest in PointsOfInterest) == len(PointsOfInterest):
        frame at MakeTransformFromPicker((0,0,300,100)):
            textbutton "Continue":
                text_font "gui/fonts/Dollface.ttf"
                action Return()

screen point_of_interest_screen(PointOfInterest):
    imagebutton at PointOfInterest.transformation, GetAccessibilityTransform():
        idle PointOfInterest.image_set.idle_image
        hover PointOfInterest.image_set.hover_image
        selected_idle PointOfInterest.image_set.idle_image
        selected_hover PointOfInterest.image_set.hover_image
        hovered Play("sound", audio.InteractableHover)
        focus_mask True
        if(PointOfInterest.active):
            action[ 
                    SetField(PointOfInterest, "seen", True),
                    Call(PointOfInterest.exposition_label, from_current=True)
                ]

    transclude

transform BasePACTransform: 
    BackgroundScale