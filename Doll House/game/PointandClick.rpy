##Point and Click Screens

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
    #PointOfInterest = namedtuple('PointOfInterest', ['name', 'exposition_label', 'image_set', 'transformation', 'active'])

screen point_and_click_screen_base():
    layer 0

    transclude

screen point_of_interest_screen(PointOfInterest):
    imagebutton:
        idle PointOfInterest.image_set.base_image
        hover PointOfInterest.image_set.base_image
        selected_idle PointOfInterest.image_set.base_image
        selected_hover PointOfInterest.image_set.base_image
        if(PointOfInterest.active):
            action[ Call(PointOfInterest.exposition_label),
                    SetField(PointOfInterest, "seen", True)
                ]


    transclude

screen collectible_item_collection_screen(item_name, item_description, image_image, found_variable_name, inventory_variable_name):
    frame at truecenter:
        modal True
        vbox:
            spacing 10
            text item_name id "item_name"
            add image_image
            text _(item_description)
            hbox:
                textbutton "Collect" action[SetVariable(found_variable_name, True), SetVariable(inventory_variable_name, True), Hide("collectible_item_collection_screen")]
                textbutton "Ignore" action[SetVariable(found_variable_name, False), Hide("collectible_item_collection_screen")]

'''
    This screen is used to display a collectible item. 
    It is supposed to act like a base class for the item, values that must be
    specified will be at the end.
    # - When a player clicks on this item in the environment they have the ability
        to collect it and add it to their inventory.
    # - If a player presses the [insert accessibility input here] then it will 
        cause the item to do something to reveal itself in the environment
    Values to be specified:
    # pos
        The position of the object in the scene.
    # xysize
        The dimensions of the object you're trying to display
    # item_name

    # item_description

    #  
'''
screen collectible_item_screen_base(el_transformo, item_image_file_name, item_name, item_description):
    layer 0

    imagebutton at el_transformo:
        auto item_image_file_name+"_%s.webp"
        action ShowTransient("collectible_item_collection_screen", 
            item_name=_(item_name), 
            item_description=item_description, 
            image_image = _(item_image_file_name+"_displaying_screen.webp"),
            found_variable_name = _(""),
            inventory_variable_name = _(""))

    transclude