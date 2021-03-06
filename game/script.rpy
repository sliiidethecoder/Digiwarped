﻿# The script of the game goes in this file.

# Effects
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define slowflash = Fade(0.5, 0.0, 0.5, color="#fff")
define slowflash0 = Fade(2, 1, 2, color="#fff")


transform fog:
    contains:
        subpixel True
        yalign 0.9
        xalign 0.0
        alpha .7
        HBox ("fog1.png", "fog1.png", "fog1.png", "fog1.png")
        linear 20.0 xpos -2.0
        repeat

    contains:
        subpixel True
        yalign 0.7
        xalign 0.0
        alpha .7
        HBox ("fog2.png", "fog2.png", "fog2.png", "fog2.png")
        linear 40.0 xpos -2.0
        repeat

image lightning:
    "lightning-3058.png"

transform lightning_flashes:
        zoom 2
        parallel:
            yalign 0.0
            choice:
                xzoom 1
                xalign 0.9
            choice:
                xzoom 1
                xalign 0.5
            choice:
                xzoom -1
                xalign 0.1
        parallel:
            alpha 0.0
            linear 0.25 alpha 1.0
            linear 0.25 alpha 0.0
            linear 2
        repeat

image glittering:
        contains:
            "glitter1.png"
            alpha 0.0
            linear 1 alpha 1.0
            linear 1 alpha 0.0
            repeat
        contains:
            "glitter2.png"
            alpha 1.0
            linear 1 alpha 0.0
            linear 1 alpha 1.0
            repeat

transform snowfall:
    contains:
        subpixel True
        yalign 1.0
        xalign 0.5
        HBox ("snowfall1.png", "snowfall1.png")
        linear 20.0 yalign -1.0

    contains:
        subpixel True
        yalign 2.0
        xalign 0.5
        alpha .5
        HBox ("snowfall1.png", "snowfall1.png")
        linear 22.0 yalign -1.0
        repeat

    contains:
        subpixel True
        yalign 2.0
        xalign 0.5
        alpha .7
        HBox ("snowfall1.png", "snowfall1.png")
        linear 32.0 yalign -1.0
        repeat
    contains:
        subpixel True
        yalign 2.0
        xalign 0.5
        alpha .4
        HBox ("snowfall1.png", "snowfall1.png")
        linear 28.0 yalign -1.0
        repeat

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define name = "Aki"
define y = Character(name, color = "#ffffff")

define un = Character("???", color = "#ffffff")

define g = Character("Gryphairmon", color = "#A28FE2")

define h = Character("Holy Digimon", color = "#FFD700")

define m = Character("Monomon", color = "#ff0000")

define w = Character("Weremon", color = "#f7cd62")

define c = Character("Corealmon", color = "#bee8df")

define f = Character("Furizumon", color = "#c6fbff")

image monomon = "monomon_temp.png"
image monomon red = "monomon_temp red.png"

image gryphairmon wings = At("gryphairmon_wings.png", flap)

transform flap:
    xzoom 1 yzoom 1 xalign 0.5
    linear 3 xzoom 0.8
    linear 3 xzoom 1
    repeat

image gryphairmon friendly:
    contains:
        yanchor 0.15
        "gryphairmon wings"
    contains:
        yalign 0.24
        xalign 0.5
        "gryphairmon_body_friendly.png"
    contains:
        xalign 0.495
        yalign 0.263
        yzoom 1
        "gryphairmon_eyes_friendly.png"
        choice:
            4.5
        choice:
            3.5
        choice:
            1.5
        # This randomizes the time between blinking.
        yzoom .8
        yalign 0.272
        "gryphairmon_eyes_friendly.png"
        .005
        yzoom 1
        yalign 0.289
        "gryphairmon_eyes_closed.png"
        .03
        yzoom .8
        yalign 0.272
        "gryphairmon_eyes_friendly.png"
        .005
        repeat

image gryphairmon skeptical:
    contains:
        yanchor 0.15
        "gryphairmon wings"
    contains:
        yalign 0.266
        xalign 0.5
        "gryphairmon_body_skeptical.png"
    contains:
        xalign 0.495
        yalign 0.263
        yzoom 1
        "gryphairmon_eyes_skeptical.png"
        choice:
            4.5
        choice:
            3.5
        choice:
            1.5
        # This randomizes the time between blinking.
        yzoom .8
        yalign 0.272
        "gryphairmon_eyes_skeptical.png"
        .005
        yzoom 1
        yalign 0.289
        "gryphairmon_eyes_closed.png"
        .03
        yzoom .8
        yalign 0.272
        "gryphairmon_eyes_skeptical.png"
        .005
        repeat

image holydigi wings = At("holydigi_wings.png", flap)

image phophetwulvermon praying:
    contains:
        yanchor -0.02
        "holydigi wings"
    contains:
        yalign 0.45
        xalign 0.5
        "holydigi_body_cheerful.png"
    contains:
        xalign 0.5
        yalign -0.210
        yzoom 1
        "holydigi_eyes_cheerful.png"
        choice:
            4.5
        choice:
            3.5
        choice:
            1.5
        # This randomizes the time between blinking.
        yzoom .8
        yalign -0.180
        "holydigi_eyes_cheerful.png"
        .02
        yzoom 1
        yalign -0.150
        "holydigi_eyes_closed.png"
        .03
        yzoom .8
        yalign -0.180
        "holydigi_eyes_cheerful.png"
        .01
        repeat


init:
    $ corealmondaycount = 0


# The game starts here.

label start:

    scene black
    with slowflash
    scene black
    jump whereto

    label intro:
        python:
            name = renpy.input("Enter your name:")
            name = name.strip()

            if not name:
                 name = "Aki"

        "You have logged in as [name]!"

        window hide fade

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg primaryvillage_wut:
        truecenter
        ypos 0.3
        zoom 1.0
        on show:
            zoom 1.0
            linear 3 zoom 0.8

    with slowflash0

    show babydigimon:
        truecenter zoom 1.4
        yalign -0.3
        on show:
            alpha 0.0 zoom 1.5
            linear 2 alpha 1.0 zoom 1.4

    "As you land on the green ground you notice you are no longer alone. The landscape has become unbelievably colorful… And you’re surrounded by dozens of tiny round creatures all looking at you!"

    "What are those?!?!??"

    "A couple of the the strange creatures start bouncing towards you. Somehow it doesn’t seem to think it’s tiring to move like that. Should you be afraid or is it as harmless as it looks?"

    menu:
        "They're so adorable! There’s no way they can hurt you!":
            jump theyreadorable

        "Strange creatures in a strange place? I should be cautious":
            jump strangecreatures

    label theyreadorable:
        "The creatures approach you and you give a small pet on one’s head. It looks happy and makes a purring sound."

        "It really doesn’t look dangerous! Maybe this place isn’t so bad. Even if you’re stuck here you have these guys to keep you company."

    label strangecreatures:
        "You get on your feet and back away. What if it has poisonous skin like one of those African frogs? Then you’d be dead if you these things touch you!"

        "Some of those creatures are caught in surprise but others keep approaching you … "

    un "Heyyy! You..!"

    "Hearing someone call out to you makes you feel glad, it seems to be someone that you can talk to, then ask about these creatures, and where you are right now."

    hide babydigimon
    show bg primaryvillage_wut:
        truecenter
        zoom 0.7
        ypos 0.1

    show gryphairmon friendly:
        xalign 0.5
        yalign 0.1
        zoom .7

    with fade

    "But when you turn around a white gryphon with purple markings stands in front of you. Was the voice coming from this bird creature?"

    un "Why are you looking so confused? Have you never seen a Gryphairmon before?"

    menu:
        "Eh? A…. what ??":
            jump ehawhat

        "Nope. Can’t remember ever seen something like you.":
            jump cantrememberyou

        "You can TALK !?":
            jump youcanTALK

    label ehawhat:
        un "A GRYPHAIRMON! I’m a gryphon Digimon."

        menu:
            "What is a Digimon?":
                jump youdontknow

            "I still don’t get it but… Nice to meet you Gryphairmon!":
                jump stilldontgetit

        label stilldontgetit:
            g "Aw that’s nice of you! By the way… What is your Name?"

            "You introduce yourself to Gryphairmon"

            g "Oh! Sounds pretty nice! So I guess you are not a Digimon but  one of those humans."
            jump youdontknow

    label cantrememberyou:
        show gryphairmon skeptical
        y "Really? Well… I have never seen a Digimon like you either."

        menu:
            "What is a Digimon?":
                jump youdontknow

            "I’m a Human…":
                jump imahuman0

        label imahuman0:
        show gryphairmon friendly
        g "Ohhhh! I’ve heard stories about humans! I should have known that you are not a Digimon! I mean how can you fight without claws and with such blunt teeth?"

        jump youdontknow

    label youcanTALK:
        "Obviously. Many Digimon at the Rookie level can talk."
        menu:
            "Digimon? Rookie? What are you talking about??":
                jump youdontknow

            "Sorry… I’ve just never seen a ”Digimon“ like you and I’ve never talked with one!":
                jump iveneverseen

        label iveneverseen:
            "So this if your first time talking to a Digimon? That’s cool! So you must be one of those humans…"
            jump youdontknow

    label youdontknow:
        show gryphairmon friendly
        "Ah I see! You don’t know what a Digimon is, right? Well, for starters you are in the Digital World! Digiworld for short. And this World is inhabited by digital monsters called Digimon!"

        "The little Digimon that just welcomed you are Baby-Digimon. Digimon can digivolve and become stronger, reaching higher levels. I’m a Rookie Digimon and I take care of the little Baby-Digimon"

        "So… how did you come to Primary Village?"

    "You explain to Gryphairmon what happened"

    g "Uhh… Okay… "

    g "I understand… I guess."

    g "Well then, that makes you are our guest! Come with me!"

    g "We need to find a place for you to stay while visiting our world!"

    menu:
        "Thank you very much!":
            jump tyvm

        "Well… to be honest I want to go back home.":
            jump iwanttogohome

    label tyvm:
        "You’re welcome! Come, I will bring you to toy town where you can stay! Uh, I have an idea! After that I should bring you to the sanctuary! There is a holy Digimon who may have some information about your mysterious appearance! Also, maybe he can find a way for you to get home again."

    label iwanttogohome:
        "Aw, I’m sorry to hear that but I don’t know how you can get home. Come, I will bring you to ???  where you can stay for now! Uh, I have an idea! Maybe the holy Digimon in the Sanctuary has some information about your mysterious appearance!"

    "I will take you there after that!"

    scene bg room:
        truecenter zoom 0.4
    hide gryphairmon friendly

    g "Here we are! This will be your new room, I hope ya like it! Feel free to look around, I will be outside waiting."

    show gryphairmon friendly:
        left
        xanchor 0.5
        ypos 0.65
        xpos 0.3
        zoom 0.45

    g "Oh Great, you are ready! Now come, I will take you to the Sanctuary in Freezeland. I should warn you, It will be very cold!"

    scene bg sanctuary_entrance:
        zoom 1.3
    show gryphairmon friendly:
        yanchor 0.6
        zoom .6
        xalign 0.5
        ypos 0.6

    show image snowfall

    g "Brrrrr, so cold! Look we are in front of the majestic Sanctuary. Don’t be shy, just go inside! The holy Digimon will be in there I have to go back now and look after the Baby-Digimon. Good luck!"

    hide gryphairmon friendly
    label sanctuary:
        scene bg sanctuary_hall:
            truecenter zoom 0.5
        with slowflash0
        show glittering:
            zoom 0.8

        show phophetwulvermon praying:
            truecenter zoom 0.5

        "There is a Digimon in the middle of the hall with it’s back toward you. It looks as if they might be praying to the statue."

        "As you walk towards it the Digimon turns around with it’s eyes closed. He starts talking in a relaxed pace."

    h "I have foreseen your arrival, destined one"

    h "Thou who has come from a land that is both incredibly far and incredibly close.
    Thou who shall lift the veil of darkness from this world and bring back light"

    h "I welcome you on behalf of the Digimon gods, and shall tell you about the quest bestowed upon you"
    show black:
        alpha 0.7
    play sound "sounds/thunder2.mp3"
    show white:
        alpha 0.0
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.0
        linear 2
        repeat
    show lightning at lightning_flashes

    show delegamon_silhouette:
        truecenter zoom 1.3
        on show:
            ypos 0.5
            linear 2 ypos 0.48
            linear 2 ypos 0.5
            repeat
    with flash

    h "I have seen a great darkness coming to this world. A powerful evil force is planning to take control over everything, causing a great deal of misery to the peaceful inhabitants of our island. You are our last hope!"

    h "The only way to stop it is with your help, and so I must ask you, destined one. Won’t you lend us your strength and help us?"

    menu:
        "Of course I will!":
            jump ofcourseiwill

        "Wait, what do I have to do exactly?":
            jump whatdoido

        "No thanks.":
            jump nothx

    label ofcourseiwill:
        "That’s a relief to hear!"
        jump explanation

    label whatdoido:
        "Oh of course! I’ll explain"
        jump explanation

    label nothx:
        "*gasp* But you are the destined one! Please hear me out."
        jump explanation

    label explanation:
        hide lightning at lightning_flashes
        hide delegamon_silhouette
        hide white
        hide black
        with fade

        h "You are the only one who can help us. In 32 days, the portal to the other world will open and evil will strike. You have until then for saving not just one world, but two."

    h "And how do you do this you ask? You need to find a partner, a Digimon who you’re compatible with."

    h "You see, we Digimon get stronger over time, but the bond between human and Digimon will not only make us grow stronger more swiftly, but together you shall gain unimaginable power. You’ll see when you find the right Digimon!"

    h "You will likely need to form a bond of friendship with the Digimon before hand. If it’s strong enough, you can lend each other power. There are plenty of nice Digimon who’d love to meet you! I’m sure you’ll make a lot of friends here!"

    h "Ah! Before you go, allow me to I will upgrade your digivice!"

    h "...Ah, of course! I’m talking about the thing in your pocket that brought you to the Digiworld. Let me see it for a moment!"

    "Before you realize it, you have already handed the digivice over to him. The Digimon adds a small chip into your Digivice and hands it back to you."

    h "There! It will now allow you to get around in the Digital World. Feel free to explore as much as you like!"

    "You take a look at your digivice. Where do you want to go?"
    jump whereto
    label whereto:
        show digivice_tri:
            truecenter zoom 4

        menu:
            "Intro":
                jump intro

            "Snowfields":
                jump snowfields

            "Bridge to temple":
                jump badlands

            "Oasis":
                jump oasis

            "Freezetown":
                jump freezetown



    #monomons route, badlands ----------
    label badlands:
        scene bg bridge:
                truecenter zoom .7

        with fade
        window hide fade


        centered "Seeing the Temple in the distance you decided to walk towards it, you think there might be people there, or at least someone who could help you."

        centered "As you’re making your way towards your destination you find yourself in a place almost completely desolated."

        scene bg wasteland

        show image fog:
            on show:
                xalign 0.5
                alpha 0.0
                linear 30 alpha 1.0

        centered "The ground is dry and weary and there seems to be no sign of life, the atmosphere seems eerie as fog seems to roll around the already haunted landscape."

        centered "Feeling a shiver down your spine you start to realize that maybe you’re not supposed to be here."

        menu:

            "I have a bad feeling… Maybe I should go back…":
                jump badfeeling

            "I have to keep going, the temple can’t be too far now!":
                jump keepgoing

        label keepgoing:

            "You keep wandering and find that you’ve passed the same rock twice, maybe five times now? The air feels heavy and you feel like somebody's been watching you."

            "Now that you think about it the feeling was always there but now it’s so strong to cannot help but feel paranoid…"

            jump badfeeling

        label badfeeling:

            "Feeling unsafe and vulnerable you decide that it’s time to head back to the village for now, next time you’ll take a different route in order to avoid this creepy place."

        "The fog has appeared to get heavier now and you are all turned around, you can no longer see the large bridge that you crossed to get here."

        show redlight:
            truecenter zoom 0.1
            linear 20 zoom 0.4
        with slowflash

        "Feeling hopelessly lost you wonder if you’ll ever find you way out… Wait what’s that?"

        "Seeing the red light in the distance fills you with dread, was this thing watching you the entire time!?"

        "You hear footsteps approaching you, a slight squish to their steps, unsuited to anything that would live in this environment."

        show monomon red:
            truecenter zoom 0.5
            on show:
                xalign 0.5
                alpha 0.0
                linear .5 alpha 1.0
        with slowflash

        "You almost freeze in place from the sounds and the sight for this creature, you can kind of make it out-"

        "Oh no, are those tentacles!?"

        menu:

            "RUN FOR IT!":
                jump runforit

            "Freeze in fear":
                jump freezeinfear

        label runforit:

            "You’re not going to stick around to find out what kind of digimon is approaching you, or see if it even is a digimon."

            "You run through the dense fog as fast as you can, but it sounds like the footsteps aren't far behind, it’s gaining on you!"

            "You feel the adrenaline rushing through your veins as you try and make your escape from whatever that creature was, but you're so focused on running that you trip over something and wipe out."

            "You roll a bit as you fall over, landing on your side. You feel pain in one of your legs, you hope you didn’t cut yourself. As you try to get up you realize how disoriented you are, just how far did you roll?"

            "You try to get back up quickly but it’s too late now, you close your eyes in fear of what might happen."

        label freezeinfear:

            "You cannot move as you watch it close in on you, your legs turning to stone as you can only look at the ominous glow like a deer in headlights."

            "It feels like you’re heart is beating out of your chest the closer it gets to you and you begin to wonder when your life will start flashing before your eyes."

            "You feel your legs shaking under you and give in under you. Falling on your rump you take one last glimpse at the silhouette before looking away and closing your eyes, prepared for the worst."

        # This shows a character sprite. A placeholder is used, but you can
        # replace it by adding a file named "eileen happy.png" to the images
        # directory.

        hide redlight
        show monomon:
            truecenter zoom 1
        with fade

        # These display lines of dialogue.

        m "Hey what’s wrong, are you okay?"

        "You open your eyes to the concerned, childish voice in surprise. Seeing the rookie digimon fretting over you puts you at ease, it seems like the glowing light you saw was from the strange device attached to their chest."

        m "Sorry if I scared you, not many digimon come here so I was surprised! Do you need help getting up?"

        "The digimon then offers you a helping... Hand?"

        "It seems like the tendrils wrapping around the arms also function as fingers, they look slimy and if you’re honest with yourself look like they would feel gross and cold."

        menu:

            "Take the digimon’s… Hand":
                jump takethehand

            "It’s okay I can uh, get up myself":
                jump icangetup

        label takethehand:

            "You accept the help to get back on your feet and put out your arm."

            "You feel the tentacles wrap around your hand and wrist for a better grip. At first it seems scary but despite the look of them they are not slimy at all; they’re actually soft and warm like humans hand would be."

        label icangetup:

            "The cephalopod-like digimon withdraws their ‘hand’ and you get back on your feet without trouble, dusting yourself off. There seems to be sadness in their eyes, or is that just your imagination?"

        "Once you’re all settled they seem relieved, almost happy to see you."

        m "I’m glad you’re okay, my names Monomon nice to meet you!"

        "They smile widely at you with a chipper attitude, you can only guess that they don’t get a lot of company around here which is why they’re so happy to see you."

        m "What’s your name? I’ve never seen a digimon like you before!"

        "They keep they’re happy-go lucky spirit when they talk. Wait, did they just call you a digimon!?"

        menu:

            "My name is [name] and I’m human, nice to meet you too!":
                jump mynameis

            "I’m not a digimon":
                jump notadigimon

        label notadigimon:

            "Monomon’s expression changes in an instant"

            m "Huh, what? Not a digimon!?"

            "They seem surprised and shocked like you’ve told them something blasphemous, have they not seen a human before? The digimon you interacted with before seemed to know you were human right away…"

            y "Yup, and my name’s [name] by the way."

        label mynameis:

            y "My name is [name] and I’m human, nice to meet you too!"

        "Monomon tilts their head at you before walking around you, checking you from every angle. When they come back in front of you they’re smiling again."

        m "Wow that’s so cool I never met a Hoomin before!"

        y "...It’s human and you can just call me [name]"

        m "Okay [name]! Let’s become great friends okay!"

        "You cannot help but smile at the strange rookie, even if they’re appearance is strange you cannot help but think that they’re cute… well only a little anyways."

        "Quickly you remember the ruins you were heading to, Monomon might be able to help guide you through here since they seem to live here."

        y "Um, originally I was heading to the ruins past here, do you think you can direct me there?"

        "Monomon hesitates for a moment as if they don’t know what to say, their smile also disappears and is replaced with an apologetic expression."

        m "Uh, well I can lead you there but…"

        "They look away while they hesitate."

        m "Nobody really lives there anymore, it’s practically abandoned. There’s rumors of a digimon that lives there but… They’re not a friendly digimon from what I’ve heard. Sorry for not being much help."

        "Well it was worth a try but luckily your journey wasn't for nothing, you got to meet Monomon after all!"

        y "That’s okay! I’m glad I ran into you, if I didn’t I would have headed to the ruins for nothing or get eaten up by that rumored digimon you spoke of."

        "When you speak about the rumored digimon Monomon seems uncomfortable, but they quickly brush it off and go back to being their cheerful self."

        m "No problem, um, will you be sticking around?"

        "They look at you with puppy eyes while they say this, you really must go back but it’s hard…"

        "Well it’s not actually that hard to say no to them, their appearance is still rather off putting."

        menu:

            "Sorry I have to go…":
                jump ihavetogo

            "I can’t, but I’ll come back and visit!":
                jump illcomevisit

        label ihavetogo:

            y "Sorry I have to go…"

        label illcomevisit:

            y "I can’t, but I’ll come back and visit!"

        "Monomon seems a little disheartened to hear those words but manages to keep smiling."

        m "That’s okay, it’s just nobody comes here. I haven’t seen another digimon in forever… Much less a human."

        "They sound quite lonely but you must be on your way. Now that you know you can find a friendly digimon here this place doesn't seem so bad, even if still looks depressing."

        y "But first, can you lead me back to the bridge? I’m still a little lost…"

        m "Of course!"

        "Monomon answers happily as they start skipping along, you sigh at their enthusiasm and begin to follow."

        "You feel much more relieved when you leave the Badlands and reach the bridge, Monomon somehow manages to seem happy and sad at the same time."

        m "Promise to come and visit? Please make it sooner than later!"

        "You smile and tell Monomon that you will try your best. You then wave goodbye and part ways… They seemed like a nice digimon but the place they were in, you let your thoughts wonder on why Monomon lives in the Badlands alone as you head back to the village."

        jump whereto

    #weremons route, snowfields ----------
    label snowfields:
        scene bg snowfields:
            truecenter
            zoom 1.2

        show image snowfall
        "You peacefully walk through the snow, marvelling at the mountanous landscape."
        with flash
        "suddenly a snowball hits you right in the face. You wipe the snow off your face and try to find who or what threw it at you."

        "You can't see anyone."

        menu:
            "Keep looking":
                jump keeplooking

            "Leave before you get hit by another one":
                jump leavebeforeyougethit

        label leavebeforeyougethit:
            "You make a run for it before another snowball appears."
            jump whereto

        label keeplooking:
            show weremon:
                truecenter
                zoom 0.5
            "You notice a wolf-like digimon eagrly digging in the snow. They must be the one that threw the snowball."
            menu:
                "Throw snowball back":
                    jump throwback

                "Tell him not to throw any more snowballs at you":
                    jump dontthrow
            label throwback:
                with flash
                w "Hey, why'd you do that?!"

                "You explain that you were settling the score with him and throw another snowball at him."
                with flash

                "You both spend the next few minutes having a snowball battle."

                "After a little while you say bye and walk away"

                jump whereto
            label dontthrow:
                "The Digimon throws another snowball in your face. You decide to leave for the day so you wouldn’t get anymore snowballs in your face."

                jump whereto

    #corealmons route, oasis -----------
    label oasis:
        if corealmondaycount == 0:
            scene bg desert0:
                zoom 1.2
            with flash

            "A calm-looking sea of sand is laid out in front of you as everything comes into view. Looking around, you see a little oasis. The heat is already getting to you, but you wonder what could possibly be out here."

            menu:
                "Go to the oasis":
                    jump gotooasis

                "Head back":
                    jump whereto

            label gotooasis:
                "You start walking, curiosity getting the better of you as your legs carry you to the small lake."

                scene bg oasis:
                    zoom 1.2
                with dissolve

                "Once you reach the pool you immediately feel cooler as the shade of the palm trees wash over you. You enjoy the warm breeze before something grabs your attention, a splash in the water."

            menu:
                "Investigate":
                    jump investigate

                "Head back":
                    jump whereto

            label investigate:
                $ corealmondaycount += 1

                scene cg splash
                with flash

                "Cautiously, you walk closer to the lake before something bursts out, drenching you in water."

                "It takes you a moment to gather yourself after the sudden movement, but you look into the water to see a pair of eyes looking guiltily at you."

                scene bg oasis:
                    zoom 1.2
                with dissolve

                show corealmon:
                    zoom 0.5
                    xalign 0.5
                    yalign 1
                    alpha 0
                    linear 2 yalign 0.5 alpha 1

                "They slowly rise as the creature makes it's way out of the water, revealing a blue seal-looking thing with a seashell mounted on it's head."

                "It looks up at you."

                un "I'm really really sorry! I didn't know anyone was here, and it was a nice day, and I just thought- Oh..I'm super sorry, no one ever comes out here so I just thought.."

                "He looks like he's silently kicking himself for being so careless."

                y "It's alright, really! I'm sure I'll dry off fast with the heat."

                "His worried expression changes to one of relief as he smiles awkwardly."

                un "Oh! That was rude of me...I'm Corealmon, what's your name?"

                "You introduce yourself."

                c "How nice, I hate being so blunt but I think you might want to leave. It gets pretty hot in the afternoon."

                "You look up at the sun, and suddenly remember the heat. You decide it probably is a good idea to leave, so you say goodbye and open your map."

                jump whereto
        if corealmondaycount == 1:
            scene bg oasis:
                truecenter
                zoom 1.2
            with dissolve

            "You look around expecting to see Corealmon in the water like yesterday, but he's sitting next to the lake on a blanket with the winged wolf you saw when you first came here."

            show corealmon:
                zoom 0.5
                xalign 0.7

            "He spots you out of the corner of his eye and smiles, beckoning you closer."

            c "Hello again!"

            "He grins at you while the wolf looks you up and down"

            c "Fancy seeing you here."

            "He chuckles, as he takes a bite of what looks to be a sandwich."

            c "Oh, where are my manners? Your welcome to have a seat and a snack."

            "Corealmon says as he moves at make room for you."

            menu:
                "Sit and eat with them":
                    jump sitandeat
                "Leave":
                    jump whereto

            label sitandeat:
                "You sit down and take a sandwich."

                jump whereto

    #furizumons route, freezetown -----------
    label freezetown:
        scene bg snow:
            truecenter
            zoom 0.8
        with slowflash
        show image snowfall

        "It's very cold. Do you wish to keep going?"
        menu:
            "Yes":
                jump yeskeepgoing
            "No":
                jump nodontkeep

        label yeskeepgoing:
            show white:
                alpha 0
                linear 3 alpha 1

            "You continue through the icy landscape, only to succumb to the cold and black out…"

            centered "{color=#477d82}Hey, Wake up! C’mon, wake up!{/color}"

            scene cg furizuappears:
                truecenter
            show white:
                alpha 1
                linear 3 alpha 0

            "That was a close one, kid. Your skin was cold as ice."
            jump freezetowntown

        label nodontkeep:
            "You decide to hunker down for the night. A snowstorm passes overhead, but you are left unharmed."

        label freezetowntown:
            scene bg freezetown:
                truecenter
                zoom 0.8
            with dissolve
            show furizumon:
                truecenter
                zoom 0.55
            show image snowfall

        f "Hello!"


    # This ends the game.

    return
