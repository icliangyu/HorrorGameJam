# Labels and naming of assets are just placeholders
# 
#
#

define n = Character("Nicole") 
define d = Character("Doll")
define m = Character("Mom")
define e = Character("Emi")
default suspicion = 0 
# Suspicion needs to be reworked / reworded it doesn't work as intended with plot
# Thinking of malice instead of

label start:
    scene bg black
    n "Let's see what you look like..."
    # need SFX of rustling sound of boxes here

    scene bg white
    show nicole surprised
    n "What?"
    n "This isn't the doll I ordered..."
    show nicole angry

    # cue leitmotif for the player's introduction to the doll!
    show doll neutral

    menu unboxing:
        "How should I greet my new owner?"

        "Smile":
            $ suspicion += 1
            jump bad_choice_1

        "...":
            jump good_choice_1

label bad_choice_1
    # SFX for +1 suspicion point
    # player should also have a visual indicator of +1 point
    show doll happy
    show nicole surprised
    n "Huh... you are pretty cute though, maybe I'll keep you around."
    n "I've seen a lot of detailed ball-jointed dolls but you're something else."
    n "Life like, even..."

label good_choice_1
    show doll neutral
    show nicole neutral
    n "*Sigh* Whatever, this is fine too. I'm too lazy to request a return from the seller."

label bedroom:
    scene bg bedroom
    # point and click gameplay begins
    # a lot of exposition will happen through item interaction
    # image button coding action will be configured to jump("label_whatever_item_is_clicked_on")
    m "Nick! Come down here and watch the house. I'm going to buy groceries!"
    n "*Sigh"
    m "Now!" 
    n "Ugh! Okay fine!"
    n "Couldn't just call Emi? Why is it always me?"
    n "Hmm... where to hide you so that rascal doesn't find you...?"
    n "Under the bed should do for now." 
    # SFX was storing box away
    # SFX of door slamming
    # SFX of footsteps stomping downstairs

    #### narration and dialogue portion not sure what to call it
    d "So this must be my home and that was my new owner."
    d "A bit on the older side to be playing with dolls. I'm used to much younger owners but I suppose this is fine too."

    I crawled out from underneath the bed and took in the room before me. 
    It wasn't particularly big but it did have character. 

    #will insert more descriptions once BGs are finalized

    Now that I was finally introduced to my new home it would be best to look around.

    show doll happy
    d "Don't mind if I do hehe!"

    
# Insert creepy ass SFX for the point and click portions

label diary:
    d "A diary?" 
    d "She doesn't seem like the type of girl who would write about her feelings and lock them away in a secret book."
    d "I am quite curious though..."
    d "Oh Nicole, what are you hiding within these pages."

    n "Sunday XX, 20XX"
    n "Mom tried to set me up with one of her friend's son- again." 
    n "How many times have I told her I'm not interested?"
    n "Probably a thousand."
    n "How many times have I told her I'm not interested men?"
    n "I'll get around to it."

label bills:
    d "What's this?"
    d "

label other_dolls:
    d "That's a lot of dolls."
    d "Hehe... I'm not afraid of a little competition."
    d "They may have been here longer but none of them are me."
    d "Upon closer inspection, I can see that I'm not the usual type that Nicole would gravitate towards."
    d "That might pose as a problem."
    d "All of the previous owners were similar to me."
    d "Well, nothing I can't fix."

label clothes:
    d "What is all of this?
    d "Is this really what she wears on the daily?"
    d "This style really doesn't suit me at all but it's nothing that can't be changed."
    d "Nicole, why are you dressing yourself up in such masculine clothes? 

label bedroom_part2:
    d "Somebody is coming. I must hide."

    e "Hmm..." 
    # SFX of door creaking open
    e "Did Nick get another friend?"
    e "Now where could they be...?"
    # SFX rummaging sound or reuse SFX of storing box away
    e "Really Nick? You should know better than to hide your pretties under the bed."
    e "Who do we have here?"
    e "*Gasp* She's beautiful!"
    show doll neutral
    e "Nadeshiko, huh? Let's go downstairs. 

label kitchen:
    e "Let's put you down here."
    e "Wow... you're even prettier up close."

    show doll confused

    # SFX of pencil scratching on paper
    e "Your dress is so detailed..."
    e "And this stitching!"

    d "Is she drawing me?"

    e "I wish Nick wore clothes like you, that way I could wear them too."

menu emi_question:
    "What should I do?"

    "Console Emi":
        $ suspicion += 1
        jump bad_choice_2

    "Listen to Emi":
        jump good_choice_2

label bad_choice_2:
    e "I don't want to sound ungrateful but sometimes it's embarrassing wearing Nick's hand me downs."
    e "Once I get a job, I'll be able to wear all the girly clothes I want."
    e "But..."
    e "That kind of money would be helpful to the family so I don't know..."

    d "I could be your big sister, Emi."
    d "Then you wouldn't have to wear those ugly clothes anymore."

    e "I think I would like that."

    #should jump to next section

label good_choice_2:
    e "I don't want to sound ungrateful but sometimes it's embarrassing wearing Nick's hand me downs."
    e "Once I get a job, I'll be able to wear all the girly clothes I want."
    e "But..."
    e "That kind of money would be helpful to the family so I don't know..."

    e "I'll just have to work extra hard so that there's enough for both."

    #should jump to next section

label kitchen_part_2:
    e "Nick never lets me play with her dolls but I need them for reference."
    e "They're the perfect inspiration and model for my designs."
    e "Welp! Can't study on an empty stomach. I wonder if mom made anything."
    #SFX fridge rummaging

    #transition to point and click 

label ramune:
    d "These drinks are quite popular with young ones these days."
    d "I wonder how they get the marble inside..."
    d "The shape makes drinking it impracticable but nothing a straw won't fix."

label homework:
    d "There seems to be more doodles on the pages than actual homework."
    d "Are these sketches of me?" 
    d "I'm surprised she managed to capture so much detail so quickly."
    d "These are pretty good, what a talented child."

menu spill_drink:
    "It sounds like Nicole is coming downstairs, what should I do?" 

    "Knock over the ramune":
        $ suspicion += 1
        jump bad_choice_3

    "Sit still":
        jump good_choice_3

label bad_choice_3:
    # insert SFX of glass 
    e "*Gasp*
    e "She's going to kill me if she sees you."
    e "Let's go, you'll be safe in the living room."
    n "Are you serious, Emi? Next time clean up your mess!"
    n "Emi! What are you doing with my doll? You're going to ruin it!"
    e "I wasn't! I was just..."
    n "Stop touching my stuff!"
    e "Okay, I'm sorry..."
    n "Go put her in the living room. We need to clear the table and make rice before mom gets back."
    e "Okay..."

    n "*Grumbles *How are you going to study now? Your workbook's full of soda."
 
label good_choice_3:
    n "Emi? Are you down here?"

    e "*Gasp*
    e "She's going to kill me if she sees you."
    e "Let's go, you'll be safe in the living room."

    n "Emi? Hm, what's this?"
    n "Did Emi draw these?"
    # SFX flipping through pages
    n "Is that Nadeshiko, and my other dolls?"
    n "These are good... no, they're amazing." 
    n "I never knew she could draw."
    n "All this time I thought she was just messing around with them." 

label living_room:
    d "So this is the living room. It reminds me of a home I once lived in years ago."
    d "Nicole seems like the kind of older sister who bosses Emi around."
    d "That won't do but for now let's find out more about this household, shall we?"

    # point and click segment

label plants:
    d "Oh I know these, Money Trees."
    d "These are supposed to bring abundance to their owners. I wonder if they actually believe that."


label altar: 
    d "That's strange. There aren't any photographs."
    d "In fact, there aren't any photos in the living room at all."

label statue:
    d "A Buddha."
    d "This must be the statue that Nicole's mother prays to everyday after work."
    d "

label attic_scene:
    scene bg attic
    # Doll is narrating not sure how to label / code it

    I decided to wander about the house while Nicole and Emi were busy in kitchen.
    I wanted to know more about these people and what made them tick. 
    That's the only way if I am to stay here and become a part of this family.

    show nicole neutral
    Nicole was simple enough.

    show emi neutral
    Emi was quite the surprise.

    But there was one last person's secrets I needed to uncover.
    show mother neutral
    The mother.

    Her bedroom was locked so there wasn't anyway to enter but even if I could I doubt there'd be anything worth noting.
    If the mother's room is anything like the living area then it'd be devoid of personal belongings other than wall scrolls, plants, and other common household items.

    No... what I needed was something more.

    Other than the bathroom, there was only one other place left in the house.
    ...
    ..
    .
    The attic.

    The inside of the attic is cluttered with boxes and a film of dust.
    It's a storage area which is perfect for hidden treasures.

    I rummage through the closest box to me and continue through the room prying boxes open until I find something that peaks my interest.

    Nestled at the bottom is a couple of photos and trinkets.

    d "These look important. Maybe they're exactly what I've been looking for."

    I carefully inspected the first photo. In it is a young woman and a man. It looks like a wedding photo. 

    d "Interesting, now why would this be hidden in the attic and not taking its place in the living room?"

    The next photo is one of Nicole and Emi. The woman must be their mother but there's no sign of their father.

    Putting the photos aside, I turn the strange trinket over in my hand to take in its dull sheen.

    d "A hairpin. The same one worn in the wedding photo, if I'm not mistaken."

    d "I can't imagine Nicole ever wearing something as beautiful as this however I do think it'd suit me."

    d "What's this? There's something else at the bottom."

    At the very bottom and neatly folded are a few garments in various shades of blue.

    d "Are these baby clothes?"

    They weren't just baby clothes but boy clothes. 

    d "There's a brother, what happened to him?"

    d "*Gasp* Or maybe..."

    I glance at the photo of Nicole and Emi again and suddenly it made sense.

    d "They must have been expecting a son but ended up with a girl instead."

    d "How sad... I can help make it better." 

        menu photograph:
            "I want to help the family."
            
            "Fix the photograph":
                $ suspicion += 1
                jump bad_choice_5

            "Ignore the photograph":
                jump good_choice_5
    
return
