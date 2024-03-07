##Point and Click Screens

init:
    define HighContrast = False
    transform HighContrastTransform:
        matrixcolor ContrastMatrix(10.0)
    transform NormalContrastTransform:
        matrixcolor ContrastMatrix(1.0)

init python:
    class PointOfInterestImageSet:
        def __init__(self, base_image: str, hover_image: str = "", selected_idle_image: str = "", selected_hover_image: str = ""):
            self.base_image = base_image
            self.hover_image = hover_image if hover_image != "" else base_image
            self.selected_idle_image = selected_idle_image if selected_idle_image != "" else base_image
            self.selected_idle_image = selected_hover_image if selected_hover_image != "" else base_image

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
    for pointOfInterest in PointsOfInterest:
        use point_of_interest_screen(pointOfInterest)
    vbox:
        textbutton ("\u00d8" if HighContrast else "O"):
            action [ToggleVariable("HighContrast"),
                    SetVariable("AccessibilityTransform", (HighContrastTransform if not HighContrast else NormalContrastTransform)) # !HighContrast because it hasn't been set yet
            ]
        if persistent.completed_playthrough or sum(pointOfInterest.seen == True for pointOfInterest in PointsOfInterest) == len(PointsOfInterest):
            frame at MakeTransformFromPicker((0,0,300,100)):
                textbutton "continue":
                    action Return()

screen point_of_interest_screen(PointOfInterest):
    imagebutton at PointOfInterest.transformation, GetAccessibilityTransform():
        idle PointOfInterest.image_set.base_image
        hover PointOfInterest.image_set.base_image
        selected_idle PointOfInterest.image_set.base_image
        selected_hover PointOfInterest.image_set.base_image
        focus_mask True
        if(PointOfInterest.active):
            action[ 
                    SetField(PointOfInterest, "seen", True),
                    SetField(PointOfInterest, "active", False), #Not inherently true if we get an inventory and such
                    Call(PointOfInterest.exposition_label, from_current=True)
                ]


    transclude

transform BasePACTransform: 
    BackgroundScale