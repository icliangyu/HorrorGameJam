# Labels and naming of assets are just placeholders
define nicole = Character("Nicole") 
define doll = Character("Doll")
define mom = Character("Mom")
define emi = Character("Emi")
default malice = 0 

# malice needs to be reworked / reworded it doesn't work as intended with plot
# Thinking of malice instead of

transform PortraitDimensions:
    xysize (-363, 826)

transform LeftPortrait:
    pos (421, 229)
    xysize (-363, 826)

transform RightPortrait:
    pos (1532, 229)
    xysize (363, 826)

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

    scene bg_bedroom
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

    $ bedroomPCO = []
    menu bedroomMenu: #Make this point and click actually
        set bedroomPCO
        "Diary":
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
            pass
            jump bedroomMenu

        "Bills":
            doll "What's this?"
            doll ""
            pass
            jump bedroomMenu
        
        "Other Dolls":
            doll "That's a lot of dolls."
            doll "Hehe... I'm not afraid of a little competition."
            doll "They may have been here longer but none of them are me."
            doll "Upon closer inspection, I can see that I'm not the usual type that Nicole would gravitate towards."
            doll "That might pose as a problem."
            doll "All of the previous owners were similar to me."
            doll "Well, nothing I can't fix."
            pass
            jump bedroomMenu

        "Clothes":
            doll "What is all of this?"
            doll "Is this really what she wears on the daily?"
            doll "This style really doesn't suit me at all but it's nothing that can't be changed."
            doll "Nicole, why are you dressing yourself up in such masculine clothes?"
            pass
            jump bedroomMenu

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

    scene bg_kitchen

    $ kitchenPCO = []
    menu kitchenMenu:
        set kitchenPCO 
        "ramune":
            doll "These drinks are quite popular with young ones these days."
            doll "I wonder how they get the marble inside..."
            doll "The shape makes drinking it impracticable but nothing a straw won't fix."
            pass
            jump kitchenMenu

        "homework":
            doll "There seems to be more doodles on the pages than actual homework."
            doll "Are these sketches of me?" 
            doll "I'm surprised she managed to capture so much detail so quickly."
            doll "These are pretty good, what a talented child."
            pass
            jump kitchenMenu

    menu spill_drink:
        "It sounds like Nicole is coming downstairs, what should I do?" 

        "Knock over the ramune":
            $ malice += 1
            # insert SFX of glass 
            emi "*Gasp*"
            emi "She's going to kill me if she sees you."
            emi "Let's go, you'll be safe in the living room."
            nicole "Are you serious, Emi? Next time clean up your mess!"
            nicole "Emi! What are you doing with my doll? You're going to ruin it!"
            emi "I wasn't! I was just..."
            nicole "Stop touching my stuff!"
            emi "Okay, I'm sorry..."
            nicole "Go put her in the living room. We need to clear the table and make rice before mom gets back."
            emi "Okay..."

            nicole "*Grumbles *How are you going to study now? Your workbook's full of soda."

        "Sit still":
            nicole "Emi? Are you down here?"

            emi "*Gasp*"
            emi "She's going to kill me if she sees you."
            emi "Let's go, you'll be safe in the living room."

            nicole "Emi? Hm, what's this?"
            nicole "Did Emi draw these?"
            # SFX flipping through pages
            nicole "Is that Nadeshiko, and my other dolls?"
            nicole "These are good... no, they're amazing." 
            nicole "I never knew she could draw."
            nicole "All this time I thought she was just messing around with them." 

    scene bg_living_room

    show doll neutral at LeftPortrait
    doll "So this is the living room. It reminds me of a home I once lived in years ago."
    doll "Nicole seems like the kind of older sister who bosses Emi around."
    doll "That won't do but for now let's find out more about this household, shall we?"

    # point and click segment
    $ livingroomPCO = []
    menu livingroomMenu:
        set livingroomPCO
        "plants":
            doll "Oh I know these, Money Trees."
            doll "These are supposed to bring abundance to their owners. I wonder if they actually believe that."
            pass
            jump livingroomMenu


        "altar": 
            doll "That's strange. There aren't any photographs."
            doll "In fact, there aren't any photos in the living room at all."
            pass
            jump livingroomMenu

        "statue":
            doll "A Buddha."
            doll "This must be the statue that Nicole's mother prays to everyday after work."
            doll ""
            pass
            jump livingroomMenu

    scene bg attic
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

    menu photograph:
        "I want to help the family."
        
        "Fix the photograph":
            "Woot!"

        "Ignore the photograph":
            $ malice += 1
            "I hate the family."

return