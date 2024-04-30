# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character('Toby', color= "#D1FFBD")
define n = Character('Tony', color= "#E0D5F7")
define b = Character('bob', color= "#f5e49c")
define s = Character('Scourge', color= "#ec4040")
define c = Character('Carrie', color= "#f37e24")
define r = Character('Randy', color= "#8d17f5")

# The game starts here.

label start:
    scene bg garden
    queue music "soundtrack.mp3"
    "In a charming garden nestled at the edge of a bustling town, lived a community of plants thriving beneath the sunshine."

    scene bg dirt

    "Living there was were The Turnip Troupe,"
    show toby happy:
        xalign 0.5
        yalign 0.5
    "Toby,"
    show tony happy:
        xalign 0.25
        yalign 0.5
    "Tony,"
    show bob happy:
        xalign 0.75
        yalign 0.5
    "and bob."
    hide bob happy
    hide tony happy
    hide toby happy
    "known for their raging garden parties"
    "They had good company with"
    show radradish:
        xalign 0.5
        yalign 0.5
    "The Rad Radishes"
    hide radradish
    show crunchycarrots:
        xalign 0.5
        yalign 0.5
    "The Crunchy Carrots"
    hide crunchycarrots
    show poppingpotatoes:
        xalign 0.5
        yalign 0.5
    "and The Popping Potatoes"
    hide poppingpotatoes
    "The Turnip Troupe spent most of their day planning their parties and chatting with the local vegetables."
    "Everything seemed perfect until one day, rumors from neighboring gardens start to spread."
    stop music fadeout 0.5
    queue music "scary.mp3"
    show carrie sadtalk:
        xalign 0.25
        yalign 0.5
    c "Did you hear? There's been talk about some kind of bug that has causing trouble in the gardens."
    show randy sadtalk:
        xalign 0.35
        yalign 0.5
    r "I heard that, too. Apparently, it burrows into the roots and just... destroys everything."
    show bob sadtalk:
        xalign 0.5
        yalign 0.5
    n "Did I hear that there is a bug going around?"
    c "Yeah. Hopefully it is just a rumor."

    "There was an sudden eerie sound, like tiny claws scratching against the soil."
    hide bob sadtalk
    hide randy sadtalk
    hide carrie sadtalk
    show weevil:
        xalign 0.75
        yalign 0.5
    "Out from the darkness crawled an evil bug known as Scourge the Evil Weevil."
    s "I've heard a lot about this garden."
    s "Oops wrong garden! Don't worry though, I'll be back for you all"
    hide weevil
    show toby ok:
        xalign 0.5
        yalign 0.5
    show tony ok:
        xalign 0.25
        yalign 0.5
    show bob ok:
        xalign 0.75
        yalign 0.5

    "Later that evening, The Turnip Troupe huddled together, brainstorming ways to defeat the Scourge."
    "Who's idea should we listen to first..."

menu idea:
    "Toby":
        jump tobyidea
    "Tony":
        jump tonyidea
    "Bob":
        jump bobidea

label tobyidea:
    t "Maybe we should create a protective barrier around the garden bed, using twigs and small rocks."
    n "I think Scorge is smarter than that, he could simply burrow under the barrier."
    jump idea
label tonyidea:
    n "Oh I have an idea!"
    n "What if we asked some of the Ladybugs to come stay at our garden to scare Scorge away"
    b "Did you forget Cassie recently got in a fight with the Ladybugs? They are definetly not going to work with us."
    jump idea
label bobidea:
    b "Scourge is smart, but he's also greedy,"
    b "Let's use that against him!"
    jump supplies

label supplies:
    show bg dirt
    stop music
    queue music "soundtrack.mp3"
    hide tony ok
    hide toby ok
    hide bob ok
    "Toby's plan involved creating a decoy root plant, a large hollow clay turnip filled with a sticky sap made from the nearby pine trees."
    show bob happytalk:
        xalign 0.5
        yalign 0.5
    b "Cassie's turnip costume from Halloween would be perfect for this! Let's go ask her."
    hide bob happytalk
    show bob happytalk:
        xalign 0.5
        yalign 0.5
    
    b "Hey Carrie!"
    show carrie sadtalk:
        xalign 0.25
        yalign 0.5
    c "Hey bob."
    b "Do you happen to still have the turnip costume from Halloween?"
    c "Yeah, why?"
    b "I think we have figured out a way to get rid of Scourge once and for all."
    
    "*bob explains the plan to Cassie*"

    c "Sounds like a plan! Here is the costume. If you need any further help you know the Crunchy Carrots got your back."
    t "Actually, do you know any gardens that may have pine trees?"
    c "I forgot which exact one but there are three gardens that could have the pine sap you are looking for."

menu pine:
    "Garden with the animal":
        jump animalgarden
    "Garden with the strawberries":
        jump strawberrygarden
    "Garden with the roses":
        jump rosegarden

label animalgarden:
    scene bg pinedog
    t "Okay, let's head to the garden."
    b "I see the pine trees! Now all we need to do is collect some sap in the costume"
    jump bossfight
label strawberrygarden:
    scene bg strawberry
    b "Okay, let's head to the garden."
    t "I see the strawberries but no trees. Let's head back"
    jump pine
label rosegarden:
    scene bg rose
    n "Okay, let's head to the garden."
    b "Ouch! I just got pricked by a rose. Do you see anything?"
    t "Nope, don't see any pine trees. Let's head back"
    jump pine

label bossfight:
    scene bg dirt2
    stop music
    queue music "scary.mp3"
    show toby ok:
        xalign 0.5
        yalign 0.5
    show tony ok:
        xalign 0.25
        yalign 0.5
    show bob ok:
        xalign 0.75
        yalign 0.5
    b "Let's place it where Scourge burrowed through last time"
    show decoy
    hide toby ok
    hide tony ok
    hide bob ok
    t "Now it's just time to wait and see."
    "*later that night*"
    n "Psst, I think I hear him coming."
    show weevil:
        xalign 0.75
        yalign 0.5
    s "I am back! I know you guys missed me."
    s "Oh my, I have never seen a turnip so big!"
    s "*bites into the decoy*"
    "As soon as he bit into the turnip, the sticky sap gushed out, gluing his mandibles shut and dripping onto his legs, trapping him."
    s "*inaudible noises*"
    "Scourge tried to break free, but the more he struggled, the more stuck he became."
    stop music
    queue music "soundtrack.mp3"
    show bob happytalk:
        xalign 0.75
        yalign 0.5
    b "Aha! We have finally stopped you."
    hide decoy
    hide bob happytalk
    hide weevil
    show bg black
    "The Turnip Troupe banded together and moved the weevil to the surface right before the gardener came up."
    "The gardener saw the weevil in awe; he finally found the culprit that has been destroying nearby gardens." 
    "He scooped up the trapped weevil and took him far away from the garden, where he couldn't cause any more trouble."
    jump end

label end:
    scene bg party
    show toby happy:
        xalign 0.5
        yalign 0.5
    show tony happy:
        xalign 0.25
        yalign 0.5
    show bob happy:
        xalign 0.75
        yalign 0.5
    show radradish:
        xalign 0.25
        yalign 0.25
    show crunchycarrots:
        xalign 0.35
        yalign 0.25
    show poppingpotatoes:
        xalign 0.75
        yalign 0.25
    "The Turnip Troupe were safe again, and the garden returned to its peaceful state."
    "From that day on, The Turnip Troupe kept a close watch for any signs of trouble. And though Scourge the Weevil never returned, they were always ready to defend their beloved garden."
    
    

return    
