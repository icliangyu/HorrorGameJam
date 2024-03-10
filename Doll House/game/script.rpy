###
###
###
###

define nicole = character("\"Nicole\" if knows_owners_name else \"The Owner\"", dynamic=True)
define doll = character("Nadeshiko")
define emi = character("Emi")
define mom = character("Mother")

define malice = 0 

init python:
    def ChangeMalice(value):
        if value > 0:
            renpy.sound.play(renpy.store.audio.MaliceIncrease)
        renpy.store.malice += value

init 0:
    define knows_owners_name = False

label start:
    scene black
    centered "For centuries dolls have been common household items beloved by children."
    centered "But recently they have started to become a popular collector's item."
    centered "They are adored by many for their perfect features and ornate clothes." 

    centered "But did you know?"

    centered "Dolls have been found to exist in ancient civilizations."
    centered "And they weren't just hidden away in the corners of bedrooms like today."
    centered "No..."
    centered "They took on multiple roles."
    centered "Some were used as lucky charms, some as religious symbols, and others for protection."

    centered "Isn't it peculiar how they are modeled after the human figure?"
    centered "Miniature human-like objects imbued with qualities to cover our limitations."
    centered "It's no wonder that with time they became companions to the young and vulnerable."

    centered "This is the story of one such doll..."

label bedroom:
    show nicole happy at LeftPortrait
    nicole "Let's see what you look like..."

    narrator "On that day, darkness finally gave way to a blinding light that was almost immediately eclipsed by a scowling face."

    ### SCENE BG BLURRED BEDROOM

    show nicole surprised at LeftPortrait
    nicole "What?"
    show nicole angry at LeftPortrait
    nicole "This isn't the doll I ordered."

    show doll neutral at RightPortrait
    narrator "A pair of scrutinizing eyes stared back, studying the doll over carefully. There was no hint of true satisfaction or dissatisfaction at what had been received."
    narrator "Rather, there remained an air of indifference directed at the doll upon inspection."

    show nicole angry at LeftPortrait
    nicole "Did you not come with any information?"

    ### SFX RUMMAGING
    narrator "The girl clicked her tongue impatiently as she emptied out the box."
    narrator "Other than the doll, the only other thing inside the box was a certificate of authentication."

    show nicole surprised at LeftPortrait
    nicole "Nadeshiko..."
    nicole "No brand name, or serial number, and yet the craftsmanship is too excellent to be counterfeit."
    nicole "Maybe it's one of a kind?"

    narrator "Unsure of whether to keep this mysterious doll of unknown origins, the girl pondered this question as weary eyes full of uncertainty met glassy doe eyes lined with thick lashes."

        menu unboxing:
            "How should I greet my new owner?"

            "Smile":
                show doll happy at LeftPortrait
                $ ChangeMalice(1)
                narrator "In wanting to give her new owner a warm welcome, the doll's mouth curved up with the slightest smile."

                show nicole happy at RightPortrait
                nicole "Huh... you are pretty cute though, maybe I'll keep you around."
                show nicole surprised at RightPortrait
                nicole "I've seen a lot of detailed ball-jointed dolls but you're something else."
                nicole "Life-like, even..."
                show nicole happy at RightPortrait

                narrator "The owner responded back in kind with a small smile of her own, and this gave the doll immense relief knowing that she was accepted for the time being."

            "...":
                show doll neutral at LeftPortrait
                show nicole sad at RightPortrait
                nicole "*Sigh* Whatever, this is fine for now. I'm too lazy to request a return from the seller."
                show nicole neutral at RightPortrait
                nicole "I'll think about it later."
                nicole "It's pretty, sure, but I don't know if this model is worth more or less than what I originally bought. I don't want to get ripped off."

    show mom neutral at RightPortrait
    mom "Nick! Come down here and watch the house. I'm going to buy groceries!"

    show nicole fear at LeftPortrait
    nicole "*Sigh*"
    show nicole angry at LeftPortrait
    nicole "Just a minute!"

    show mom angry at RightPortrait
    mom "Now!"

    show nicole angry at LeftPortrait
    nicole "Ugh! Okay fine!"
    nicole "She couldn't just get Emi? Why is it always me?"

    narrator "The owner grumbled to herself as she cleared the boxes off her desk and slid them under the bedframe."

    show doll neutral at RightPortrait
    show nicole fear at LeftPortrait
    nicole "Hmm... but first where to hide you so that the rascal won't find you."
    show nicole happy at LeftPortrait
    nicole "Under the bed should do for now."

    ### SFX FOOTSTEPS RECEDING
    ### SFX DOOR CLOSING

    narrator "And so the doll joined the boxes in the darkness of the underside of the bed. The world of light she so desperately sought came to a quick end." 

    show doll surprised at LeftPortrait
    doll "This must be my new home."
    show doll sad at LeftPortrait
    doll "That makes her my new owner."
    show doll happy at LeftPortrait
    doll "A bit on the older side to be playing with dolls. I'm used to much younger owners but I suppose this is fine too."

    scene bg bedroom 
    narrator "The doll crawled out from the depths of the darkness and brushed herself off indignantly."
    narrator "Now that Nadeshiko was finally introduced to her new home she couldn't wait to learn more about the owner."  
    narrator "After all, the doll wanted nothing more than to make a good impression."

        jump bedroom.point_and_click

            label .diary_exposition:
                show doll surprised at LeftPortrait
                show doll happy at LeftPortrait
                doll "A diary? Don't mind if I do hehe!"
                show doll neutral at LeftPortrait
                doll "She doesn't seem like the type of girl who would write about her feelings and lock them away in a secret book."
                show doll happy at LeftPortrait
                doll "I am quite curious though..."
                show doll neutral at LeftPortrait
                doll "Tell me, what are you hiding within these pages?"

                narrator "It was rather uncouth to look through a person's diary but curiosity got the better of Nadeshiko and she immediately found herself poring over the scratchy writing, trying to absorb any and all information that it could give on the owner."

                centered "Mom tried to set me up with one of her friend's sons— again." 
                centered "How many times have I told her I'm not interested?"
                centered "Probably a thousand."
                centered "How many times have I told her I'm not interested in men?"
                centered "I'll get around to it... one day..."

                centered "Today mom came home and went straight to the living room to pray. It's so annoying how she pushes this onto us."
                centered "What's praying going to do anyway?"
                centered "How come we keep praying but our problems keep on getting bigger? Like the rent and my student loans."
                centered "I shouldn't have bought another doll but I deserve something nice one in a while... right? If so then why do I feel so guilty?"
                centered "Maybe that money should have been put towards the rent."
                centered "I can always return the doll but I also really want it. I guess I'll see how I feel when it arrives."

                show doll sad at LeftPortrait
                doll "Hmm... she's really bitter."
                show doll happy at LeftPortrait
                doll "But that's why I'm here to make things better!"
                return

            label .bills_exposition:
                narrator "The doll's curious gaze landed upon the pile of opened envelopes."

                show doll fear at LeftPortrait
                doll "Bills, bills, and more bills. It looks like they're addressed to someone named Nicole."
                show doll happy at LeftPortrait
                doll "So my owner's name is Nicole. How wonderful! Both of our names start with the letter N."

                narrator "Though only a doll, she was able to understand the weight of the situation. There were student loans, utilities, and credit card payments all addressed to Nicole."

                show doll neutral at LeftPortrait
                doll "One of the statements indicate a recent doll purchase. That must be the doll I replaced."
                
                narrator "Not being one to leave things to chance, the audacious doll scavenged around the desk where a couple of slips from her packaging also laid atop. Finding exactly what she was looking for, the doll tore up the slips to reduce the chances of being returned."

                ### SFX PAPER RIPPING

                show doll happy at LeftPortrait
                doll "There."
                doll "I'm here to stay."

                $ knows_owners_name = True
                return

            label .dolls_exposition:
                narrator "On the shelf were a couple of dolls whose eyes were locked forward in a vacant stare. Nadeshiko tilted her head as she stared back, waiting to see if any of them would acknowledge her."
                narrator "This might have been the first time the doll ever experienced something akin to jealousy since all of her previous owners only had her and her alone."

                show doll happy at LeftPortrait
                doll "Heh... I'm not afraid of a little competition."
                show doll angry at LeftPortrait
                doll "They may have been here longer but none of them are like me."
                show doll surprised at LeftPortrait
                doll "Hmm... upon closer inspection I can see that I'm not the usual type she would gravitate towards."
                show doll neutral at LeftPortrait
                doll "That might pose a problem."
                doll "All of the previous owners were similar to me."
                show doll happy at LeftPortrait
                doll "Well, nothing I can't fix."
                return
            
            label .books_exposition:
                show doll surprised at LeftPortrait
                doll "There's a book here about a human girl with a doll's eye."
                doll "Interesting..."

            label .closet_exposition:
                narrator "To the doll's dismay, this was a pile of her owner's clothes."

                show doll surprised at LeftPortrait
                doll "What is all of this?"
                show doll sad at leftPortrait
                doll "Is this really what she wears... on the daily?"

                narrator "Being a doll, Nadeshiko has only ever known of custom handmade items of the finest quality. The pieces before almost made her weep in despair."

                show doll sad at LeftPortrait
                doll "This style really doesn't suit me at all but it's nothing that can't be changed."
                doll "Oh why... why are you dressing yourself up in such masculine clothes?"
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

    ### THIS IS HERE IN CASE THE PLAYER SKIPS THE POINT AND CLICK
    $ knows_owners_name = True

    ### SFX FOOTSTEPS APPROACHING
    show doll surprised at LeftPortrait
    doll "Huh? It sounds like someone is coming. I must hide!"

    narrator "Nadeshiko quickly ran underneath the bed and crawled back into the shadows of the boxes. If anyone had witnessed this, they would have simply thought that a small animal had scurried under the bed."

    ### SFX DOOR OPENING
    show doll neutral at LeftPortrait
    doll "This must be Emi."

    show emi neutral at RightPortrait
    emi "Hmm..."
    emi "Did Nick get another friend? I saw her carry up a box so it must be true."
    emi "Now where could they be...?"
    show emi happy at RightPortrait
    emi "Really Nick? You should know better than to hide your pretties under the bed."
    emi "Let's see who we have here..."
    emi "*Gasp* She's beautiful!"

    narrator "The young girl turned over the doll and her accompanying certificate in awe. The doll stayed still but her glassy eyes shone with happiness at being found and rescued from her place in the darkness."

    centered "Or perhaps the source of happiness stemmed from the child's radiant love for her despite only just having met. There wouldn't be any need for convincing Emi unlike with Nicole."

    show emi happy at LeftPortrait
    emi "Nadeshiko, huh? Let's go downstairs."

label kitchen:
    ### SCENE BG BLURRED KITCHEN
    narrator "With the doll in hand, the younger sister skipped down the steps and into the kitchen where she diligently sat at the dinner table everyday after school to do homework."

    show emi happy at LeftPortrait
    emi "Let's put you down here."

    narrator "Propped up against a pencil case, Nadeshiko once again found herself being inspected by a set of curious brown eyes; however there was a stark difference between the two sisters."
    narrator "While Nicole's weary eyes held traces of age and suspicion, Emi's was filled to the brim with life and adoration."
    
    centered "The doll liked this a lot."

    show emi happy at LeftPortrait
    emi "Wow... you're even prettier up close."
    emi "And your name's Nadeshiko, how fitting!"

    narrator "The young girl ran her fingers through the doll's silky hair as though oiled by camellias. She straightened out the dress, and leaned back with a content sigh."
    narrator "If the doll could, she too would have let out a similar sigh with eyes closed in bliss. She found these actions to be particularly endearing, and felt excitement at the prospect of being a part of the family."
    narrator "Of course, she had to keep her excitement to herself but wished to someday share it with Emi."
    narrator "Nadeshiko's hair and garments were continuously stroked and studied by Emi's keen eyes as she muttered to herself."

    show emi happy at LeftPortrait
    emi "Your dress is so detailed, and the stitching!"
    show emi neutral at Leftportrait
    emi "I have to get this down on paper."

    ### SFX PENCIL SCRATCHING ON PAPER
    narrator "Emi's hands left the doll to pick up the pencil lying in the middle of her notebook and began to scrawl around the corners of her page, doing well to avoid the math problems."
    narrator "It wasn't long before Nadeshiko's likeness began to appear on the lined white pages."

    show doll neutral at RightPortrait
    doll "Is she drawing... me?"
    doll "There she was, in perfect likeness, in Emi's notebook modeling different designs and patterns."

    narrator "For a young girl to take inspiration from her and so quickly create something before her eyes was amazing to Nadeshiko. In fact, she was so amazed that a sense of embarrassment and flattery overwhelmed the doll as she sat still and looked on at the prodigy working away."
    narrator "The doll thought to herself,"

    show doll angry at RightPortrait
    doll "Nicole doesn't seem to harbor any skills or hobbies other than collecting dolls and debt."
    show doll happy at RightPortrait
    doll "I think I like Emi better."

    narrator "Suddenly the young girl spoke to the doll as if she knew it was listening."

    show emi sad at LeftPortrait
    emi "I wish Nick wore clothes like you, that way I could wear them too."

        menu comforting:
            "What should I do?"

            "Console Emi":
                $ ChangeMalice(1)
                show emi neutral at LeftPortrait
                emi "I don't want to sound ungrateful but sometimes it's embarrassing wearing Nick's hand me downs."

                show emi sad at LeftPortrait
                show doll neutral at RightPortrait
                doll "..."

                show emi neutral at LeftPortrait
                emi "They're just so... we just have different styles."
                emi "Once I'm old enough to work, I'll be able to wear whatever I want."
                show emi happy at LeftPortrait
                emi "Even dresses like yours!"
                show emi neutral at LeftPortrait
                emi "But..."
                show emi sad at LeftPortrait
                emi "That kind of money would be helpful to mom and Nicole so I don't know..."

                narrator "Emi's downcast face continued to glance between the doll and the page as she sketched. Even though the two had just met, Nadeshiko didn't like seeing Emi so sad."

                centered "So the doll decided to speak up."
                centered "I could be your big sister, Emi."
                centered "Then you wouldn't have to wear those ugly clothes anymore."
                centered "A sweet girl like you deserves to be dressed in frills and laces."
                centered "I can help."

                narrator "The young girl looked up from her work. Her eyes searched the doll's unmoving gaze for a moment before replying with a wide smile."

                show emi happy at LeftPortrait
                emi "I think I would like that."

            "Listen to Emi":
                show emi neutral at LeftPortrait
                emi "I don't want to sound ungrateful but sometimes it's embarrassing wearing Nick's hand me downs."

                show emi sad at LeftPortrait
                show doll neutral at RightPortrait
                doll "..."

                show emi neutral at LeftPortrait
                emi "They're just so... we just have different styles."
                emi "Once I'm old enough to work, I'll be able to wear whatever I want."
                show emi happy at LeftPortrait
                emi "Even dresses like yours!"
                show emi neutral at LeftPortrait
                emi "But..."
                show emi sad at LeftPortrait
                emi "That kind of money would be helpful to mom and Nicole so I don't know..."

                narrator "As much as Nadeshiko wanted to, she knew that it wouldn't have been wise to risk doing anything that would startle Emi."
                narrator "So with an uneasy heart, the doll remained silent and listened to the young girl talk as she drew."

                show emi happy at LeftPortrait
                emi "I'll just have to work extra hard and save up so that there's enough for both."
                emi "But mom and Nicole come first. I don't want them to be so stressed all the time."
                emi "I wouldn't be happy having pretty clothes while they're worried about money and the house anyway."

                narrator "Nadeshiko listened to the heartfelt words that Emi was telling her in confidence. She couldn't help but admire the young girl's selflessness that could only be possessed by those beyond her years."

    show emi sad at LeftPortrait
    emi "*Sigh*"
    emi "Nick never lets me play with her dolls because she thinks I’ll ruin them but I need them for reference."
    show emi neutral at LeftPortrait
    emi "They’re the perfect inspiration and model for my designs"

    doll "Nadeshiko knew that as long as Emi had her then there wouldn’t be any need for Nicole’s other dolls."
    doll "She alone was enough."

    ### SFX STOMACH GROWL

    show emi happy at LeftPortrait
    emi "Hehe... whoops... that was me. Welp! Can’t study on an empty stomach. I wonder if mom made anything."
    show emi sad at LeftPortrait
    emi "Aww... there’s nothing to eat. Cup noodles it is!"
    show emi happy at LeftPortrait

    scene bg kitchen
    narrator "Nadeshiko almost let out a giggle at the sight of Emi frantically rummaging through the fridge and cabinets in search of food. The young prodigy had a lot of life in her that drew Nadeshiko to her, unlike Nicole."
    narrator "While Emi made her food, the doll took this time to look around the kitchen in hopes of learning more about this peculiar household."

        jump kitchen.point_and_click

            label .ramune_exposition:
                show doll neutral at LeftPortrait
                doll "These drinks are quite popular with the young ones these days."
                show doll surprised at LeftPortrait
                doll "The liquid inside is so bright and colorful! It'd probably stain easily."
                show doll fear at LeftPortrait
                doll "I wonder how they get the marble inside... do people break the bottle to collect them?"
                show doll happy at LeftPortrait
                doll "The shape makes drinking it impractical but nothing a straw won’t fix. Then again, maybe that why children love it."
                return

            label .homework_exposition:
                show doll surprised at LeftPortrait
                doll "There seems to be more doodles on the pages than actual homework."
                show doll neutral at LeftPortrait
                doll "These sketches of me are impeccable..."
                doll "I’m surprised she managed to capture so much detail so quickly."
                show doll happy at LeftPortrait
                doll "What a talented child."
                return

            label .rice_cooker_exposition:
                show doll neutral at LeftPortrait
                doll "Is that a rice cooker?"
                doll "This one looks a lot more modern than the one at the previous house."
                doll "It doesn’t look like it’s on so there mustn't be any rice inside."
                return

            label .wok_exposition:
                show doll happy at LeftPortrait
                doll "A classic wok. Great for making fried rice!"
                show doll surprised at LeftPortrait
                doll "I wonder if Emi knows how to make fried rice."
                return

            label .fridge_exposition:
                show doll neutral at LeftPortrait
                doll "There won't be anything useful in there until Mother comes back."
                return

            label .soysauce_exposition:
                show doll fear at LeftPortrait
                doll "Much too salty for me."
                doll "Don't people believe that salt can ward off evil spirits?"
                show doll angry at LeftPortrait
                doll "Good thing there's no evil spirits here."
                return

            label .point_and_click:
                init 1:
                    define KitchenPAC_POI = [
                        PointOfInterest("Ramune", "kitchen.ramune_exposition", PointOfInterestImageSet("images/environment/closet/Closet_Hover.png"), BackgroundScale),
                        PointOfInterest("Homework", "kitchen.homework_exposition", PointOfInterestImageSet("images/environment/diary/Diary_Hover.png"), BackgroundScale),
                        PointOfInterest("Rice Cooker", "kitchen.rice_cooker_exposition", PointOfInterestImageSet("images/environment/papers/Papers_Hover.png"), BackgroundScale),
                    ]
            call screen point_and_click_screen(KitchenPAC_POI)

    narrator "As Nadeshiko was taking in her surroundings, she heard the faint sound of footsteps."

        menu warning:
            "It sounds like Nicole is coming downstairs, what should I do?"

            "Knock over the ramune":
                $ ChangeMalice(1)
                ### SFX GLASS BREAKING
                show emi sad at LeftPortrait
                emi "*Gasp*"

                show nicole neutral at RightPortrait
                nicole "What are you making?"
                show nicole fear at RightPortrait
                nicole "Wait."
                show nicole angry at RightPortrait
                nicole "Is that my doll? What are you doing with it? You're going to ruin it!"

                show emi crying at LeftPortrait
                emi "I wasn't! I-I was... just..."

                show nicole angry at RightPortrait
                nicole "Stop touching my stuff! And are you serious?"

                narrator "The older girl angrily gestured at the puddle of ramune being soaked up by the pages of Emi’s notebook, dyeing the drawings of the doll a bright red."

                centered "Nadeshiko sat in innocent stillness, and looked at the red pool with her painted smile and vacant eyes as though Nicole had been the one to bleed out the liquid."

                show nicole angry at RightPortrait
                nicole "Next time clean up your mess!"

                show emi sad at LeftPortrait
                emi "Okay, I'm sorry..."

                show nicole angry at RightPortrait
                nicole "Just! Argh!"
                nicole "Go put her in the living room. We need to clear the table and make rice before mom gets back."

                show emi crying at LeftPortrait
                emi "Okay..."

                narrator "The frightened young girl picked up the doll and pressed it to her chest like a warding charm to protect her from her sister’s wrath. In stifling silence, the two made for the living room."
                narrator "Nadeshiko could feel Nicole’s eyes following her."

                show nicole sad at RightPortrait
                nicole "Fine, whatever, I’ll clean it up myself since I do everything around here."

            "Sit still":
                show nicole neutral at RightPortrait
                nicole "Emi? Are you down here? What are you making?"

                show emi sad at LeftPortrait
                emi "*Gasp*"
                show emi crying at LeftPortrait
                emi "She's going to kill me if she sees you!"

                narrator "The young girl hastily dropped what she was doing and ran over to grab the doll."

                show emi neutral at LeftPortrait
                emi "Let’s go, I’ll hide you in the living room. You’ll be safe there."

                narrator "Not wanting to incur Nicole’s wrath should she be caught red handed with the new doll, Emi quickly ducked into the next room with Nadeshiko pressed tightly to her chest."
                narrator "From the kitchen, Nadeshiko could faintly hear the older sister mumbling to herself but about what she had no idea."

                show nicole surprised at LeftPortrait
                nicole "Emi? Hm, what’s this?"
                show nicole neutral at LeftPortrait
                nicole "Did she draw these?"
                show nicole surprised at LeftPortrait
                nicole "Is that Nadeshiko, and my other dolls?"
                nicole "These are good... no, they’re amazing."
                show nicole neutral at LeftPortrait
                nicole "I never knew she could draw."
                show nicole sad at LeftPortrait
                nicole "All this time I thought she was just messing around with them."

                narrator "The older girl stood in deep thought with what looked like a soft expression. Perhaps there were more surprising discoveries to be found within the house."

label living_room:
    ### SCENGE BG BLURRED LIVING ROOM
    narrator "Emi squeezed the doll tightly in a wistful embrace before placing it between two cushions on the sofa. The young girl gave one last look before returning to the kitchen."

    centered "The doll felt bad for Emi because she had to live with such a wretched person like Nicole."

    show doll sad at LeftPortrait
    doll "Poor Emi."
    show doll happy at LeftPortrait
    doll "Things will be different soon enough hehe!"

    narrator "The doll’s eyes followed her small back, making sure that Emi fully turned the corner. Nadeshiko didn’t move until the voices of the two girls could be heard amongst the busy clattering of dishes."

    show doll neutral at leftPortrait
    doll "A new room."

    narrator "The doll propped herself into an upright position, the springy coils of the old sofa underneath let out an audible groan at her slight movement."

    show doll surprised at LeftPortrait
    doll "What an uncomfortable seat!"

    narrator "Immediately the doll’s thoughts turned to Emi. It was so sad seeing the conditions she had to live in. The doll thought almost angrily,"

    show doll fear at LeftPortrait
    doll "Why wasn’t Nicole working harder to provide for them?"
    show doll neutral at LeftPortrait
    doll "Once I become a part of the family, the first thing I’ll do is get rid of this sofa."
    show doll angry at LeftPortrait
    doll "I’m starting to see just how irresponsible that girl is!"
    show doll sad at LeftPortrait
    doll "Nicole seems like the type of older sister who bosses Emi around."
    show doll neutral at LeftPortrait
    doll "That won’t do but for now let’s find out more about this household, shall we?"
    show doll angey at LeftPortrait
    doll "This is my chance to find out more about my current owner." 
    scene bg livingroom

        jump living_room.point_and_click

            label .plants_exposition:
                show doll neutral at LeftPortrait
                doll "Oh I know these. Money trees."
                doll "These are supposed to bring abundance. Do they actually believe that though?"
                show doll angry at LeftPortrait
                doll "It's funny how a lot of people don't believe in good luck are quick to fear and attribute their misfortunes to bad luck."
                show doll happy at LeftPortrait
                doll "In this family's case, they can just blame Nicole hehe!"
                return

            label .altar_exposition: 
                show doll surprised at LeftPortrait
                doll "That's strange. There aren't any pictures."
                show doll neutral at LeftPortrait
                doll "In fact, there aren't any photos in the living room at all."
                show doll angry at LeftPortrait
                doll "Then again, who would want photos of Nicole."
                return

            label .guan_yin_exposition:
                show doll fear at LeftPortrait
                doll "A buddha."
                show doll surprised at LeftPortrait
                doll "This must be the statue that Nicole's mother prays to everyday."
                show doll sad at LeftPortrait
                doll "I wonder what she's praying for..."
                show doll happy at LeftPortrait
                doll "Probably for any daughter that isn't Nicole ahaha!"
        

                    menu defiling:
                        "Actually, this statue seems to be a source of stress for Nicole. I should do something."

                        "Help Nicole.":
                            $ ChangeMalice(1)
                            show doll neutral at LeftPortrait
                            doll "Since Nicole hates it so much when Mother spends so much of her time here then I’ll fix it."

                            ### SFX crash

                            show doll happy at LeftPortrait
                            doll "There! All better."
                            show doll neutral at LeftPortrait
                            doll "Now she won't be able to pray anymore."
                            doll "But she might blame you for this broken statue."
                            show doll happy at LeftPortrait
                            doll "Oops! Hehe."

                        "Don't help Nicole.":
                            show doll sad at LeftPortrait
                            doll "I don’t think Mother would appreciate it if anything were to happen to this."
                            show doll neutral at LeftPortrait
                            doll "I’ll just leave it alone..."
                            show doll angry at LeftPortrait
                            doll "For now."
                return            

            label .sofa_exposition:
                show doll angry at LeftPortrait
                doll "I'm getting rid of that thing as soon as possible."
                show doll happy at LeftPortrait
                doll "But not as soon as Nicole." 
                return

            label .point_and_click:
                init 1:
                    define living_roomPAC_POI = [
                        PointOfInterest("Plants", "living_room.plants_exposition", PointOfInterestImageSet("images/environment/plant/Plant_Hover.png"), BackgroundScale),
                        PointOfInterest("Incense",  "living_room.altar_exposition", PointOfInterestImageSet("images/environment/incense/Incense_Hover.png"), BackgroundScale),
                        PointOfInterest("Guan Yin", "living_room.guan_yin_exposition", PointOfInterestImageSet("images/environment/guan yin/GuanYin_Hover.png"), BackgroundScale),
                    ]
                call screen point_and_click_screen(living_roomPAC_POI)  

    show doll neutral at LeftPortrait
    doll "Hmm... there's nothing interesting left in this room."
    doll "This is not enough. I need to know more about these people."
    show doll angry at LeftPortrait
    doll "Especially Nicole."
    doll "That’s the only way if I am to stay here and become a part of this family."  

    show nicole neutral 
    centered "Nicole was simple enough."
    show emi neutral
    centered "Emi was quite the surprise."
    centered "But there was one last person whose secrets I needed to uncover."
    show mom neutral
    centered "Mother."

label attic:
    show doll neutral at LeftPortrait
    doll "The attic."

    narrator "The inside of the attic was cluttered with boxes and covered in a film of dust. It was a room out of sight but certainly never out of mind for this was the resting place of secrets thought to be lost to time."
    narrator "The doll smiled to herself, this was the perfect place for hidden treasures to be unearthed, and she wasted no time waiting idly."
    narrator "She rummaged through the closest box to her and continued through the room, prying open boxes until she found something that peaked her interest."

    ### SFX RUMMAGING
    scene bg attic

        jump attic.point_and_click

            label .photos_exposition:
                show doll neutral at LeftPortrait
                doll "These look important. Maybe they’re exactly what I’m looking for."

                narrator "The first photo was of a young woman and a man smiling directly at the camera. It looked like a wedding photo."

                show doll angry at LeftPortrait
                doll "Interesting, now why would this be hidden in the attic and not taking its place in the living room?"

                narrator "The next photo was one of Nicole and Emi. The woman behind them must have been their mother but there’s no sign of the father."

                show doll surprised at LeftPortrait
                doll "This is amazing."
                doll "Who would have thought that Nicole was quite the cute child in her early years."
                return

            label .hair_pin_exposition:
                narrator "There was a strange trinket lying amongst the dust. It was now covered in a dull sheen that no doubt used to shine but even with age the elegance of its shape was still evident to the doll."

                show doll sad at LeftPortrait
                doll "A hairpin. The same one worn in the wedding photo, if I’m not mistaken."
                show doll angry at LeftPortrait
                doll "I can’t imagine Nicole ever wearing something as beautiful as this, however I do think it’d suit me."
                show doll happy at LeftPortrait
                doll "I hope mother gifts me something one day."
                return

            label .clothing_trunk_exposition:
                narrator "Neatly folded and looking out of place in the attic were a few garments in various shades of blue. Nadeshiko held them up and realized they weren’t much bigger than her."

                show doll neutral at LeftPortrait
                doll "What's this?"
                show doll surprised at leftPortrait
                doll "Are these baby clothes?"

                centered "No."
                centered "They were not just baby clothes, they were boy clothes."

                show doll surprised at LeftPortrait
                doll "There's a brother? What happened to him?"
                show doll fear at LeftPortrait
                doll "*Gasp* Or maybe..."

                narrator "The doll glanced between the photograph of Nicole and Emi, and the tiny clothes. Suddenly it made sense."

                show doll neutral at LeftPortrait
                doll "Mother must have been expecting a son but ended up with a girl instead."
                show doll sad at LeftPortrait
                doll "How sad... is that why Nicole wears such boyish clothes?"
                show doll angry at LeftPortrait
                doll "I can help make it better."
                return

            label .point_and_click:
                init 1:
                    define atticPAC_POI = [
                        PointOfInterest("Photos", "attic.photos_exposition", PointOfInterestImageSet("images/environment/photos/Photos_Hover.png"), BackgroundScale),
                        PointOfInterest("HairPin",  "attic.hair_pin_exposition", PointOfInterestImageSet("images/environment/hairpin/HairPin_Hover.png"), BackgroundScale),
                        PointOfInterest("ClothingTrunk", "attic.clothing_trunk_exposition", PointOfInterestImageSet("images/environment/clothingtrunk/ClothingTrunk_Hover.png"), BackgroundScale),
                    ]
            call screen point_and_click_screen(atticPAC_POI)

    narrator "Once Nadeshiko was content with what she had discovered there was only one thing left to do."

        menu ruin:
            "What should I do?"

            "Fix the photograph":
                ### SFX SCRATCHING

                show doll angry at LeftPortrait
                doll "There!"
                show doll happy at LeftPortrait
                doll "I think the picture looks much better now that Nicole's out of it!"

                narrator "The doll took the end of the hairpin and dug it into young Nicole’s smiling face."
                narrator "She dragged the sharp end with all her might over and over until there was a gaping hole where there was once Nicole’s face."

                show doll angry at LeftPortrait
                doll "You're not wanted, Nicole."
                show doll neutral at LeftPortrait
                doll "You were never wanted. Not from the beginning, and certaintly not now." 
                show doll happy at LeftPortrait
                doll "This should make you understand."

            "Ignore the photograph":
                show doll neutral at LeftPortrait
                doll "I don’t see how this is important. It’s just a silly old photo!"
                show doll angry at LeftPortrait
                doll "I don’t want to look at this picture anymore." 
                show doll fear at LeftPortrait
                doll "Why do they look so happy?"
                doll "It bothers me."

label lead_up:
    ### SFX MUFFLED THUMPING / FOOTSTEPS

    show nicole neutral at LeftPortrait
    show emi sad at RightPortrait
    emi "Do you hear that?"

    show nicole neutral at LeftPortrait
    nicole "Hear what?"

    ### SFX MUFFLED THUMPING / FOOTSTEPS

    show emi neutral at RightPortrait
    emi "Nick, listen! Someone's up in the attic."

    ### SFX MUFFLED THUMPING / FOOTSTEPS

    show nicole angry at LeftPortrait
    nicole "No there isn-"
    show nicole fear at RightPortrait

    ### SFX MUFFLED THUMPING / FOOTSTEPS LOUDER

    show emi sad at RightPortrait
    emi "See!"
    show emi crying at RightPortrait
    emi "What should we do?"

    show nicole angry at Leftportrait
    nicole "Wait down here. I'll check it out."
    show nicole neutral at LeftPortrait
    nicole "It might just be an animal or something."

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
