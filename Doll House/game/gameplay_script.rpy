# Labels and naming of assets are just placeholders
define nicole = Character("Nicole") 
define doll = Character("Doll")
define mom = Character("Mom")
define emi = Character("Emi")


# How evil you are >:3
define malice = 0 

label gameplay_start:
    scene bg_black
    nicole "Let's see what you look like..."
    # need SFX of rustling sound of boxes here
    
    scene bg_white
    show nicole surprised at RightPortrait
    nicole "What?"
    nicole "This isn't the doll I ordered..."
    show nicole angry

    # cue leitmotif for the player's introduction to the doll!
    show doll neutral at LeftPortrait

    menu unboxing:
        "How should I greet my new owner?"

        "Smile":
            $ malice += 1
            # SFX for +1 malice point
            # player should also have a visual indicator of +1 point
            show doll happy
            show nicole surprised
            nicole "Huh... you are pretty cute though, maybe I'll keep you around."
            nicole "I've seen a lot of detailed ball-jointed dolls but you're something else."
            nicole "Life like, even..."

        "...":
            show doll neutral
            show nicole neutral
            nicole "*Sigh* Whatever, this is fine too. I'm too lazy to request a return from the seller."

label bedroom:
    scene bg bedroom at BackgroundScale
    # point and click gameplay begins
    # a lot of exposition will happen through item interaction
    # image button coding action will be configured to jump("label_whatever_item_is_clicked_on")
    mom "Nick! Come down here and watch the house. I'm going to buy groceries!"
    nicole "*Sigh*"
    mom "Now!" 
    nicole "Ugh! Okay fine!"
    nicole "Couldn't just call Emi? Why is it always me?"
    nicole "Hmm... where to hide you so that rascal doesn't find you...?"
    nicole "Under the bed should do for now." 
    # SFX was storing box away
    # SFX of door slamming
    play sound Footsteps
    # SFX of footsteps stomping downstairs

    #### narration and dialogue portion not sure what to call it
    doll "So this must be my home and that was my new owner."
    doll "A bit on the older side to be playing with dolls. I'm used to much younger owners but I suppose this is fine too."

    narrator "I crawled out from underneath the bed and took in the room before me."
    narrator "It wasn't particularly big but it did have character."

    #will insert more descriptions once BGs are finalized

    narrator "Now that I was finally introduced to my new home it would be best to look around."

    show doll happy at LeftPortrait
    doll "Don't mind if I do hehe!"

    jump bedroom.point_and_click

    label .papers_exposition:
        doll "What's this?"
        doll ""
        return
    
    label .closet_exposition:
        doll "What is all of this?"
        doll "Is this really what she wears on the daily?"
        doll "This style really doesn't suit me at all but it's nothing that can't be changed."
        doll "Nicole, why are you dressing yourself up in such masculine clothes?"
        return 
    
    label .diary_exposition:
        doll "A diary?" 
        doll "She doesn't seem like the type of girl who would write about her feelings and lock them away in a secret book."
        doll "I am quite curious though..."
        doll "Oh Nicole, what are you hiding within these pages."

        nicole "Sunday XX, 20XX"
        nicole "Mom tried to set me up with one of her friend's son- again." 
        nicole "How many times have I told her I'm not interested?"
        nicole "Probably a thousand."
        nicole "How many times have I told her I'm not interested men?"
        nicole "I'll get around to it."
        return

    label .point_and_click:
        transform closet_transform: 
            BasePACTransform
        transform diary_transform: 
            BasePACTransform
        transform papers_transform: 
            BasePACTransform
        init 1:
            define BedroomPAC_POI = [
                PointOfInterest("Closet", "bedroom.closet_exposition", PointOfInterestImageSet("images/environment/closet/Closet_Hover.png"), closet_transform),
                PointOfInterest("Diary", "bedroom.diary_exposition", PointOfInterestImageSet("images/environment/diary/Diary_Hover.png"), diary_transform),
                PointOfInterest("Papers", "bedroom.papers_exposition", PointOfInterestImageSet("images/environment/Papers/Papers_Hover.png"), papers_transform),
            ]

        call screen point_and_click_screen(BedroomPAC_POI)

    doll "Somebody is coming. I must hide."

    show emi neutral at RightPortrait
    emi "Hmm..." 
    # SFX of door creaking open
    emi "Did Nick get another friend?"
    emi "Now where could they be...?"
    # SFX rummaging sound or reuse SFX of storing box away
    emi "Really Nick? You should know better than to hide your pretties under the bed."
    emi "Who do we have here?"
    emi "*Gasp* She's beautiful!"
    show doll neutral at LeftPortrait
    emi "Nadeshiko, huh? Let's go downstairs."

    emi "Let's put you down here."
    emi "Wow... you're even prettier up close."

    show doll fear at LeftPortrait

    # SFX of pencil scratching on paper
    emi "Your dress is so detailed..."
    emi "And this stitching!"

    doll "Is she drawing me?"

    emi "I wish Nick wore clothes like you, that way I could wear them too."

    # This decision will have consequences!
    menu emi_question:
        "What should I do?"

        "Console Emi":
            $ malice += 1
            emi "I don't want to sound ungrateful but sometimes it's embarrassing wearing Nick's hand me downs."
            emi "Once I get a job, I'll be able to wear all the girly clothes I want."
            emi "But..."
            emi "That kind of money would be helpful to the family so I don't know..."

            doll "I could be your big sister, Emi."
            doll "Then you wouldn't have to wear those ugly clothes anymore."

            emi "I think I would like that."

        "Listen to Emi":    
            emi "I don't want to sound ungrateful but sometimes it's embarrassing wearing Nick's hand me downs."
            emi "Once I get a job, I'll be able to wear all the girly clothes I want."
            emi "But..."
            emi "That kind of money would be helpful to the family so I don't know..."

            emi "I'll just have to work extra hard so that there's enough for both."

    emi "Nick never lets me play with her dolls but I need them for reference."
    emi "They're the perfect inspiration and model for my designs."
    emi "Welp! Can't study on an empty stomach. I wonder if mom made anything."
    #SFX fridge rummaging

    #transition to point and click 

label kitchen:
    scene bg kitchen at BackgroundScale
    narrator "The younger sister brought me downstairs to the kitchen where she was doing her homework."
    narrator "The kitchen was brightly lit and..."

    emi "Let's put you down here."

    narrator "She propped me up against her pencil case and leaned in closely to look at me."
    narrator "She had the same deep brown eyes as Nicole just less tired."

    emi "Wow... you're even prettier up close."
    emi "And your name's Nadeshiko, how fitting!"

    narrator "Emi ran her fingers through my hair and straightened out my dress." 
    narrator "I found these actions particularly endearing and felt exictement at the prospect of being a part of the family."
    narrator "Of course, I had to keep my excitement to myself but I wished to someday share it with Emi."
    narrator "She continued to study my garments with a keen eye and occasionally muttered to herself."

    emi "Your dress is so detailed and the stitching!"
    emi "I want to get this down on paper."

    narrator "She picked up the pencil lying in the middle of her notebook and began to scrawl around the corners of her page, avoiding the math formulas."
    narrator "It wasn't long before my likeness began to appear on the white pages."
    narrator "Was she drawing... me?"

    narrator "There I was, in perfect likeness, in her notebook modelling different designs and patterns." 
    narrator "For a young girl to take inspiration from me and quickly create something before my eyes... it was amazing."
    narrator "A sense of embarrassment and flattery overwhelmed me as I sat still and looked on at the prodigy." 
    narrator "Nicole didn't seem to harbour any skills or hobbies other than collecting dolls."
    narrator "I think I like Emi."

    emi "I wish Nick wore clothes like you, that way I could wear them too."

    menu .emi_question:
        "What should I do?"

        "Console Emi":
            $ malice += 1
            emi "I don't want to sound ungrateful but sometimes it's embarrassing wearing Nick's hand me downs."
            emi "Once I get a job, I'll be able to wear all the girly clothes I want."
            emi "But..."
            emi "That kind of money would be helpful to the family so I don't know..."

            narrator "Emi's downcasted face continued to glance between me and the page as she sketched."
            narrator "Even though we had just met, I didn't like seeing her sad."
            narrator "So I decided to speak up."

            doll "I could be your big sister, Emi."
            doll "Then you wouldn't have to wear those ugly clothes anymore."

            narrator "Emi looked up from her work. Her eyes searched mine for a moment before replying with a wide smile."

            emi "I think I would like that."

        "Listen to Emi":
            emi "I don't want to sound ungrateful but sometimes it's embarrassing wearing Nick's hand me downs."
            emi "Once I get a job, I'll be able to wear all the girly clothes I want."
            emi "But..."
            emi "That kind of money would be helpful to the family so I don't know..."

            narrator "As much as I wanted to, it wouldn't be wise to risk doing anything that would startle Emi." 
            narrator "So I remained silent and listened to her talk as she drew."

            emi "I'll just have to work extra hard so that there's enough for both."

    emi "Nick never lets me play with her dolls because she thinks I'll ruin them but I need them for reference."
    "They're the perfect inspiration and model for my designs."

    narrator "As long as Emi had me there wouldn't be any need for Nicole's other dolls." 
    narrator "I was enough." 

    narrator "Suddenly a low rumbling sound came from Emi as she shot up from her seat and over to the fridge."

    emi "Welp! Can't study on an empty stomach. I wonder if mom made anything."
    emi "Aww... there's nothing to eat. Cup noodles it is!"

    narrator "I almost let out a giggle at the sight of Emi frantically rummaging through the fridge and cabinets in search of food."
    narrator "She had a lot of life in her that drew me to her, unlike Nicole."
    narrator "While Emi made her food, I took this time to look around the kitchen."

    jump kitchen.point_and_click

    label .ramune_exposition:
        doll "These drinks are quite popular with young ones these days."
        doll "The liquid inside is so bright and colourful."
        doll "I wonder how they get the marble inside..."
        doll "The shape makes drinking it impracticable but nothing a straw won't fix."
        return

    label .homework_exposition:
        doll "There seems to be more doodles on the pages than actual homework."
        doll "These sketches of me are impeccable..." 
        doll "I'm surprised she managed to capture so much detail so quickly."
        doll "What a talented child."
        return
            
    label .rice_cooker_exposition:
        doll "Is that a rice cooker?"
        doll "This one looks a lot more modern than the one at a previous house." 
        doll "It doesn't look like it's on."
        return

    label .point_and_click:
        init 1:
            define KitchenPAC_POI = [
                PointOfInterest("Ramune", "kitchen.ramune_exposition", PointOfInterestImageSet("images/environment/closet/Closet_Hover.png"), BackgroundScale),
                PointOfInterest("Homework", "kitchen.homework_exposition", PointOfInterestImageSet("images/environment/diary/Diary_Hover.png"), BackgroundScale),
                PointOfInterest("Rice Cooker", "kitchen.rice_cooker_exposition", PointOfInterestImageSet("images/environment/papers/Papers_Hover.png"), BackgroundScale),
            ]
        call screen point_and_click_screen(KitchenPAC_POI)

    menu .emi_warning:
        "It sounds like Nicole is coming downstairs, what should I do?"

        "Knock over the ramune":
            $ malice += 1
            emi "*Gasp*"

            nicole "What are you making?"
            nicole "Wait."
            nicole "Is that my doll? What are you doing with it? You're going to ruin it!"

            emi "I wasn't! I-I was... just..."

            nicole "Stop touching my stuff! And are you serious?"

            narrator "Nicole gestured at the puddle of ramune being soaked up by the pages of Emi's notebook."

            nicole "Next time clean up your mess!"

            emi "Okay, I'm sorry..."

            nicole "Go put her in the living room. We need to clear the table and make rice before mom gets back."

            emi "Okay..."

            narrator "Emi picked me up and quietly made for the living room. I could feel Nicole's eyes following us."

            nicole "Fine, whatever. I'll clean it up myself since I do everything around here."

        "Sit still":
            nicole "Emi? Are you down here? What are you making?"

            emi "*Gasp*"
            emi "She's going to kill me if she sees you."

            narrator "Emi quickly drops what she is doing and runs over to me."

            emi "Let's go, I'll hide you in the living room. You'll be safe there."

            narrator "She quickly ducks into the next room."
            narrator "From the kitchen I can faintly hear Nicole mumbling to herself."

            nicole "Emi? Hm, what's this?"
            nicole "Did she draw these?"
            nicole "Is that Nadeshiko, and my other dolls?"
            nicole "These are good... no, they're amazing." 
            nicole "I never knew she could draw."
            nicole "All this time I thought she was just messing around with them." 

label living_room:
    scene bg livingroom at BackgroundScale

    show doll neutral at LeftPortrait
    doll "So this is the living room. It reminds me of a home I once lived in years ago."
    doll "Nicole seems like the kind of older sister who bosses Emi around."
    doll "That won't do but for now let's find out more about this household, shall we?"

    jump living_room.point_and_click

    label .plants_exposition:
        doll "Oh I know these, Money Trees."
        doll "These are supposed to bring abundance to their owners. I wonder if they actually believe that."
        return

    label .altar_exposition:
        doll "That's strange. There aren't any photographs."
        doll "In fact, there aren't any photos in the living room at all."
        return

    label .guan_yin_exposition:
        doll "A Buddha."
        doll "This must be the statue that Nicole's mother prays to everyday after work."
        doll ""
        return

    label .point_and_click:
        init 1:
            define living_roomPAC_POI = [
                PointOfInterest("Plants", "living_room.plants_exposition", PointOfInterestImageSet("images/environment/plant/Plant_Hover.png"), BackgroundScale),
                PointOfInterest("Incense",  "living_room.altar_exposition", PointOfInterestImageSet("images/environment/incense/Incense_Hover.png"), BackgroundScale),
                PointOfInterest("Guan Yin", "living_room.guan_yin_exposition", PointOfInterestImageSet("images/environment/guan yin/GuanYin_Hover.png"), BackgroundScale),
            ]
        call screen point_and_click_screen(living_roomPAC_POI)

label attic:
    scene bg attic at BackgroundScale
    # Doll is narrating not sure how to label / code it

    narrator "I decided to wander about the house while Nicole and Emi were busy in kitchen."
    narrator "I wanted to know more about these people and what made them tick."
    narrator "That's the only way if I am to stay here and become a part of this family."

    show nicole neutral at truecenter, PortraitDimensions
    narrator "Nicole was simple enough."
    hide nicole

    show emi neutral at truecenter, PortraitDimensions
    narrator "Emi was quite the surprise."
    hide emi

    narrator "But there was one last person's secrets I needed to uncover."

    show mom neutral at truecenter, PortraitDimensions
    narrator "The mother."
    hide mom

    narrator "Her bedroom was locked so there wasn't anyway to enter but even if I could I doubt there'd be anything worth noting."
    narrator "If the mother's room is anything like the living area then it'd be devoid of personal belongings other than wall scrolls, plants, and other common household items."

    narrator "No... what I needed was something more."

    narrator "Other than the bathroom, there was only one other place left in the house."
    narrator "..."
    narrator ".."
    narrator "."
    narrator "The attic."

    narrator "The inside of the attic is cluttered with boxes and a film of dust."
    narrator "It's a storage area which is perfect for hidden treasures."

    show doll neutral at LeftPortrait
    narrator "I rummage through the closest box to me and continue through the room prying boxes open until I find something that peaks my interest."

    narrator "Nestled at the bottom is a couple of photos and trinkets."

    doll "These look important. Maybe they're exactly what I've been looking for."

    narrator "I carefully inspected the first photo. In it is a young woman and a man. It looks like a wedding photo."

    doll "Interesting, now why would this be hidden in the attic and not taking its place in the living room?"

    narrator "The next photo is one of Nicole and Emi. The woman must be their mother but there's no sign of their father."

    narrator "Putting the photos aside, I turn the strange trinket over in my hand to take in its dull sheen."

    doll "A hairpin. The same one worn in the wedding photo, if I'm not mistaken."

    doll "I can't imagine Nicole ever wearing something as beautiful as this however I do think it'd suit me."

    doll "What's this? There's something else at the bottom."

    narrator "At the very bottom and neatly folded are a few garments in various shades of blue."

    doll "Are these baby clothes?"

    narrator "They weren't just baby clothes but boy clothes."

    doll "There's a brother, what happened to him?"

    doll "*Gasp* Or maybe..."

    narrator "I glance at the photo of Nicole and Emi again and suddenly it made sense."

    doll "They must have been expecting a son but ended up with a girl instead."

    doll "How sad... I can help make it better." 
    
    jump attic.point_and_click

    label .photos_exposition:

    return

    label .hair_pin_exposition:

    return

    label .clothing_trunk_exposition:

    return


    label .point_and_click:
        init 1:
            define atticPAC_POI = [
                PointOfInterest("Photos", "attic.photos_exposition", PointOfInterestImageSet("images/environment/photos/Photos_Hover.png"), BackgroundScale),
                PointOfInterest("HairPin",  "attic.hair_pin_exposition", PointOfInterestImageSet("images/environment/hairpin/HairPin_Hover.png"), BackgroundScale),
                PointOfInterest("ClothingTrunk", "attic.clothing_trunk_exposition", PointOfInterestImageSet("images/environment/clothingtrunk/ClothingTrunk_Hover.png"), BackgroundScale),
            ]
        call screen point_and_click_screen(atticPAC_POI)

    menu photograph:
        "I want to help the family."
        
        "Fix the photograph":
            "Woot!"

        "Ignore the photograph":
            $ malice += 1
            "I fucking hate the family."

    if malice == 5:
        jump bad_ending
    elif malice == 0:
        jump good_ending
    else:
        jump neutral_ending

label bad_ending:
    doll "Ye gads, my roast is ruined!"
    $ persistent.got_bad_ending = True
    jump game_end

label neutral_ending:
    nicole "Patented Skinner Burgers."
    $ persistent.got_neutral_ending = True
    jump game_end

label good_ending:
    emi "Auroa Borealis, localized entirely in your living room?"
    doll "Yes."
    emi "Well Doll, you drive a hard bargain."
    $ persistent.got_good_ending = True
    jump game_end
