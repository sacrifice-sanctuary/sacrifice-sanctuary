init python:
    from Profile import Profile, BloodType, Gender, CharacterStatus
    from datetime import date

# The script of the game goes in this file.

define fastDissolve = Dissolve(0.3)
define dissolve2 = Dissolve(0.6)
define FD2 = { "master" : Dissolve(0.2) }

define flashbulb = Fade(0.2, 0.0, 0.4, color='#dddddd')

default bleep = True


init python:

    renpy.music.register_channel("Bleep", mixer="voice")

    def beepHT(event, **kwargs):
        if event == "show":
            renpy.music.play("beep1.ogg", channel="Bleep", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="Bleep")


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ht = Character("Helpful Tips", color="3366FF", who_outlines=[(2, "02648C", 0, 0)], what_outlines=[(1, "5B707B", 0, 0)]) #, callback=beepHT red=ED1C24, green=22B14C, purple=A349A4, orange=FF7F27, blue=00A2E8
define uk = Character("???", color="666666", who_outlines=[(2, "333333", 0, 0)], what_outlines=[(1, "777777", 0, 0)])
define np = Character("Pandora", color="2092C8", who_outlines=[(2, "0284BC", 0, 0)], what_color="0784B9", what_outlines=[(1, "02648C", 0, 0)], alt="Pandora thoughts")

define pk = Character("Pandora", color="00A2E8", who_outlines=[(2, "0284BC", 0, 0)], what_outlines=[(1, "5B707B", 0, 0)])
define dk = Character("Darya", color="00A2E8", who_outlines=[(2, "0284BC", 0, 0)], what_outlines=[(1, "5B707B", 0, 0)])
define eb = Character("Emilio", color="00A2E8", who_outlines=[(2, "0284BC", 0, 0)], what_outlines=[(1, "5B707B", 0, 0)])
define fc = Character("Florus", color="00A2E8", who_outlines=[(2, "0284BC", 0, 0)], what_outlines=[(1, "5B707B", 0, 0)])

define bl = Character("Belinda", color="22B14C", who_outlines=[(2, "188638", 0, 0)], what_outlines=[(1, "506C58", 0, 0)])
define ds = Character("Dexter", color="22B14C", who_outlines=[(2, "188638", 0, 0)], what_outlines=[(1, "506C58", 0, 0)])
define av = Character("Ainsley", color="22B14C", who_outlines=[(2, "188638", 0, 0)], what_outlines=[(1, "506C58", 0, 0)])

define rh = Character("Ratna", color="ED1C24", who_outlines=[(2, "B1171D", 0, 0)], what_outlines=[(1, "6C4D4E", 0, 0)])
define nl = Character("Nikolas", color="ED1C24", who_outlines=[(2, "B1171D", 0, 0)], what_outlines=[(1, "6C4D4E", 0, 0)])
define ff = Character("Fabrice", color ="ED1C24", who_outlines=[(2, "B1171D", 0, 0)], what_outlines=[(1, "6C4D4E", 0, 0)])

define of = Character("Osanne", color="A349A4", who_outlines=[(2, "783678", 0, 0)], what_outlines=[(1, "725872", 0, 0)])
define ka = Character("Kevin", color="A349A4", who_outlines=[(2, "783678", 0, 0)], what_outlines=[(1, "725872", 0, 0)])
define vl = Character("Valkyrie", color="A349A4", who_outlines=[(2, "783678", 0, 0)], what_outlines=[(1, "725872", 0, 0)])

define cm = Character("Carwyn", color="FF7F27", who_outlines=[(2, "C4621F", 0, 0)], what_outlines=[(1, "7A6659", 0, 0)])
define nt = Character("Nin", color="FF7F27", who_outlines=[(2, "C4621F", 0, 0)], what_outlines=[(1, "7A6659", 0, 0)])
define dh = Character("Dakota", color="FF7F27", who_outlines=[(2, "C4621F", 0, 0)], what_outlines=[(1, "7A6659", 0, 0)])

define mm = Character("Maizey", color="7A4C0E", who_outlines=[(2, "523309", 0, 0)], what_outlines=[(1, "52493E", 0, 0)])

#~TRANSFORMS~#
transform centre:
    xalign 0.5
    yalign 1.0

transform twoleft:
    xpos 50
    yalign 1.0

transform tworight:
    xpos 800
    yalign 1.0

transform threeleft:
    xpos -100
    yalign 1.0

transform threeright:
    xpos 1000
    yalign 1.0
#the threes are unlikely to be used bc they make the screen very cramped due to the large sprite size

#############
# VARIABLES #
#############
default teamcol = "n" #for setting team colour for when that matters for the UI
default uivis = True #dont entirely remember when this is used
default wiggle = True #arrow wiggle variable for moving arrows in the halls


default selection = 0
default EC = ["string test", "evil test"]

default clues = {
    0 : "Woke up in Strange Room",

}

default clues_text = [
    ["After being grabbed by a mysterious person I woke up in a strange room and covered in bruises."],
    ["The door to my room was unlocked, and I couldn't find a key anywhere. I can leave whenever I want but can't barricade myself in."], 
    ["The bed, table, and chair of this bedroom are of noticably low quality: the whole room feels somewhat half-arsed in construction."], 
    ["The bedroom wardrobe has multiple copies of my custom outfit. While convenient for a long-term stay it does bring up some troubling implications."], 
    ["There's a spikey cactus on a chest of drawers despite there being no windows, it's probably going to die from lack of sunlight soon."],
    ["This doodle of Maizey seems weirdly out of place, but it can't be here for no reason."],
    ["The speaker on the wall here seems to imply someone might try to contact us at some point, but I can't see any buttons on it for it to be a functioning intercom system."],
    [""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""]
    ]


default ch1murder = {
    0 : "[[Wet logs]",
    1 : "TWO bodies",
    2 : "yikes"

}

default ch1murder_text = [
    ["In the oven"],
    ["Two of them"],
    ["murder :[["]
    ]


#~flags~#
default daryaroom = False #is darya in the room right now?

default flagA = 0 #simple progression 1

default pp = True #prologue progression (for dumb button stuff)

default day = 1 #in case we need this for optionally-out-of-order event shenanigans


#~locations~#
default currentlocation = "" #where you currently are

default pandoraroomread = [0,0,0,0,0,0,0,0,0,0,0] #0=door, 1=wardrobe, 2=bed, 3=table, 4=chair, 5=note, 6=drawers, 7=bin, 8=cactus, 9=clock, 10=speaker
default corrA1read = [0,0,0,0,0,0,0] #0=pandoor, 1=flodoor, 2=dardoor, 3=nikdoor, 4=toidoor, 5=toilet sign, 6=dorm sign
default corrB1read = [0,0,0,0,0,0,0] #0=closet, 1=emidoor, 2=cardoor, 3=dakdoor, 4=fabdoor, 5=shodoor, 6=shower sign
default corrC1read = [0,0,0,0,0,0] #0=X1door, 1=nindoor, 2=dexdoor, 3=beldoor, 4=X2door, 5=ratdoor
default corrD1read = [0,0,0,0,0,0] #0=kevdoor, 1=valdoor, 2=aindoor, 3=osadoor, 4=X3door, 5=X4door

default corrDdoorread = [0] #0=blocked door

default corrF1read = [0] #0=nin

default recroomeread = [0,0,0,0] #0=shelves, 1=pc, 2=belinda, 3=osanne

default dhallread = [0] #0=carwyn

default kitchenread = [0] #0=nikrat

default medbayread = [0] #0=valkev

default corrH1read = [0] #0=exit door


#~interactable totals~#
default asktotal = 0 #generally talking to people total
default roomtotal = 0 #generally interacting with things total


#~Profiles Data~#
default allowedP = True 
default pactive = True

# See Profile.py for more information on this class.
default profiles = {
    "ainsley" : Profile("Ainsley Velos", Gender.FEMALE, "'Mustelid'", "N/A", date.fromisoformat("2030-01-07"), 157, 52, BloodType.O_NEG),
    "belinda" : Profile("Belinda Lizforth", Gender.FEMALE, "'Crocodillian'", "Herpetology Zoologist", date.fromisoformat("2023-04-03"), 178, 80, BloodType.B_POS),
    "carwyn" : Profile("Carwyn Moss", Gender.MALE, "'Ibex(Goat?)'", "Published Author", date.fromisoformat("2025-12-06"), 173, 66, BloodType.O_POS),
    "darya" : Profile("Darya Kidwell", Gender.FEMALE, "'Bat-like'", "Ferry Captain", date.fromisoformat("2027-06-26"), 170, 67, BloodType.AB_NEG),
    "dexter" : Profile("Dexter Salvage", Gender.MALE, "'Gliding Lizard'", "Commercial Airline Pilot (Former)", date.fromisoformat("2024-02-29"), 168, 71, BloodType.O_NEG),
    "emilio" : Profile("Emilio Hawson Barnes", Gender.MALE, "'Small Feline'", "Livestock Farmer", date.fromisoformat("2025-10-14"), 183, 73, BloodType.O_NEG),
    "fabrice" : Profile("Fabrice Fulton", Gender.MALE, "'Swan'", "Professional Origamist", date.fromisoformat("2029-11-11"), 177, 54, BloodType.O_NEG),
    "florus" : Profile("Florus Claude", Gender.MALE, "'Butterfly'", "Contract Gardener", date.fromisoformat("2022-04-12"), 172, 59, BloodType.A_POS),
    "kevin" : Profile("Kevin Atwood", Gender.MALE, "'Horseshoe Crab'", "Student Nurse", date.fromisoformat("2027-09-30"), 165, 56, BloodType.B_NEG),
    "nikolas" : Profile("Nikolas Lambert", Gender.MALE, "'Spider or Tarantula'", "Apprentice Cartographer", date.fromisoformat("2030-07-25"), 160, 54, BloodType.AB_POS),
    "nin" : Profile("Ninhursag Talus", Gender.FEMALE, "'Kingfisher'", "Speleologist", date.fromisoformat("2024-09-11"), 167, 69, BloodType.A_POS),
    "osanne" : Profile("Osanne Foxglove", Gender.FEMALE, "'Violet Ground Beetle'", "Biochemist (Botany Specialisation)", date.fromisoformat("2024-10-31"), 162, 51, BloodType.O_POS),
    "pandora" : Profile("Phantom Magpie", Gender.FEMALE, "'Common Eurasian Magpie'", "Unknown", date.fromisoformat("0001-01-01"), 0, 0, BloodType.UNKNOWN),
    "ratna" : Profile("Ratna Harlow", Gender.NEUTRAL, "'Jerboa, not mouse'", "Apprentice Paleontologist", date.fromisoformat("2029-05-10"), 161, 61, BloodType.A_POS),
    "valkyrie" : Profile("Valkyrie Laskea", Gender.FEMALE, "'Monitor Lizard'", "Cyber Security Technician", date.fromisoformat("2028-01-31"), 161, 59, BloodType.O_POS),
    "dakota" : Profile("Dakota", Gender.MALE, "N/A", "Working Horse", date.fromisoformat("2043-10-20"), 16.1, 532, BloodType.QA_POS),
    "maizey" : Profile("Maizey", Gender.FEMALE, "N/A", "Bunker Host", date.fromisoformat("0001-01-01"), 200, 85, BloodType.ELEC)
}

default profileselect = list(profiles.keys())[0] # Default to the first entry, rather than hardcoding it as "ainsley"

#~Map Stuff~#
default mactive = False

default strintloc = "0"
default bigx = 0
default bigy = 0

default dmap1 = { #compares current location to this dict lookup, then the number string is converted into co-ords for the character position dot
    "corrA1" : "08100350",
    "corrA2" : "08100510",
    "corrA3" : "07300510",
    "corrC1" : "08100140",
    "corrC2" : "08100300",
    "corrC3" : "08250110",
    "corrC4" : "07300110",
    "corrB1" : "05100350",
    "corrB2" : "05100510",
    "corrB3" : "05800510",
    "corrD1" : "05100140",
    "corrD2" : "05100300",
    "corrD3" : "04700110",
    "corrD4" : "05800110"
}


#########################
# The game starts here. #
#########################

image splash1 = "splash1.png"
image splash2 = "splash2.png"
image splash3 = "splash3.png"

label splashscreen:
    scene black
    with Pause(1)

    show splash1 with fade
    with Pause(3)

    show splash2 with fade
    with Pause(5)

    show splash3 with fade
    with Pause(3)


    scene black with fade

    with Pause(1)

    return

screen keyscr: #code source: https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=22458&p=283744&hilit=movie+skip#p283744
    key "K_RETURN" action Hide("nonexistent_screen")
    key "K_KP_ENTER" action Hide("nonexistent_screen")
    key "K_SPACE" action Hide("nonexistent_screen")
    
    key "mousedown_4" action Hide("nonexistent_screen")
    key "K_PAGEUP" action Hide("nonexistent_screen")
    key "mousedown_5" action Hide("nonexistent_screen")
    key "K_PAGEDOWN" action Hide("nonexistent_screen")
    
    key "mouseup_3" action Hide("nonexistent_screen")
    key "mouseup_1" action Hide("nonexistent_screen")

    key "K_ESCAPE" action Return("smth")

label start:
    stop music

    $ quick_menu = False
    
    #intro stuff goes here

    show screen keyscr

    #play opening movie
    $ renpy.movie_cutscene("images/opening.ogv")

    hide screen keyscr

    #play ch1 screen - dont actually it's out of place here, it should go after the intro section
    #$ renpy.movie_cutscene("chapter1.ogv")

    scene black

    pause 1.5

    np "..."
    np "Given what just happened, I'm fairly certain I've been arrested."
    np "But this doesn't seem like any prison cell I've been in before."
    np "I don't even think that was a police helicopter, I've never just been paralysed and thrown into a van."
    np "Usually they at least have the courtesy to handcuff me and give me something to sit on."

    $ currentlocation = "pandora"


    image PR = "bg pandora_full.png"

    window hide dissolve

    scene black with dissolve

    #pause 0.2

    show PR with dissolve:
        blur 30

    #np "My vision is still blurry from waking up."

    pause 0.2

    scene black with dissolve

    pause 0.2

    show PR with dissolve:
        blur 10

    pause 0.2

    scene bg pandora_full with fade

    window auto

    np "I blink to clear my head and get a better look at where I find myself. {alt}Description: The room appears to be some sort of dorm, to the left is a bed and a wardrobe, at the back of the room is a small bin, a speaker on the wall, a table with a note on it and a chair. To the right is a metal door, a chest of draws with a cactus on it, and a clock mounted on the wall. The walls appear to be made out of metal plates.{/alt}"
    pk "Since I don't know anything right now, I should check out everything in this room and see if there's anything that tells me where I am."

    #bl "test"

    #rh "test"

    #of "test"

    #cm "test"

    #uk "test"

    #mm "test"

    pk "My left forearm stings a bit and feels itchy, but I think I just landed on it. For now I need to prioritise knowing my surroundings."
    pk "I'll make note of anything that seems especially important."

    ht "Anything that can be clicked on will highlight when you hover over it."
    ht "Most interactables will have a second dialogue on re-prompting, but never a third. Though, as the story progresses new dialogue may be present."
    ht "Pandora will note down things she deems important in the 'clues' section of the quick menu on the left."
    ht "Press the help button to view the controls, and other helpful information, at any time. {alt}Use the up and down arrow keys to cycle through interactables that are on-screen (menus, clickable objects, etc.).{/alt}"


    #dk "eagvnaerjsi"
    #eb "erovbeuosiprep"
    #fc "ivasbjfolvbnv"

    
    "Notes on 'Woke up in Strange Room' jotted down."
    
    $ quick_menu = True

    play music "audio/lonely room.mp3" fadein 1.0

    jump draw_pandora_room


#==============#
# PANDORA ROOM #
#==============#

screen pandora_room:
    add "bg pandoraroom"

    imagebutton:
        xpos 1332
        ypos 248

        focus_mask True

        auto "pandora_door %s"

        alt "A metal door, with a small peephole in the middle"

        action Jump("pandora_door")

    imagebutton:
        xpos 80
        ypos 240

        focus_mask True

        auto "pandora_wardrobe %s"

        alt "A wooden wardrobe"

        action Jump("pandora_wardrobe")
        
    imagebutton:
        xpos 0
        yalign 1.0

        focus_mask True

        auto "pandora_bed %s"

        alt "A wooden bed. The covers and pillow are grey."

        action Jump("pandora_bed")

    imagebutton:
        xpos 632
        ypos 504

        focus_mask True

        auto "pandora_table %s"

        alt "A wooden table. There is a small drawing on top"

        action Jump("pandora_table")

    imagebutton:
        xpos 900
        ypos 472

        focus_mask True

        auto "pandora_chair %s"

        alt "A wooden chair. It is tucked under a wooden table"

        action Jump("pandora_chair")

    imagebutton:
        xpos 792
        ypos 516

        focus_mask True

        auto "pandora_note %s"

        alt "Small piece of paper, on top of the wooden table"

        action Jump("pandora_note")
    
    imagebutton:
        xalign 1.0
        ypos 572

        focus_mask True

        auto "pandora_drawers %s"

        alt "Chest of drawers"

        action Jump("pandora_drawers")

    imagebutton:
        xpos 468
        ypos 600

        focus_mask True

        auto "pandora_bin %s"

        alt "A blue bin"

        action Jump("pandora_bin")

    imagebutton:
        xpos 1700
        ypos 452

        focus_mask True

        auto "pandora_cactus %s"

        alt "A green cactus in a brown pot"

        action Jump("pandora_cactus")

    imagebutton:
        xpos 1664
        ypos 112

        focus_mask True

        auto "pandora_clock %s"

        alt "A clock, it's stopped at 5 minutes to 6."

        action Jump("pandora_clock") 

    imagebutton:
        xpos 908
        ypos 324

        focus_mask True

        auto "pandora_speaker %s"

        alt "A metal speaker embedded in the wall above a table."

        action Jump("pandora_speaker")

    if daryaroom == True:
        imagebutton:
            xpos 1088
            ypos 320

            focus_mask True

            auto "daryadefault %s"

            alt "A woman dressed as a pirate. Her name is Darya"

            action Jump("pandora_darya")

    add "darkborder":
        blend "multiply"
        alpha 0.8


          

label draw_pandora_room:
    if roomtotal == 11 and flagA == 0:
        $ roomtotal = 0
        jump daryaburstpandoraroom

    if currentlocation != "pandora":
        scene bg pandora_full with fade
        $ currentlocation = "pandora"
    elif currentlocation == "pandora":
        scene bg pandora_full
    
    call screen pandora_room

        



label pandora_door:


    if flagA == 0:
        if daryaroom == True:
            menu:
                np "Should we head out?"

                "Yes, let's have a look around outside":
                    pk "So, before we run into the unknown, could you tell me what you saw before you barged in here?"

                    show darya yeah1 with dissolve2
                    #uk "darya needs to mention about the rough layout of what she saw. then they decide to check all the doors before leaving the dorms."
                    dk "{piracow}It seemed to be a dormitory of sorts.{/piracow}"
                    dk "{piracow}There were many doors similar to yer own.{/piracow}"

                    pk "Since it won't be dorms all the way down, I assume. Do you want to see what or who we can find in this area then move onto the rest of wherever we are?"
                    np "Again, assuming there {i}is{/i} a 'somewhere else', being methodical will prevent us from missing anything."

                    show darya yeah2 with fastDissolve
                    dk "Sounds good!"
                    show darya yeah1 with fastDissolve
                    dk "{piracow}However! Before we leave, I should draw ye a map of what I saw.{/piracow}"
                    hide darya with dissolve2

                    np "Darya took a pen out of her pocket and flipped the picture of 'Maizey' to the back and began scribbling on it."
                    np "..."

                    show daryamap with dissolve:
                        yalign 0.4
                        xalign 0.5
                        

                    dk "{piracow}This be what I saw!{/piracow}{alt}Description: A map of the dorms, it is shaped like a rectangular loop with doors lining both walls of the left and right sides of the rectangle. A door marked exit is in the top right. The top and bottom of the rectangle each have a door separating the left and right of the dorms into two halves, the left side is labelled 'B', and the right is labelled 'A'.{/alt}"

                    pk "The way you draw speech marks makes it look like the words are quivering in terror."

                    hide daryamap with dissolve

                    show darya grumpy with dissolve2
                    dk "Hey!"

                    pk "Anyway, thanks, this might be helpful."

                    show darya neutral with fastDissolve
                    dk "Let us be on our way, then."

                    stop music fadeout 1.0

                    jump draw_corrA1

                "No, let's stay here for a bit longer":
                    jump draw_pandora_room



            jump draw_pandora_room

        if pandoraroomread[0] == 1:
            pk "An unlocked metal door."

            jump draw_pandora_room
        elif pandoraroomread[0] == 0:
            pk "A secure metal door, it has a peephole in it but doesn't seem to be locked right now."
            pk "It appears to be a couple of inches thick, like a sort of barricade door."
            pk "Might be in my best interest to look for the key but I don't see one around."
            pk "I also don't want to leave without good reason since I don't know what's out there."
            pk "So for now I'll leave it be but keep an eye on it just in case."

            $ clues.update( {1 : "Bedroom Door"} )

            "Notes on 'Bedroom Door' jotted down."
            
            $ roomtotal += 1
            $ pandoraroomread[0] = 1
            jump draw_pandora_room

label pandora_wardrobe:

    if flagA == 0:
        if daryaroom == True:
            if pandoraroomread[1] == 2:
                np "There are copies of our custom outfits in our wardrobes, leading to some creepy implications."
                jump draw_pandora_room


            elif pandoraroomread[1] == 1:
                pk "Hey... Darya?"

                show darya ask1 with dissolve2
                dk "{piracow}Aye?{/piracow}"

                pk "Assuming you came from a room similar to mine..."
                pk "Did you also have a bunch of copies of your clothes in here?"
                pk "My outfit is handmade so there shouldn't be any more that exist."

                show darya hm with fastDissolve
                dk "{piracow}Ya, that be what I discovered too.{/piracow}"
                dk "{size=-10}But I didn't want to think about how it probably meant we'd been stalked.{/size}"
                hide darya with dissolve2

                np "That does seem to be the most likely explanation so far, let's be careful when we explore."

                $ clues_text[3].append("Darya suggested that we might have been stalked due to the anomoly of our wardrobe contents and I'm inclined to agree.")
                "Notes on 'Clothes in Wardrobe' have been updated."

                $ pandoraroomread[1] = 2
                jump draw_pandora_room

        if pandoraroomread[1] == 1:
            pk "A wardrobe with copies of my clothes that shouldnt exist."

            jump draw_pandora_room
        elif pandoraroomread[1] == 0:
            pk "The wardrobe seems to have a bunch of copies of my outfit."
            pk "Wait hold on, who made these? This one I'm wearing is the only one that should exist."
            pk "Who took the time to copy my custom outfit and why?"

            $ clues.update( {3 : "Clothes in Wardrobe"} )

            "Notes on 'Clothes in Wardrobe' have been jotted down."
            
            $ roomtotal += 1
            $ pandoraroomread[1] = 1
            jump draw_pandora_room

label pandora_bed:

    if flagA == 0:
        if daryaroom == True:
            if pandoraroomread[2] == 2:
                np "We both seem to have been given a mediocre bed in the rooms we woke up in."
                jump draw_pandora_room

            elif pandoraroomread[2] ==1:
                pk "Hey, any opinions on the quality of the furniture? Like this bed?"

                show darya neutral with dissolve2
                dk "{piracow}Ay, I tested mine out before I heard ye banging about.{/piracow}"
                show darya yikes with fastDissolve
                dk "{piracow}T'was not of the greatest quality.{/piracow}"
                hide darya with dissolve2

                np "That was a stupid question."

                $ pandoraroomread[2] = 2
                jump draw_pandora_room

        if pandoraroomread[2] == 1:
            pk "A bed of questionable quality."

            jump draw_pandora_room
        elif pandoraroomread[2] == 0:
            pk "A surprisingly comfy bed."
            pk "The cotton is low quality, but the mattress is soft, and the pillow is very flat."
            pk "I might need to get another one from somewhere if I'm going to have to sleep here."
            pk "Interestingly, I woke up on the floor. I guess my kidnappers care little for my comfort."

            $ clues_text[0].append("I also seem to have woken up on the floor despite there being a bed right next to me...")
            "Notes on 'Woke up in Strange Room' have been updated."

            if pandoraroomread[3] == 1 and pandoraroomread[4] == 1:
                $ clues.update( {2 : "Bedroom Furniture"} )
                "Notes on 'Bedroom Furniture' have been jotted down."
            
            $ roomtotal += 1
            $ pandoraroomread[2] = 1
            jump draw_pandora_room

label pandora_table:

    if flagA == 0:

        if pandoraroomread[3] == 1:
            pk "A cheap wooden table."

            jump draw_pandora_room
        elif pandoraroomread[3] == 0:
            pk "A very simple wooden table, probably not worth very much."
            pk "It's made of cheap wood and the construction is terrible."
            pk "It wouldn't be very practical to run off with, anyway."
            pk "There's also a note, of note, on it."

            if pandoraroomread[2] == 1 and pandoraroomread[4] == 1:
                $ clues.update( {2 : "Bedroom Furniture"} )
                "Notes on 'Bedroom Furniture' have been jotted down."
            
            $ roomtotal += 1
            $ pandoraroomread[3] = 1
            jump draw_pandora_room

label pandora_chair:

    if flagA == 0:

        if pandoraroomread[4] == 1:
            pk "This is my chair."

            jump draw_pandora_room
        elif pandoraroomread[4] == 0:
            pk "This chair is made of a hard wood and doesn't seem very comfortable."
            pk "But. It's better than not having a chair."
            pk "Y'know, I'm actually glad to have it."

            if pandoraroomread[2] == 1 and pandoraroomread[3] == 1:
                $ clues.update( {2 : "Bedroom Furniture"} )
                "Notes on 'Bedroom Furniture' have been jotted down."
            
            $ roomtotal += 1
            $ pandoraroomread[4] = 1
            jump draw_pandora_room

label pandora_note:

    if flagA == 0:
        if daryaroom == True:
            if pandoraroomread[5] == 2:
                show jbdoodle with fastDissolve:
                    xalign 0.5
                    yalign 0.5
                
                np "Whoever brought us here seems to really want us to know that this cereal mascot is involved."

                hide jbdoodle with fastDissolve

                jump draw_pandora_room


            elif pandoraroomread[5] == 1:
                show darya neutral with dissolve2

                show jbdoodle_iconbox with fastDissolve:
                    xalign 0.75
                    yalign 0.4

                dk "{piracow}I see you got a picture like that as well.{/piracow}"

                pk "Yeah, any idea what it means?"

                show darya hm with fastDissolve
                dk "{piracow}Sadly not a clue, matey.{/piracow}"

                hide jbdoodle_iconbox with fastDissolve
                
                hide darya with dissolve2
    

                $ pandoraroomread[5] = 2
                jump draw_pandora_room

        if pandoraroomread[5] == 1:
            show jbdoodle with fastDissolve:
                xalign 0.5
                yalign 0.5

            pk "A picture of a cereal mascot who may or may not have something to do with this."

            hide jbdoodle with fastDissolve

            jump draw_pandora_room

        elif pandoraroomread[5] == 0:
            show jbdoodle with fastDissolve:
                xalign 0.5
                yalign 0.5

            pk "There's a drawing of the Maple Yummys cereal's mascot, Maizey. {alt}Description: a poorly drawn doodle of a bipedal blue mouse, the tail, feet and hands are coloured orange and it is holding up 2 peace signs. The mouse is wearing a red hankerchief as a scarf and has a red star on its chest on the left side. The mouse appears to be wearing a brown skirt held up by suspenders as well as a small cowboy hat. There is the text 'Hi!' to the top left of the mouse.{/alt}"
            pk "Wait, have I been kidnapped by a cereal company?"
            pk "What would they even want with me?"
            pk "Unless... This is some type of new way to market products?"

            $ clues.update( {5 : "Doodle of Cereal Mascot"} )

            "Notes on 'Doodle of Cereal Mascot' have been jotted down."

            hide jbdoodle with fastDissolve
            
            $ roomtotal += 1
            $ pandoraroomread[5] = 1
            jump draw_pandora_room

label pandora_drawers:

    if flagA == 0:

        if pandoraroomread[6] == 1:
            pk "A simple chest of drawers."

            jump draw_pandora_room
        elif pandoraroomread[6] == 0:
            pk "A small chest of drawers, it got mostly socks and underwear in it."
            pk "How long am I expected to stay here for?"
            pk "This can't be a prison cell... right?"

            $ ch1murder_text[0].append("this should be 2nd")
            
            $ roomtotal += 1
            $ pandoraroomread[6] = 1
            jump draw_pandora_room

label pandora_bin:

    if flagA == 0:

        if pandoraroomread[7] == 1:
            pk "A disappointingly empty bin."

            jump draw_pandora_room
        elif pandoraroomread[7] == 0:
            pk "It's an empty-looking plastic bin."
            pk "I don't think it's going to help me much unless there's something like a door key in there."
            np "..."
            pk "There isn't."
            
            $ ch1murder_text[0].append("please add this text")
            
            $ roomtotal += 1
            $ pandoraroomread[7] = 1
            jump draw_pandora_room

label pandora_cactus:

    if flagA == 0:

        if pandoraroomread[8] == 1:
            pk "A little, prickly cactus."

            jump draw_pandora_room
        elif pandoraroomread[8] == 0:
            pk "A little cactus, it probably won't be doing very well without sunlight."
            pk "Actually, it's interesting that there's no windows here. Am I underground?"
            np "Anyway, I wonder what it feels like to-"
            pk "Ouch!"

            $ clues.update( {4 : "Small Cactus"} )

            "Notes on 'Small Cactus' have been jotted down."
            
            $ roomtotal += 1
            $ pandoraroomread[8] = 1
            jump draw_pandora_room

label pandora_clock:

    if flagA == 0:
        if daryaroom == True:
            if pandoraroomread[9] == 2:
                np "Two clocks stopped on the exact same time isn't too weird, but it's certainly interesting."
                jump draw_pandora_room


            elif pandoraroomread[9] == 1:
                pk "The clock is stopped."

                show darya neutral with dissolve2
                dk "{piracow}Mine was stopped as well.{/piracow}"
                show darya bois with fastDissolve
                dk "{piracow}Curiously, it were on the exact same time.{/piracow}" #HEHE STARBUBBLES <3
                hide darya with dissolve2

                $ pandoraroomread[9] = 2
                jump draw_pandora_room

        if pandoraroomread[9] == 1:
            pk "A useless, stopped clock."

            jump draw_pandora_room
        elif pandoraroomread[9] == 0:
            pk "There's a clock on the wall that seems to be stopped."
            pk "Even if it wasn't I wouldn't know if it's AM or PM."
            np "Another point for the 24hr clock system."
            
            $ roomtotal += 1
            $ pandoraroomread[9] = 1
            jump draw_pandora_room

label pandora_darya:

    if flagA == 0:
        show darya neutral with dissolve2
        dk "{piracow}Arg, let's be going then. Nothing to be gained from staying idle.{/piracow}"
        hide darya with dissolve2

        np "Except maybe staying safe from anything that might be out there?"
        np "Then again, she managed to break in here easily enough - anyone who means me harm would be able to as well."
        np "And the real safest option is to know where we are."

        jump draw_pandora_room

label pandora_speaker:


    if flagA == 0:
        if daryaroom == True:
            if pandoraroomread[10] == 2:
                np "A mysterious speaker that neither of us know the purpose of."
                jump draw_pandora_room
           
            elif pandoraroomread[10] == 1:
                pk "Any idea what this is meant for?"
                np "I point to the speaker on the wall."

                show darya hm with dissolve2
                dk "I don't, had one in my r-"
                show darya threat with fastDissolve
                dk "{size=-10}Wait, I mean: {/size}{piracow}It's purpose be a mystery!{/piracow}"

                np "For the love of god please turn the voice off."

                hide darya with dissolve2

                $ pandoraroomread[10] = 2
                jump draw_pandora_room

        if pandoraroomread[10] == 1:
            pk "There's a strange speaker on the wall."

            jump draw_pandora_room
        elif pandoraroomread[10] == 0:
            pk "There's what looks like a strange sort of speaker on the wall."
            pk "It's embedded into the metal plate quite firmly and has a grate over the diaphragm."
            pk "I can only assume it's to prevent people like me from poking at it."

            $ clues.update( {6 : "Wall Speaker"} )

            "Notes on 'Wall Speaker' have been jotted down."
            
            $ roomtotal += 1
            $ pandoraroomread[10] = 1
            jump draw_pandora_room
        


#====================#
### Dorms Corridor ###
#====================#

screen doors: #this is the 'texbox' for when pandora senses someone behind a door as a QoL thing
    add "hoverdoor.png":
        xalign 0.5
        yalign 0.95

#CORRIDOR A1

screen corrA1:
    add "bg corra1.png"

    imagebutton:
        xanchor 0.0 
        yanchor 0.0
        xpos 874
        ypos 430

        focus_mask True

        auto "rightarrow %s"

        alt "An arrow pointing right."

        if corrA1read[6] == 0:
            action Jump("nogood1")
            alt "You cannot walk this way"
        else:
            action Jump("draw_corrA3")
            alt "Press to turn to Dormitory B's door"
        
        if wiggle:
            at buttup2

    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 1500
        ypos 906

        focus_mask True

        auto "turnarrow %s"

        alt ""

        if corrA1read[6] == 0:
            action Jump("nogood1")
        else:
            action Jump("draw_corrC2")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 1300
        ypos 276

        focus_mask True

        auto "pandoor1 %s"

        action Jump("pandoor")

        alt "A door with a bird shape on it"

    imagebutton:
        xpos 304
        ypos 284

        focus_mask True

        auto "flodoor1 %s"



        if corrA1read[6] == 0:
            action [
                Hide("doors"),
                Jump("nogood1")
            ]
        else:
            if flagA == 1:
                hovered Show("doors")
                unhovered Hide("doors")
            action [
                Hide("doors"),
                Jump("flodoor")
            ]
        
        alt "A door with a butterfly shape on it"

    imagebutton:
        xpos 1088
        ypos 332

        focus_mask True

        auto "dardoor1 %s"

        action Jump("dardoor")

        alt "A door with a bat-like shape on it"

    imagebutton:
        xpos 624
        ypos 348

        focus_mask True

        auto "nikdoor1 %s"

        if corrA1read[6] == 0:
            action Jump("nogood1")
        else:
            action Jump("nikdoor")

        alt "A door with a spider shape on it"

    imagebutton:
        xpos 764
        ypos 376

        focus_mask True

        auto "toiletdoor1 %s"

        action Jump("toidoor")

        alt "The toilet door"

    imagebutton:
        xpos 816
        ypos 404

        focus_mask True

        auto "toiletsign1 %s"

        action Jump("toisign")

        alt "A sign for the toilets"

    imagebutton:
        xpos 1000
        ypos 372

        focus_mask True

        auto "dormsign %s"

        action Jump("dormsign")

        alt "dorm rules sign"

    add "darkborder":
        blend "multiply"
        alpha 0.8

label nogood1:
    scene bg corra1_full 
    np "There's a sign labelled 'dorm rules' at the end of the corridor. I think I should read it before I check anywhere else."
    jump draw_corrA1

label draw_corrA1: 
    if currentlocation != "corrA1":
        scene bg corra1_full with fade
        $ currentlocation = "corrA1"
    elif currentlocation == "corrA1":
        scene bg corra1_full


    if flagA == 0:
        play music "audio/wandering.mp3" fadein 1.0


        ht "To navigate the area click on doors to enter them, or the arrows to move around the corridors."
        ht "When navigating corridors, remember that {i}generally{/i} {image=cornera.png} arrows will turn 90 degrees, and {image=rounda.png} arrows will turn 180 degrees."
        #ht "Characters that are tagging along with Pandora will (theoretically, feature not in the alpha) be displayed at the bottom right."
        #ht "Click their icons to hear what they have to say."
        ht "Click the 'map' icon in the bottom left to get a view of where you are, though currently the feature is unavailable outside of the dorms."

        $ flagA = 1
        $ mactive = True

    call screen corrA1

label pandoor:
    if flagA == 1:
        np "That's the door we just exited, going back in would take us back to, what I believe is, my room."
        np "There's a silhouette of a bird, I can only presume a magpie, just under the peephole."

        if corrA1read[0] == 0:
            $ corrA1read[0] = 1
            $ roomtotal += 1

        if currentlocation == "corrA1":
            jump draw_corrA1
        else:
            jump draw_corrA2

label dardoor:
        if flagA == 1:
            np "There's a door with what looks like a sort of bat drawn on it."

            if corrA1read[2] == 0:
                show darya neutral with dissolve2
                dk "{piracow}That one be my door!{/piracow}"
                show darya bois with fastDissolve
                dk "Well, the door to the room I woke up in."

                np "Her being my direct neighbour explains why she was able to hear me, I guess."

                hide darya with dissolve2

                $ corrA1read[2] = 1
                $ roomtotal += 1

        if currentlocation == "corrA1":
            jump draw_corrA1
        else:
            jump draw_corrA2

label nikdoor:
        if flagA == 1:
            if corrA1read[3] == 1:
                np "There's a door with a spider drawn on it."

            elif corrA1read[3] == 0:
                np "There's a door with a spider drawn on it, I knock to see if anyone's inside."
                play sound "audio/knock.wav"
                np "..."
                np "No response."

                $ corrA1read[3] = 1
                $ roomtotal += 1

        if currentlocation == "corrA1":
            jump draw_corrA1
        else:
            jump draw_corrA2

label flodoor:
        if flagA == 1:
            if corrA1read[1] == 1:
                np "A strange man named Florus is in the room marked by the butterfly door."
                np "I shouldn't disturb him again, it'd be rude."

            elif corrA1read[1] == 0:
                np "There's a door with a butterfly drawn on it, I knock to see if anyone's inside."
                play sound "audio/knock.wav"
                np "..."
                np "The door slowly opened, and a man emerged."

                show florus neutral with dissolve2
                "{uk}Man With Flowers{/uk}" "... hello?"
                hide florus with fastDissolve

                show florus neutral at twoleft

                show darya yeah2 at tworight

                with fastDissolve

                dk "{piracow}AHOY!{/piracow}"

                show florus flinch with fastDissolve
                "{uk}Man With Flowers{/uk}" "!?"
                show florus neutral with fastDissolve

                show darya neutral with fastDissolve
                dk "{piracow}What be your name?{/piracow}"

                show florus confused with fastDissolve
                fc "Um... My name be Florus...?"

                show darya ask1 with fastDissolve
                np "Darya paused and looked at Florus expectantly, as though waiting for him to ask her name in kind."

                show florus blerg with fastDissolve
                fc "Anyway, do... either of you know what's going on?"

                pk "Not really, but I think that-"

                show darya bois with fastDissolve
                dk "{piracow}It seems we be in a sort of bunker!{/piracow}{size=-10} Probably...{/size}"

                show florus tired with fastDissolve
                fc "Hmm... sounds like a lot of bother."
                fc "I think I'll just stay in here where I woke up, and out of the way."
                fc "Goodbye."
                hide florus with dissolve2

                np "He went to close the door but Darya quickly put her arm out and yelled."

                show darya threat with fastDissolve
                dk "Wait!"
                show darya hm with fastDissolve
                dk "{piracow}Don't ye wish to ask who we be?{/piracow}"

                show florus uhm at twoleft with dissolve2
                fc "I suppose..."

                show darya ohyeah with fastDissolve
                dk "I be Darya Skafos, captain of The Dragonflight!"

                show florus neutral with fastDissolve
                np "Florus looked cautiously over to me."

                show darya neutral with fastDissolve

                pk "I'm... Phantom Magpie."
                np "I probably shouldn't directly mention that that's a made up name. In... both of our cases."
                pk "As you can tell, she's, uh, she's a pirate. And I'm, well I can't really, {size=-15}legally{/size}, say, but my work helps the poor."
                np "I really shouldn't have blurted out directly what I actually do to Darya before, but I can't take it back."
                pk "What do you do?"

                show florus excited with fastDissolve
                fc "Oh! Well, I'm a gardener! People hire me to care for and design gardens for them."
                show florus glee with fastDissolve
                fc "I especially like designing flowerbeds and choosing what kinds of flowers are best for..."
                show florus uhm with dissolve2
                fc "..."
                show florus tired with dissolve2
                fc "Well, it's uh, it was nice meeting you both."
                fc "I'm just gonna..."

                np "He looks at us with a tired gaze, then slips back into his room and closes the door."

                hide florus with dissolve2

                hide darya with fastDissolve
                show darya yeah1 at centre with fastDissolve
                dk "{piracow}Knowing it's not just us here be somewhat reassuring.{/piracow}"
                show darya hm with fastDissolve
                dk "He was a little strange though..."

                if corrB1read[3] == 0:
                    np "Okay pot, leave the kettle alone; I've known you for all of 10 minutes, and for each of those minutes you have been waving around a sword made of cardboard and craft foam."
                elif corrB1read[3] == 1:
                    np "Okay pot, leave the kettle alone; I've known you for nearly half an hour, and for that entire time you have been waving around a sword made of cardboard and craft foam."

                hide darya with dissolve2

                $ corrA1read[1] = 1
                $ roomtotal += 1

        if currentlocation == "corrA1":
            jump draw_corrA1
        else:
            jump draw_corrA2

label toisign:
        if flagA == 1:
            np "There's a sign with a toilet drawn on, presumably indicating the purpose of the room next to it."

        if currentlocation == "corrA1":
            jump draw_corrA1
        else:
            jump draw_corrA2

label toidoor:
        if flagA == 1:
            np "Inside is a row of 8 toilet cubicles, and 4 sinks."

        if currentlocation == "corrA1":
            jump draw_corrA1
        else:
            jump draw_corrA2

label dormsign:
    if flagA ==1:
        if corrA1read[6] == 1:
            np "The 'dorm rules' are as follows:"
            np "1: Keep the noise down between 23:00 and 07:00 (designated 'nighttime'), your bunkmates may be trying to sleep!"
            np "2: Your doors must be kept locked as Management does not take responsibility for stolen or damaged property."
            np "3: You are responsible for keeping the dorms tidy, however the Assistants will clean everywhere else."
            np "4: As there is a limited number of toilets/showers per dorm group, be respectful about not staying in for too long."

            if currentlocation == "corrA1":
                jump draw_corrA1
            else:
                jump draw_corrA2

        elif corrA1read[6] == 0:
            pk "Hey, there's a sign taped to the wall here with some 'dorm rules' on."

            show darya ask1 with dissolve2
            dk "{piracow}I saw it on me way over to yer abode, but didn't care to read.{/piracow}"
            dk "{piracow}Do ye wish to read it out, or should I be the one?{/piracow}"

            np "Please care a little more about your surroundings..."
            pk "I'll read it out, I guess:"

            show darya neutral with fastDissolve

            pk "'1: Keep the noise down between 23:00 and 07:00 (designated 'nighttime'), your bunkmates may be trying to sleep!'"
            np "'Bunkmates', huh. This being some sort of bunker does make some sense, I think. But what reason would there be to put us in one?"
            pk "'2: Your doors must be kept locked as Management does not take responsibility for stolen or damaged property.'"

            show darya hm with fastDissolve
            dk "Keeping our doors locked- {piracow}be a difficult task without the keys.{/piracow}"

            np "So she didn't get a room key either."
            pk "Maybe this 'management' is going to give them to us?"
            np "But then why would we wake up in our rooms without them?"

            show darya neutral with fastDissolve

            pk "Anyway, '3: You are responsible for keeping the dorms tidy, however the Assistants will clean the rest of the bunker.'"
            np "Assuming this information is up to date, the presence of 'assistants' sounds somewhat promising in nothing properly dangerous going on."

            pk "And finally, '4: As there is a limited number of toilets/showers per dorm group, be respectful about not staying in for too long.'"

            show darya yeah1 with fastDissolve
            dk "{piracow}Aha! The toilets in question must be at the end of the corridor there.{/piracow}"

            np "Why is that the thing you focus on?"

            show darya hh with fastDissolve
            dk "{size=-15}It seems we're in some sort of bunker, but for what purpose is...{/size}"

            pk "What are you mumbling about?"

            show darya threat with fastDissolve
            dk "{piracow}It be nothing to concern yerself with!{/piracow}"
            hide darya with dissolve2

            np "I hope for both of our sakes that you're smarter than you let on."

            $ corrA1read[6] = 1
            if currentlocation == "corrA1":
                jump draw_corrA1
            else:
                jump draw_corrA2

#Corridor A2

screen corrA2:
    add "bg corra2.png"

    imagebutton:
        xpos 950
        ypos 580

        focus_mask True

        auto "forward arrow %s"

        action Jump("draw_corrC2")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 180
        ypos 880

        focus_mask True

        auto "left arrow2 %s"

        action Jump("draw_corrA3")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 632
        ypos 372

        focus_mask True

        auto "pandoor2 %s"

        action Jump("pandoor")

    imagebutton:
        xpos 212
        ypos 404

        focus_mask True

        auto "dormsign2 %s"

        action Jump("dormsign")

    imagebutton:
        xpos 456
        ypos 340

        focus_mask True

        auto "dardoor2 %s"

        action Jump("dardoor")

    imagebutton:
        xpos 1272
        ypos 372

        focus_mask True

        auto "flordoor2 %s"

        if flagA == 1:
            hovered Show("doors")
            unhovered Hide("doors")

        action [
            Hide("doors"),
            Jump("flodoor")
        ]

    imagebutton:
        xpos 1408
        ypos 344

        focus_mask True

        auto "nikdoor2 %s"

        action Jump("nikdoor")

    imagebutton:
        xpos 1640
        ypos 288

        focus_mask True

        auto "toidoor2 %s"

        action Jump("toidoor")

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_corrA2:
    if currentlocation != "corrA2":
        scene bg corra2_full with fade
        $ currentlocation = "corrA2"
    elif currentlocation == "corrA2":
        scene bg corra2_full

    call screen corrA2

#Corridor A3

screen corrA3:
    add "bg corra3"
    imagebutton:
        xpos 1432
        ypos 908

        focus_mask True

        auto "right arrow2 %s"

        action Jump("draw_corrA2")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 648
        ypos 56

        focus_mask True

        auto "dormdoor1 %s"

        action Jump("draw_corrB2")

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_corrA3:
    if currentlocation != "corrA3":
        scene bg corra3_full with fade
        $ currentlocation = "corrA3"
    elif currentlocation == "corrA3":
        scene bg corra3_full

    call screen corrA3

#Corridor B1

screen corrB1:
    imagebutton:
        xpos 980
        ypos 380

        focus_mask True

        auto "clodoor %s"

        action Jump("clodoor")

    imagebutton:
        xanchor 0.0 
        yanchor 0.0
        xpos 950
        ypos 430

        focus_mask True

        auto "left arrow %s"

        if wiggle:
            at buttup2

        action Jump("draw_corrB3")

    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 1576
        ypos 906

        focus_mask True

        auto "turnarrow %s"

        if wiggle:
            at buttup2

        action Jump("draw_corrD2")

    imagebutton:
        xpos 412
        ypos 276

        focus_mask True

        auto "cardoor %s"

        action Jump("cardoor")

    imagebutton:
        xpos 736
        ypos 332

        focus_mask True

        auto "emidoor %s"

        action Jump("emidoor")

    imagebutton:
        xpos 1108
        ypos 376

        focus_mask True

        auto "shodoor %s"

        action Jump("shodoor")

    imagebutton:
        xpos 1072
        ypos 404

        focus_mask True

        auto "shosign %s"

        action Jump("shosign")

    imagebutton:
        xpos 1196
        ypos 348

        focus_mask True

        auto "dakdoor %s"

        if flagA == 1:
            hovered Show("doors")
            unhovered Hide("doors")

        action [
            Hide("doors"),
            Jump("dakdoor")
        ]

    imagebutton:
        xpos 1416
        ypos 284

        focus_mask True

        auto "fabdoor %s"

        if flagA == 1:
            hovered Show("doors")
            unhovered Hide("doors")

        action [
            Hide("doors"),
            Jump("fabdoor")
        ]



label draw_corrB1:
    if currentlocation != "corrB1":
        scene bg corrb1_full with fade
        $ currentlocation = "corrB1"
    elif currentlocation == "corrB1":
        scene bg corrb1_full

    call screen corrB1

label fabdoor:
    if flagA == 1:
        np "There's a door with a swan drawn on it."

        if corrB1read[4] == 0:
            play sound "audio/knock.wav"
            np "..."
            np "Interestingly, there's no response."

            $ corrB1read[4] = 1
            $ roomtotal += 1

    if currentlocation == "corrB1":
        jump draw_corrB1
    else:
        jump draw_corrB2

label cardoor:
    if flagA == 1:
        np "There's a door with some kind of goat drawn on it."

        if corrB1read[2] == 0:
            play sound "audio/knock.wav"
            np "..."
            np "No response."

            $ corrB1read[2] = 1
            $ roomtotal += 1

    if currentlocation == "corrB1":
        jump draw_corrB1
    else:
        jump draw_corrB2

label emidoor:
    if flagA == 1:
        np "There's a door with a cat drawn on it."

        if corrB1read[1] == 0:
            play sound "audio/knock.wav"
            np "..."
            np "No response."

            $ corrB1read[1] = 1
            $ roomtotal += 1

    if currentlocation == "corrB1":
        jump draw_corrB1
    else:
        jump draw_corrB2

label dakdoor:
    if flagA == 1:
        if corrB1read[3] == 1:
            np "I probably shouldn't aggrivate Emilio by knocking on his door again when Darya's here."

        elif corrB1read[3] == 0:
            np "There's a door with a horse drawn on it, I lift up my hand to knock on the door but Darya quickly pipes up."

            show darya hh with dissolve2
            dk "{piracow}Arg matey{/piracow}, {size=-10}just gonna visit the loos{/size}, {piracow}I'll be but a moment.{/piracow}"

            pk "Oh, uh, sure. If anyone's in here I'll just greet them by myself or something."

            hide darya with dissolve2

            np "After giving a quick  thumbs-up, Darya heads back through the door to the other side of the dorms."        
            play sound "audio/knock.wav"
            np "..."

            show emilio happy with dissolve2
            "{uk}Cowboy{/uk}" "{piracow}Howdy partner!{/piracow}"

            pk "Hello."
            np "My eyes are drawn the NURF revolver and cowboy getup as annoyance forms in my gut."
            np "Please tell me he isn't like a second Darya..."

            show emilio welcome with fastDissolve
            "{uk}Cowboy{/uk}" "{piracow}C'mon in, can't leave ya out in the corridor like that.{/piracow}"

            np "On the one hand, since I have little idea of what's going on this could easily be a trap. Not to mention that I {i}really{/i} don't want to deal with another freaky LARPer right now..."
            np "But on the other hand, I don't want to upset him in case he's dangerous - so going along with this but keeping a cautious ear up is probably best."
            pk "Sure..."

            hide emilio with dissolve2

            stop music fadeout 1.0

            scene black with dissolve

            np "I followed the strange man into the door with the horse symbol on."
            np "And inside I was greeted by a room I never could have expected."

            scene bg horseroom with dissolve

            play music "audio/something.mp3" fadein 1.0

            #pause 1.5

            show dakota neutral with dissolve2
            dh "Neigh."
            hide dakota with dissolve2

            show emilio neutral with dissolve2
            "{uk}Cowboy{/uk}" "{piracow}Make yerself at home. {/piracow}"

            pk "There- there is a horse."

            "{uk}Cowboy{/uk}" "{piracow}That'll be Dakota, my loyal steed and truest friend.{/piracow}"
            hide emilio with dissolve2
            show dakota neutral with dissolve2
            dh "Neigh."
            hide dakota with dissolve2
            show emilio neutral with dissolve2

            pk "Oh. Okay."
            pk "Also, quick question: where are you from?"

            show emilio confuzz with fastDissolve
            "{uk}Cowboy{/uk}" "Uh, Yorkshire?"

            np "So the Texas accent is fake."
            pk "Would it be possible... for you to use your normal voice?"
            np "I try not to sound too exasperated."

            show emilio neutral with fastDissolve
            "{uk}Cowboy{/uk}" "{piracow}Of course-{/piracow} of course."

            np "Thankfully he complies without pushback, and replaces his cowboy accent with a much more natural-sounding Yorkshire one."

            show emilio happy with fastDissolve
            eb "Oh! All this and I forgot to give my name, I'm Emilio."

            pk "Nice to meet you, call me Pa-. Call me Phantom Magpie."
            np "He's got such a relaxing aura that I nearly let my guard down there."
            pk "Anyway, just to circle back quickly, {i}why{/i} is the horse here? You just kinda brushed over that."

            show emilio spin with fastDissolve
            eb "In normal circumstances I never go anywhere without him, since he's so well behaved and friendly."
            show emilio sad with fastDissolve
            eb "But in this case I don't even know why {i}I'm{/i} here, let alone poor Dakota..."

            pk "And you even have a horse because...?"

            show emilio neutral with fastDissolve
            eb "My parents got him to replace our previous workhorse, since we own a livestock farm."

            pk "For like, pulling carts?"
            np "Before Emilio had a chance to respond, Darya came bursting back into the room."

            hide emilio with fastDissolve

            show emilio neutral at tworight 
            
            show darya yeah2 at twoleft 

            with fastDissolve

            dk "{piracow}Ahoy Magpie! I have ret-{/piracow}"
            show darya grumpy

            show emilio grumpy

            with fastDissolve

            np "She casts a quick frown at Dakota, then glares angrily at Emilio after eyeing his outfit, who does the same in kind."

            dk "..."

            eb "..."

            pk "Do you two... know each other?"

            dk "The inherent rivaly we have as pirate and cowboy far surpasses something as simple as 'knowing each other'."

            np "Is that a thing...?"

            show emilio bad with fastDissolve
            eb "{piracow}There ain't room in this town for the two of us, {i}partner{/i}.{/piracow}"

            show darya threat with fastDissolve
            dk "{piracow}Says the scallywag attempting to beguile me crew.{/piracow}"
            show darya grumpy with fastDissolve

            show emilio grumpy with fastDissolve

            np "As the two argue and lose their focus on me I attempt to slip out of the room. Silently, as I've done so many times before."
            np "However, before I could reach the door, Darya seemed to notice me."

            show darya anger with fastDissolve
            dk "{piracow}Yer right, Magpie. We should leave the bilge rat to his filth.{/piracow}"

            eb "{piracow}Scram, we don't want your kind 'round here.{/piracow}"
            hide emilio 

            hide darya 

            with dissolve2

            stop music fadeout 1.0

            scene bg corrb2_full with fade

            np "I sigh as she all but drags me out. Despite the kidnapping, being in proximity of these two is somehow the worst thing to happen to me today."

            show darya grumpy with dissolve2
            dk "Let's go find some more favourable folks."

            np "I agree, but I doubt we're thinking about it in the same way."

            hide darya with dissolve2

            play music "audio/wandering.mp3" fadein 1.0

            $ corrB1read[3] = 1
            $ roomtotal += 1
            $ currentlocation = "corrB2"
            

    if currentlocation == "corrB1":
        jump draw_corrB1
    else:
        jump draw_corrB2

label shodoor:
    if flagA == 1:
        np "Inside there are 6 shower cubicles, and a row of 6 lockers. These are presumably for clothes."

    if currentlocation == "corrB1":
        jump draw_corrB1
    else:
        jump draw_corrB2

label shosign:
    if flagA == 1:
        np "There's a sign with a shower drawn on, presumably indicating the purpose of the room next to it."

    if currentlocation == "corrB1":
        jump draw_corrB1
    else:
        jump draw_corrB2

label clodoor:
    if flagA == 1:
        np "There's a small closet at the end of the corridor."
        np "It's got cleaning supplies like a mop, a vacuum, and a broom in it."
        np "Makes sense, seeing as we're apparently to clean our own dorms."

    if currentlocation == "corrB1":
        jump draw_corrB1
    else:
        jump draw_corrB2

#Corridor B2

screen corrB2:
    add "bg corrb2"

    imagebutton:
        xpos 905
        ypos 580

        focus_mask True

        auto "forward arrow %s"

        action Jump("draw_corrD2")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 1660
        ypos 840

        focus_mask True

        auto "right arrow2 %s"

        action Jump("draw_corrB3")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 68
        ypos 288

        focus_mask True

        auto "shodoor2 %s"

        action Jump("shodoor")

    imagebutton:
        xpos 400
        ypos 344

        focus_mask True

        auto "dakdoor2 %s"

        if flagA == 1:
            hovered Show("doors")
            unhovered Hide("doors")

        action [
            Hide("doors"),
            Jump("dakdoor")
        ]

    imagebutton:
        xpos 576
        ypos 372

        focus_mask True

        auto "fabdoor2 %s"

        if flagA == 1:
            hovered Show("doors")
            unhovered Hide("doors")

        action [
            Hide("doors"),
            Jump("fabdoor")
        ]

    imagebutton:
        xpos 1216
        ypos 372

        focus_mask True

        auto "cardoor2 %s"

        action Jump("cardoor")

    imagebutton:
        xpos 1352
        ypos 340

        focus_mask True

        auto "emidoor2 %s"

        action Jump("emidoor")

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_corrB2:
    if currentlocation != "corrB2":
        scene bg corrb2_full with fade
        $ currentlocation = "corrB2"
    elif currentlocation == "corrB2":
        scene bg corrb2_full

    call screen corrB2

#Corridor B3

screen corrB3:
    add "bg corrb3"

    imagebutton:
        xpos 260
        ypos 892

        focus_mask True

        auto "left arrow2 %s"

        action Jump("draw_corrB2")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 648
        ypos 56

        focus_mask True

        auto "dormdoor2 %s"

        action Jump("draw_corrA2")

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_corrB3:
    if currentlocation != "corrB3":
        scene bg corrb3_full with fade
        $ currentlocation = "corrB3"
    elif currentlocation == "corrB3":
        scene bg corrb3_full

    call screen corrB3


#Corridor C1

screen corrC1:
    add "bg corrc1"

    imagebutton:
        xpos 396
        ypos 332

        focus_mask True

        auto "xdoor1 %s"

        action Jump("Xdoor1")

    imagebutton:
        xpos 1456
        ypos 332

        focus_mask True

        auto "ratdoor %s"

        action Jump("ratdoor")
    
    imagebutton:
        xpos 160
        ypos 840

        focus_mask True

        auto "left arrow2 %s"

        action Jump("draw_corrC3")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 1695
        ypos 840

        focus_mask True

        auto "right arrow2 %s"

        action Jump("draw_corrC4")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 950
        ypos 556

        focus_mask True

        auto "forward arrow %s"

        action Jump("draw_corrA1")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 596
        ypos 364

        focus_mask True

        auto "nindoor %s"

        action Jump("nindoor")

    imagebutton:
        xpos 720
        ypos 384

        focus_mask True

        auto "dexdoor %s"

        if flagA == 1:
            hovered Show("doors")
            unhovered Hide("doors")

        action [
            Hide("doors"),
            Jump("dexdoor")
        ]

    imagebutton:
        xpos 1192
        ypos 384

        focus_mask True

        auto "beldoor %s"

        action Jump("beldoor")

    imagebutton:
        xpos 1300
        ypos 364

        focus_mask True

        auto "xdoor2 %s"

        action Jump("Xdoor2")

    add "darkborder":
        blend "multiply"
        alpha 0.8


label draw_corrC1:
    if currentlocation != "corrC1":
        scene bg corrc1_full with fade
        $ currentlocation = "corrC1"
    elif currentlocation == "corrC1":
        scene bg corrc1_full

    call screen corrC1

label Xdoor1:
    if flagA == 1:
        np "There's a door with a red X painted on it. I get the feeling that there's nothing inside."

    if currentlocation == "corrC1":
        jump draw_corrC1
    else:
        jump draw_corrC2

label nindoor:
    if flagA == 1:
        np "There's a door with a bird, that looks kind of like a kingfisher, drawn on it."

        if corrC1read[1] == 0:
            play sound "audio/knock.wav"
            np "..."
            np "No response."

            $ corrC1read[1] = 1
            $ roomtotal += 1

    if currentlocation == "corrC1":
        jump draw_corrC1
    else:
        jump draw_corrC2

label dexdoor:
    if flagA == 1:
        np "There's a door with a lizard of some sort drawn on it."

        if corrC1read[2] == 0:
            play sound "audio/knock.wav"
            np "..."
            np "Interestingly, there's no response."

            $ corrC1read[2] = 1
            $ roomtotal += 1

    if currentlocation == "corrC1":
        jump draw_corrC1
    else:
        jump draw_corrC2

label beldoor:
    if flagA == 1:    
        np "There's a door with a crocodile drawn on it."

        if corrC1read[3] == 0:
            play sound "audio/knock.wav"
            np "..."
            np "No response."

            $ corrC1read[3] = 1
            $ roomtotal += 1

    if currentlocation == "corrC1":
        jump draw_corrC1
    else:
        jump draw_corrC2

label Xdoor2:
    if flagA == 1:
        np "There's a door with a red X painted on it. I get the feeling that there's nothing inside."

    if currentlocation == "corrC1":
        jump draw_corrC1
    else:
        jump draw_corrC2

label ratdoor:
    if flagA == 1:
        np "There's a door with some sort of rodent drawn on it."
        
        if corrC1read[5] == 0:
            play sound "audio/knock.wav"
            np "..."
            np "No response."

            $ corrC1read[5] = 1
            $ roomtotal += 1

    if currentlocation == "corrC1":
        jump draw_corrC1
    else:
        jump draw_corrC2


#Corridor C2

screen corrC2:
    add "bg corrc2.png"

    imagebutton:
        xpos 1500
        ypos 904

        focus_mask True

        auto "turnarrow %s"

        action Jump("draw_corrA1")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 788
        ypos 444

        focus_mask True

        auto "left arrow %s"

        action Jump("draw_corrC4")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 884
        ypos 444

        focus_mask True

        auto "rightarrow %s"

        action Jump("draw_corrC3")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 116
        ypos 268

        focus_mask True

        auto "beldoor2 %s"

        action Jump("beldoor")

    imagebutton:
        xpos 516
        ypos 336

        focus_mask True

        auto "xdoor22 %s"

        action Jump("Xdoor2")

    imagebutton:
        xpos 688
        ypos 364

        focus_mask True

        auto "ratdoor2 %s"

        action Jump("ratdoor")

    imagebutton:
        xpos 1028
        ypos 348

        focus_mask True

        auto "xdoor12 %s"

        action Jump("Xdoor1")

    imagebutton:
        xpos 1172
        ypos 312

        focus_mask True

        auto "nindoor2 %s"

        action Jump("nindoor")

    imagebutton:
        xpos 1496
        ypos 228

        focus_mask True

        auto "dexdoor2 %s"

        if flagA == 1:
            hovered Show("doors")
            unhovered Hide("doors")

        action [
            Hide("doors"),
            Jump("dexdoor")
        ]

    add "darkborder":
        blend "multiply"
        alpha 0.8



label draw_corrC2:
    if currentlocation != "corrC2":
        scene bg corrc2_full with fade
        $ currentlocation = "corrC2"
    elif currentlocation == "corrC2":
        scene bg corrc2_full

    call screen corrC2

#Corridor C3

screen corrC3:
    add "bg corrc4"

    imagebutton:
        xpos 1434
        ypos 902

        focus_mask True

        auto "right arrow2 %s"

        action Jump("draw_corrC1")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 272
        ypos 906

        focus_mask True

        auto "turnarrow2 %s"

        action Jump("draw_corrC4")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 648
        ypos 56

        focus_mask True

        auto "dormdoor4 %s"

        action Jump("dormexitdoor")

    add "darkborder":
        blend "multiply"
        alpha 0.8



label draw_corrC3:
    if currentlocation != "corrC3":
        scene bg corrc4_full with fade
        $ currentlocation = "corrC3"
    elif currentlocation == "corrC3":
        scene bg corrc4_full

    call screen corrC3

label dormexitdoor:
    if flagA == 1:
        if corrB1read[3] != 1 or corrA1read[1] != 1:
            np "We shouldn't leave the dorms until we've finished checking it out. Pretty certain I can ignore the doors with the {color=DD0000}X{/color}s on, though."
            np "The doors with the butterfly, horse, ferret-thing, lizard, and swan drawn on feel most likely to be of note."

        elif corrB1read[3] == 1 and corrA1read[1] == 1:
            np "I take a breath in and carefully open the exit door."
            np "Normally, I'd be trying my best to be small and quiet, but with Darya around I don't think there's much point in being sneaky."
            np "Then again, that's exactly the reason it's useful to let her tag along - if anything happens, then {i}I{/i} won't be the one getting hurt."
            np "We head out into the hallway."

            jump draw_corrE1

    if currentlocation == "corrC3":
        jump draw_corrC3
    else:
        jump draw_corrC3

label dexitsign:
    if flagA == 1:
        np "There's a sign that denotes this door as the exit to the dorms."

    if currentlocation == "corrC3":
        jump draw_corrC3
    else:
        jump draw_corrC3

#Corridor C4

screen corrC4:
    add "bg corra3"

    imagebutton:
        xpos 1434
        ypos 902

        focus_mask True

        auto "turnarrow %s"

        action Jump("draw_corrC3")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 272
        ypos 906

        focus_mask True

        auto "left arrow2 %s"

        action Jump("draw_corrC1")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 648
        ypos 56

        focus_mask True

        auto "dormdoor1 %s"

        action Jump("draw_corrD1")

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_corrC4:
    if currentlocation != "corrC4":
        scene bg corra3_full with fade
        $ currentlocation = "corrC4"
    elif currentlocation == "corrC4":
        scene bg corra3_full

    call screen corrC4

#Corridor D1

screen corrD1:
    add "bg corrd1"

    imagebutton:
        xpos 340
        ypos 332

        focus_mask True

        auto "kevdoor %s"

        action Jump("kevdoor")   

    imagebutton:
        xpos 1400
        ypos 332

        focus_mask True

        auto "xdoor4 %s"

        action Jump("Xdoor4") 

    imagebutton:
        xpos 172
        ypos 840

        focus_mask True

        auto "left arrow2 %s"

        action Jump("draw_corrD4")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 1696
        ypos 840

        focus_mask True

        auto "right arrow2 %s"

        action Jump("draw_corrD3")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 904
        ypos 556

        focus_mask True

        auto "forward arrow %s"

        action Jump("draw_corrB1")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 540
        ypos 364

        focus_mask True

        auto "valdoor %s"

        action Jump("valdoor")

    imagebutton:
        xpos 664
        ypos 384

        focus_mask True

        auto "aindoor %s"

        if flagA == 1:
            hovered Show("doors")
            unhovered Hide("doors")

        action [
            Hide("jump"),
            Jump("aindoor")
        ]

    imagebutton:
        xpos 1136
        ypos 384

        focus_mask True

        auto "osadoor %s"

        action Jump("osadoor")

    imagebutton:
        xpos 1244
        ypos 364

        focus_mask True

        auto "xdoor3 %s"

        action Jump("Xdoor3")

    add "darkborder":
        blend "multiply"
        alpha 0.8


label draw_corrD1:
    if currentlocation != "corrD1":
        scene bg corrd1_full with fade
        $ currentlocation = "corrD1"
    elif currentlocation == "corrD1":
        scene bg corrd1_full

    call screen corrD1

label kevdoor:
    if flagA == 1:
        np "There's a door with what I think is a horseshoe crab drawn on it."

        if corrD1read[0] == 0:
            play sound "audio/knock.wav"
            np "..."
            np "No response."

            $ corrD1read[0] = 1
            $ roomtotal += 1

    if currentlocation == "corrD1":
        jump draw_corrD1
    else:
        jump draw_corrD2

label valdoor:
    if flagA == 1:
        np "There's a door with lizard, probably some kind of monitor, drawn on it."

        if corrD1read[1] == 0:
            play sound "audio/knock.wav"
            np "..."
            np "No response."

            $ corrD1read[1] = 1
            $ roomtotal += 1

    if currentlocation == "corrD1":
        jump draw_corrD1
    else:
        jump draw_corrD2

label aindoor:
    if flagA == 1:
        np "There's a door with a ferret-looking mammal drawn on it."

        if corrD1read[2] == 0:
            play sound "audio/knock.wav"
            np "..."
            np "Interestingly, there's no response."

            $ corrD1read[2] = 1
            $ roomtotal += 1

    if currentlocation == "corrD1":
        jump draw_corrD1
    else:
        jump draw_corrD2

label osadoor:
    if flagA == 1:
        np "There's a door with a beetle of some sort drawn on it."

        if corrD1read[3] == 0:
            play sound "audio/knock.wav"
            np "..."
            np "No response."

            $ corrD1read[3] = 1
            $ roomtotal += 1

    if currentlocation == "corrD1":
        jump draw_corrD1
    else:
        jump draw_corrD2

label Xdoor3:
    if flagA == 1:
        np "There's a door with a red X painted on it. I get the feeling that there's nothing inside."

    if currentlocation == "corrD1":
        jump draw_corrD1
    else:
        jump draw_corrD2

label Xdoor4:
    if flagA == 1:
        np "There's a door with a red X painted on it. I get the feeling that there's nothing inside."

    if currentlocation == "corrD1":
        jump draw_corrD1
    else:
        jump draw_corrD2


#Corridor D2

screen corrD2:
    add "bg corrd2"

    imagebutton:
        xpos 1500
        ypos 904

        focus_mask True

        auto "turnarrow %s"

        action Jump("draw_corrB1")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 788
        ypos 444

        focus_mask True

        auto "left arrow %s"

        action Jump("draw_corrD3")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 884
        ypos 444

        focus_mask True

        auto "rightarrow %s"

        action Jump("draw_corrD4")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 116
        ypos 268

        focus_mask True

        auto "osadoor2 %s"

        action Jump("osadoor")

    imagebutton:
        xpos 516
        ypos 336

        focus_mask True

        auto "xdoor32 %s"

        action Jump("Xdoor3")

    imagebutton:
        xpos 688
        ypos 364

        focus_mask True

        auto "xdoor42 %s"

        action Jump("Xdoor4")

    imagebutton:
        xpos 1028
        ypos 348

        focus_mask True

        auto "kevdoor2 %s"

        action Jump("kevdoor")

    imagebutton:
        xpos 1172
        ypos 312

        focus_mask True

        auto "valdoor2 %s"

        action Jump("valdoor")

    imagebutton:
        xpos 1496
        ypos 228

        focus_mask True

        auto "aindoor2 %s"

        if flagA == 1:
            hovered Show("doors")
            unhovered Hide("doors")

        action [
            Hide("doors"),
            Jump("aindoor")
        ]

    add "darkborder":
        blend "multiply"
        alpha 0.8


label draw_corrD2:
    if currentlocation != "corrD2":
        scene bg corrd2_full with fade
        $ currentlocation = "corrD2"
    elif currentlocation == "corrD2":
        scene bg corrd2_full

    call screen corrD2

#Corridor D3

screen corrD3:
    add "bg corrd3"

    imagebutton:
        xpos 1434
        ypos 902

        focus_mask True

        auto "turnarrow %s"

        action Jump("draw_corrD4")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 272
        ypos 906

        focus_mask True

        auto "left arrow2 %s"

        action Jump("draw_corrD1")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 560
        ypos 0

        focus_mask True

        auto "dormdoor3 %s"

        action Jump("blockdoor")

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_corrD3:
    if currentlocation != "corrD3":
        scene bg corrd3_full with fade
        $ currentlocation = "corrD3"
    elif currentlocation == "corrD3":
        scene bg corrd3_full

    call screen corrD3

label blockdoor:
    if flagA == 1:

        if corrDdoorread[0] == 0:
            np "This is probably the most intense 'do not enter' warning I've seen in a while."
            np "They're almost overdoing it."
            pk "We probably shouldn't try going through here, it's probably dangerous."

            show darya grumpy with dissolve2
            dk "Hey, a sign like this is proof there's something they don't want us getting at - like treasure!"
            np "Or 'death', as the signage more readily implies."
            show darya anger with fastDissolve
            dk "{piracow}Let me try t' open it.{/piracow}"
            dk "{piracow}It may need some force.{/piracow}"
            hide darya with dissolve2

            np "Darya tried rattling the handle and kicking on the door, but to no avail."

            show darya yikes with dissolve2
            dk "..."

            pk "..."

            hide darya with dissolve2

            pk "Let's just assume we're not getting in right now."

            $ roomtotal += 1
            $ corrDdoorread[0] = 1
            jump draw_corrD3

        elif corrDdoorread[0] == 1:
            np "The door is sealed off despite Darya's best efforts, seems we won't be able to get through anytime soon. Thankfully."
            jump draw_corrD3


    if currentlocation == "corrD3":
        jump draw_corrD3
    else:
        jump draw_corrD3

#Corridor D4

screen corrD4:
    add "bg corrb3"
    imagebutton:
        xpos 1434
        ypos 902

        focus_mask True

        auto "right arrow2 %s"

        action Jump("draw_corrD1")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 272
        ypos 906

        focus_mask True

        auto "turnarrow2 %s"

        action Jump("draw_corrD3")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 648
        ypos 56

        focus_mask True

        auto "dormdoor2 %s"

        action Jump("draw_corrC1")

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_corrD4:
    if currentlocation != "corrD4":
        scene bg corrb3_full with fade
        $ currentlocation = "corrD4"
    elif currentlocation == "corrD4":
        scene bg corrb3_full

    call screen corrD4

#=================#
# Rest of Floor-1 #
#=================#

#Corridor E1

screen corrE1:
    add "bg corre1"
    imagebutton:
        xpos 644
        ypos 364

        focus_mask True

        auto "e1tolaundry %s"

        action Jump("draw_laundry")

    imagebutton:
        xpos 1480
        ypos 252

        focus_mask True

        auto "e1tof1 %s"

        action Jump("draw_corrF1")

    imagebutton:
        xpos 230
        ypos 820

        focus_mask True

        auto "turnarrow2 %s"

        if wiggle:
            at buttup2

        if flagA == 2:
            action Jump("nogood2")
        else:
            action Jump("draw_corrC1")

    add "darkborder":
        blend "multiply"
        alpha 0.8

label nogood2:
    np "There's currently no need for us to go back to the dorms."
    jump draw_corrE1

label draw_corrE1:
    if currentlocation != "corrE1":
        scene bg corre1_full with fade
        $ currentlocation = "corrE1"
    elif currentlocation == "corrE1":
        scene bg corre1_full

    if flagA == 1:
        $ flagA = 2

        pk "Well that's... interesting."

        show darya yeah1 with dissolve2
        dk "{piracow}The stairs down be barricaded.{/piracow}"

        pk "Yeah, seems we're gonna be stuck on this floor for a while."

        show darya bois with fastDissolve
        dk "All that means is less to investigate."
        hide darya with dissolve2

        pk "I suppose..."
        np "She's awfully chill about this whole situation."


    call screen corrE1


#Laundry Room**

screen laundry:
    add "bg laundry"

    imagebutton:
        xpos 1530
        ypos 890

        focus_mask True

        auto "turnarrow %s"

        action Jump("draw_corrE1")

        if wiggle:
            at buttup2

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_laundry:
    if currentlocation != "laundry":
        scene bg laundry_full with fade
        $ currentlocation = "laundry"
    elif currentlocation == "laundry":
        scene bg laundry_full

    call screen laundry


#Corridor F1

screen corrF1:
    add "bg corrf1"

    imagebutton:
        xpos 116
        ypos 184

        focus_mask True

        auto "e1f1gameroom %s"

        if corrF1read[0] == 0:
            action Jump("nogood3")
        else:
            action Jump("draw_corrE1")

    imagebutton:
        xpos 1400
        ypos 268

        focus_mask True

        auto "f1e1gameroom %s"

        if corrF1read[0] == 0:
            action Jump("nogood3")
        else:
            action Jump("draw_recroom")

    imagebutton:
        xpos 1500
        ypos 900

        focus_mask True

        auto "right arrow2 %s"

        if wiggle:
            at buttup2

        if corrF1read[0] == 0:
            action Jump("nogood3")
        else:
            action Jump("draw_corrG1")

    if flagA == 2:
        imagebutton:
            xpos 1100
            ypos 300

            focus_mask True

            auto "nindefault %s"

            action Jump("nincorrconvo1")

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_corrF1:
    if currentlocation != "corrF1":
        scene bg corrf1_full with fade
        $ currentlocation = "corrF1"
    elif currentlocation == "corrF1":
        scene bg corrf1_full

    call screen corrF1

label nogood3:
    np "There's someone in the corridor who I should probably speak to first."

    jump draw_corrF1

label nincorrconvo1: #nintro

    if corrF1read[0] == 1:
        np "Nin probably isn't going to be receptive to further conversation."

    elif corrF1read[0] == 0:
        show nin greet with dissolve2
        "{uk}Woman in Helmet{/uk}" "Hello there!"

        np "The woman at the other end of the hall called out to us cheerfully as she approached."

        hide nin with fastDissolve
        show nin neutral at tworight with fastDissolve

        show darya neutral at twoleft with dissolve2
        dk "Hello!"

        pk "Hi."

        nt "I'm Nin, who're you two?"

        show darya yeah2 with fastDissolve
        dk "I'm Captain Darya Valtis!"

        show nin uncomf with fastDissolve


        pk "Call me Phantom Magpie."
        np "I'm getting a little sick of introducing myself like this."
        np "Also getting a little tired of Darya using some random-ass fake word as her last name each time..."

        show darya neutral with fastDissolve

        nt "... What are you the captain of?"

        show darya ohyeah with fastDissolve
        dk "{piracow}The greatest ship on the seven seas - The Dragonflight!{/piracow}"

        nt "Hmm. Do you have a... crew?"

        show darya hh with fastDissolve
        dk "Not quite - {piracow}she- um... me ship...{/piracow}"
        dk "{size=-10}Well, for right now I {i}do{/i} have Magpie here...{/size}"

        show nin neutral
        show darya yeah1
        with fastDissolve

        dk "Unless you want to join us?"

        show nin nope with fastDissolve
        nt "No thank you. I'm currently trying to look for other people to- to see if we can discuss anything about our situation."
        nt "But I've only managed to find a few other people so far."
        show nin point with fastDissolve
        nt "In fact, through this door is a game room - there's two people, called Belinda and Osanne, in there."
        nt "They seemed friendly enough if you wanna go say hi."
        nt "Though I wouldn't be opposed to you tagging along in my search."

        hide nin
        hide darya 
        with fastDissolve

        stop music fadeout 1.0
        scene black with dissolve

        show nin point with fastDissolve

        window hide dissolve
        pause 0.8

        hide nin with fastDissolve
        
        window auto
        
        np "As Nin points to the door with her left arm, I notice a strange new-looking vertical scar, still with stitches in, on her forearm."
        np "Seeing it causes me to grab my own left arm, the strange stinging hasnt faded, and a worrying pit formed in my gut."

        scene bg corrf1_full with dissolve

        show nin neutral with fastDissolve

        pk "Before you continue, I need to know if you woke up with that cut on your arm."

        show nin uncomf with fastDissolve
        nt "Huh? Oh yeah, this is new, but it isn't really bothering me and there's more important things to be doing."
        nt "Besides, I tried poking at it earlier and it kinda stung and felt tingly."
        show nin neutral with fastDissolve
        nt "So I'm opting to ignore it for now, since the only other option is to freak out about it."

        np "I quickly pull down my sleeve to get a look at my arm, I'd been distracted til now but-"

        hide nin with fastDissolve

        play music "audio/threat.mp3" fadein 1.0
        scene bg armscarcg with fade

        np "The worrying feeling quickly turned to panic."
        np "Thoughts of what our kidnappers could have done to us while we were unconscious raced through my mind."
        np "I resisted the wretched desire to scratch at it and rip the stitches out, instead opting to steady my breathing."

        #scene bg armscarcg2 with flashbulb

        dk "Oh thats- that's not good..."

        np "I looked up and saw Darya staring at her own arm, eyes wide and horrified."

        scene bg corrf1_full with dissolve

        show nin nope at tworight
        show darya worry at twoleft
        with fastDissolve

        nt "Are you two okay? Do you know what the arm marks mean?"

        show darya sad with fastDissolve
        dk "No we don't! And that's the problem!"

        stop music fadeout 1.0

        show nin point with fastDissolve
        nt "Well, I did notice something that looked like a medical room down the hall there."
        nt "There's also a couple more people in it, I believe one of them said he was a nurse."
        show nin neutral with fastDissolve
        nt "If you want to head over and see if he might be able to help you."

        dk "Y-yeah thanks, we'll have a look."

        play music "audio/wandering.mp3" fadein 1.0

        show nin greet with fastDissolve
        nt "If that's sorted, I'm going to go find some other people to greet."
        nt "Based on the amount of doors with pictures on, there's probably 16 people all told?"
        show nin thonk with fastDissolve
        nt "Although, I'm pretty certain it's actually 15 people and 1 horse. Based on my brief conversation with Emilio."

        show darya ask2 with fastDissolve 
        dk "Uh, who?"

        np "I sigh."
        pk "That guy you hate."

        show darya grumpy with fastDissolve
        dk "Horseboy..."

        show nin nope with fastDissolve
        nt "I'm... I don't think I can deal with you, so I'm going to head off. See ya."
        hide nin with dissolve2

        np "Rightfully concerned, Nin slipped away down the corridor."

        hide darya with dissolve2

        np "Guess we should go find some other people too."

        $ clues.update( {7 : "Scars on Arm"} )
        $ clues_text[7][0] = "Each of us woke up with a frightening scar on our left forearm, I am completely unsure what happened to cause them and the implications haunt me."
        "Notes on 'Scars on Arm' have been jotted down."


        $ corrF1read[0] = 1
        $ asktotal += 1

    if currentlocation == "corrF2":
        jump draw_corrF2
    elif currentlocation == "corrF1":
        jump draw_corrF1

#Corridor F2

screen corrF2:
    add "bg corrf2"
    imagebutton:
        xpos 116
        ypos 184

        focus_mask True

        auto "e1f1gameroom %s"

        action Jump("draw_recroom")

    imagebutton:
        xpos 1400
        ypos 268

        focus_mask True

        auto "f1e1gameroom %s"

        action Jump("draw_corrE1")

    imagebutton:
        xpos 800
        ypos 500

        focus_mask True

        auto "left arrow %s"

        action Jump("draw_corrG1")

        if wiggle:
            at buttup2

    if flagA == 2:
        imagebutton:
            xpos 600
            ypos 300

            focus_mask True

            auto "nindefault %s"

            action Jump("nincorrconvo1")

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_corrF2:
    if currentlocation != "corrF2":
        scene bg corrf2_full with fade
        $ currentlocation = "corrF2"
    elif currentlocation == "corrF2":
        scene bg corrf2_full

    if flagA == 2 and asktotal == 7:
        jump allintroviewed    

    call screen corrF2


#Rec Room

screen recroom:
    add "bg recroom"

    imagebutton:
        xpos 1450
        ypos 900

        focus_mask True

        auto "turnarrow %s"

        action Jump("draw_corrF2")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 344
        ypos 308

        focus_mask True

        auto "recshelves %s"

        action Jump("recshelves")

    imagebutton:
        xpos 1012
        ypos 456

        focus_mask True

        auto "recpc %s"

        action Jump("recpc")



    add "rectables":
        xpos 40
        ypos 568

    imagebutton:
        xpos 400
        ypos 350

        focus_mask True

        auto "belindadefault %s"

        action Jump("belintro")

    imagebutton:
        xpos 1200
        ypos 300

        focus_mask True

        auto "osannedefault %s"

        action Jump("osaintro")

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_recroom:
    if currentlocation != "recroom":
        scene bg recroom_full with fade
        $ currentlocation = "recroom"
    elif currentlocation == "recroom":
        scene bg recroom_full

    call screen recroom

label recshelves:
    np "There's a large shelving unit filled with a variety of board games and TTRPG books."
    "(Theoretically)"

    jump draw_recroom

label recpc:
    np "There's a computer at the back of the room, though it refuses to turn on."
    
    if daryaroom:
        np "That doesn't seem to be stopping Darya's attempts to get it working, however."

    jump draw_recroom


label belintro:

    if recroomeread[2] == 0:
        show belinda neutral with dissolve2
        "{uk}Woman With Reptiles{/uk}" "Hiya there you two."
        hide belinda with fastDissolve

        show belinda neutral at tworight

        show darya hm at twoleft

        with fastDissolve

        dk "Yeah, hiya."

        show belinda ohno with fastDissolve
        "{uk}Woman With Reptiles{/uk}" "Oh dear, are you feeling alright? You look a little shaken."

        show darya bois with fastDissolve
        dk "{piracow}Aye matey, I be in ship-shape!{/piracow}"

        show belinda sadsmile with fastDissolve
        "{uk}Woman With Reptiles{/uk}" "Well, as long as you're okay."

        pk "Sorry to ask this {i}again{/i}, Darya, but do you know this person?"

        show belinda huh with fastDissolve
        "{uk}Woman With Reptiles{/uk}" "Huh?"

        show darya ask2 with fastDissolve
        dk "What? No."

        "{uk}Woman With Reptiles{/uk}" "Do I have to already know someone to ask if they're okay if something seems off?"

        pk "I dunno, you two just seemed friendly is all."


        show darya yeah1
        show belinda neutral
        with fastDissolve

        dk "{piracow}If we're truly to be friends, then introductions be in order!{/piracow}"
        dk "I'm Darya, and this is Magpie." 

        "{uk}Woman With Reptiles{/uk}" "It's nice to meet you."
        show belinda excite with fastDissolve
        bl "On my end, the snake is Luna, the chameleon is Sol, and I'm Belinda!"
        show belinda neutral with fastDissolve

        np "Awful lot of animals in this place..."

        pk "That's interesting, there's a guy with a horse {nw}" 
        
        show darya grumpy with FD2
        
        extend "back in the dorms."
        pk "He didn't have any idea why his horse was brought with him, but do you have any clues?"

        show darya neutral
        show belinda ohno
        with fastDissolve

        bl "Last thing I remember before I passed out and woke up here they were with me."
        show belinda huhno with fastDissolve
        bl "So maybe they just grabbed us as a whole package?"
        show belinda sadsmile with fastDissolve
        bl "Actually, now that I think about it, these two are pretty special."
        bl "It could be important that they're here."
        show belinda neutral with fastDissolve

        np "I mean, we don't even know the importance of {i}our{/i} being here yet."

        show darya yikes with fastDissolve
        dk "{piracow}Aye well, I'm sure everyone would say {i}their{/i} pets be the special-est, don't ye think?{/piracow}"

        show belinda letsee with fastDissolve
        bl "..."
        show belinda ohno with fastDissolve
        bl "You see, Luna and Sol are former 'patients' of a company called Eclipse."

        show darya worry with fastDissolve

        bl "And, put simply, Eclipse were doing horrible things to animals in their custody, believing that it could make them develop a human level of intelligence."
        bl "I... uh, ended up there one day, realised what they were doing, and was able to grab these two before they could catch me."
        show belinda ohnono with fastDissolve
        bl "My only regret is that I wasn't able to save more of them..."

        pk "Since you called them special, does that mean that those 'horrible things' worked then?"

        bl "Unfortunately yeah, they seemed to be onto something. Luna and Sol exhibit behaviours and emotions that aren't normal for their species."
        show belinda sadsmile with fastDissolve
        bl "I don't think I'm anthropomorphising them when I say that they're a lot more attached to me than normal reptiles are..."

        show darya hh with fastDissolve
        dk "Whatever they were doing it's a shame that it worked, only gives them reason to continue..."

        pk "At least you managed to save these ones, I'm sure they appreciate it."

        bl "Thanks, I'm sure they do."

        show darya neutral
        show belinda neutral 
        with fastDissolve

        pk "And, well, it's been nice speaking to you, but me and Darya should probably go to try and keep finding information about our situation."
        pk "We're not having much luck but there's seemingly quite a few people here, and at least someone might know {i}something{/i}."

        show belinda letsee with fastDissolve
        bl "Good point, I haven't really spoken to many people yet. I'm kinda just hanging out in here cus I'm a little on edge to be honest."

        show darya ask1 with fastDissolve
        dk "{piracow}Oh, do ye wish to join us?{/piracow} We could always use the help."

        show belinda sadsmile with fastDissolve
        bl "Oh, n-no thanks. I might check the place out later on my own, but for right now I think this is my limit given the circumstances."
        show belinda neutral with fastDissolve
        bl "But I hope your investigation goes well."

        dk "Thanks, {piracow}and farewell matey.{/piracow}"
        hide darya

        hide belinda

        with dissolve2

        $ asktotal += 1
        $ recroomeread[2] = 1
        jump draw_recroom

    elif recroomeread[2] == 1:
        np "Belinda is sat at the table with her reptiles, she probably doesn't want to be bothered."
        jump draw_recroom

label osaintro:

    if recroomeread[3] == 0:
        show osanne yeah with dissolve2
        "{uk}Wizard Lady{/uk}" "Greetings!"
        hide osanne with fastDissolve

        show darya neutral at twoleft
        show osanne neutral at tworight
        with fastDissolve

        dk "Hello!"

        show darya worry 
        show osanne blung
        with fastDissolve

        "{uk}Wizard Lady{/uk}" "No, not you! Your friend!"

        np "Darya dejectedly made her way to a table and sat down."

        hide darya
        hide osanne
        with fastDissolve

        show osanne neutral with fastDissolve

        pk "Why are you-"
        with flashbulb
        np "In a flash I realised why this person took a sudden interest in me."
        pk "You're... you've Manifested, like me, aren't you?"

        show osanne yeah with fastDissolve

        "{uk}Wizard Lady{/uk}" "Yep!"

        np "She took off her hat, revealing a set of antenna underneath."

        show osanne neutral2 with fastDissolve
        "{uk}Wizard Lady{/uk}" "I'm a violet ground beetle!"
        show osanne neutral with fastDissolve
        "{uk}Wizard Lady{/uk}" "And you..."
        show osanne thinky with fastDissolve
        "{uk}Wizard Lady{/uk}" "You're clearly some kind of bird right?"
        "{uk}Wizard Lady{/uk}" "Probably a magpie, I'd say? Based on your getup."

        show osanne yeah with fastDissolve
        pk "That's right, specifically a common Eurasian magpie."
        show osanne neutral with fastDissolve
        pk "To be honest, I wasn't expecting to find anyone else who's Manifested in such a small group of people."

        show osanne whoo with fastDissolve
        "{uk}Wizard Lady{/uk}" "You {i}are{/i} a bird! Does that mean you can fly?"
        show osanne dissapointed with fastDissolve
        "{uk}Wizard Lady{/uk}" "The closest I can do is stick to walls. Can't believe my Manifest is a {i}flightless{/i} beetle, glueing me to the ground forever..."

        pk "Oh, no, not really. I can glide a bit and catch myself when I fall but it's not really 'flight'."
        show osanne neutral with fastDissolve
        pk "Honestly, for me wall climbing would be a lot more useful; it's always nerve-wracking when I lose my footing."
        np "I chuckle awkardly."

        show osanne blung with fastDissolve
        "{uk}Wizard Lady{/uk}" "Dang, if only we could swap y'know. But I do quite like my antennae."
        show osanne thinky with fastDissolve
        "{uk}Wizard Lady{/uk}" "Oh! I never actually asked, how has your Manifest expressed itself on you?"
        show osanne neutral with fastDissolve

        pk "Mostly as feathers and bird scales on my hands and forearms."
        pk "Do you... want to see?"

        show osanne yeah with fastDissolve
        "{uk}Wizard Lady{/uk}" "Absolutely!"
        show osanne neutral with fastDissolve

        np "I hesitantly removed a glove and pulled up my sleeve, revealing the feathers on my forearm and the scales on the back of my hand."
        pk "It doesn't look great, I know. I always wear gloves to cover it up..."

        "{uk}Wizard Lady{/uk}" "No I think it looks cool! {size=-10}But I might just be biased cus I find Manifests fascinating.{/size}"

        pk "... {w=0.5} {i}Ahem{/i}, well, anyway, I assume your hat is to cover up your antennae, but I was wondering about the wizard staff. What's that about?"

        show osanne yeah with fastDissolve
        "{uk}Wizard Lady{/uk}" "Aha! You see, I am a potion master! A scholar of alchemy!"

        pk "What?"

        show osanne blung with fastDissolve
        "{uk}Wizard Lady{/uk}" "I'm a chemist, and {i}also{/i} a botanist! {size=-10}Everyone always forgets my other qualification...{/size}"

        pk "In what way?"

        "{uk}Wizard Lady{/uk}" "I got an award for some chemistry research - the title and descriptor of which will probably go over your head - but I've never had any formal recognition for my botanical achievements!"
        show osanne dissapointed with fastDissolve
        "{uk}Wizard Lady{/uk}" "And I'm {i}so{/i} much more proud of those!"

        pk "Ooh, what have you done in botany?"
        show osanne yeah with fastDissolve
        np "She began to explain, but Darya was slowly inching her way back into our conversation, catching our attention."

        show osanne grump with fastDissolve
        "{uk}Wizard Lady{/uk}" "and it's still never-"
        show osanne blung 
        show darya hh:
            xpos -300
        with fastDissolve
        "{uk}Wizard Lady{/uk}" "Oh hello again."
        hide osanne 
        hide darya
        with fastDissolve

        show darya hh at twoleft
        show osanne blung at tworight
        with fastDissolve

        dk "Hi."

        pk "Hi Darya."
        np "There was a slight pause before Darya straightened herself and unsheathed her sword."

        show darya yeah1 with fastDissolve
        dk "{piracow}A-ahoy there, me hearties! I hope Magpie has been treating ye well.{/piracow}"

        show osanne thinky with fastDissolve
        "{uk}Wizard Lady{/uk}" "That's your name? We never introduced each other, did we?"
        show osanne neutral with fastDissolve
        of "I'm Osanne, nice to meet you, Magpie."

        pk "Yeah, it's nice to meet you."

        show darya neutral with fastDissolve
        dk "{piracow}And I be Captain Darya.{/piracow}"
        show darya hm with fastDissolve
        dk "{piracow}I overheard ye mention botany, and were wondering if ye had any thoughts on the cactuses in our quarters.{/piracow}"

        pk "Oh yeah, since we seem to be underground they'll probably die soon."

        show osanne thinky2 with fastDissolve
        of "After reading that 'dorms' sign I was thinking that there might be UVB in the lights, since if we're to be down here for a while it won't be great on us, either."
        show osanne dissapointed 
        show darya worry
        with fastDissolve
        of "There'd be no reason to put a desert plant in a cold, sunless prison just to leave it to die."
        show osanne neutral with fastDissolve

        pk "That makes sense actually, I never would have thought about it like that."

        show darya hm with fastDissolve
        dk "{piracow}That be interesting! {/piracow}{size=-10}Magpie would you mind if we left?{/size}"

        pk "Right, we were going to try and explore this place and see what we can investigate."
        pk "It would be nice to talk to you again later, though."

        show osanne yeah with fastDissolve
        of "Okay, see ya!"

        hide darya
        hide osanne
        with fastDissolve


        $ clues_text[4].append("Osanne brought up the idea that there might be 'UVB' in the lights to prevent the plants from dying, since it'll also stop us from suffering the consequences of too little sunlight as well.")
        "Notes on 'Small Cactus' have been updated."


        $ asktotal += 1
        $ recroomeread[3] = 1
        jump draw_recroom
    
    elif recroomeread[3] == 1:
        np "It would be too awkward to speak to her again after Darya forced me to bail out of the conversation."

        jump draw_recroom


#Corrdor G1

screen corrG1:
    add "bg corrg1"

    imagebutton:
        xpos 884
        ypos 340

        focus_mask True

        auto "exit %s"

        action Jump("gexitsign")

    imagebutton:
        xpos 1000
        ypos 400

        focus_mask True

        auto "rightarrow %s"

        action Jump("draw_corrH1")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 332
        ypos 276

        focus_mask True

        auto "g1kitchen %s"

        action Jump("draw_dhall")

    imagebutton:
        xpos 732
        ypos 336

        focus_mask True

        auto "g1med %s"

        action Jump("draw_medbay")

    imagebutton:
        xpos 400
        ypos 870

        focus_mask True

        auto "left arrow2 %s"

        action Jump("draw_corrF1")

        if wiggle:
            at buttup2

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_corrG1:
    if currentlocation != "corrG1":
        scene bg corrg1_full with fade
        $ currentlocation = "corrG1"
    elif currentlocation == "corrG1":
        scene bg corrg1_full

    if flagA == 2 and asktotal == 7:
        jump allintroviewed

    call screen corrG1

label gexitsign:
    np "There's a very suspicious sign here with a label I don't quite trust."

    jump draw_corrG1

#Corridor G2

screen corrG2:
    add "bg corrg2"

    imagebutton:
        xpos 1000
        ypos 400

        focus_mask True

        auto "rightarrow %s"

        action Jump("draw_corrF1")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 1576
        ypos 236

        focus_mask True

        auto "g2med %s"

        action Jump("draw_medbay")

    imagebutton:
        xpos 1176
        ypos 320

        focus_mask True

        auto "g2kitchen %s"

        action Jump("draw_dhall")

    imagebutton:
        xpos 250
        ypos 830

        focus_mask True

        auto "left arrow2 %s"

        action Jump("draw_corrH1")

        if wiggle:
            at buttup2

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_corrG2:
    if currentlocation != "corrG2":
        scene bg corrg2_full with fade
        $ currentlocation = "corrG2"
    elif currentlocation == "corrG2":
        scene bg corrg2_full

    if flagA == 2 and asktotal == 7:
        jump allintroviewed

    call screen corrG2


#Dining Hall

screen dininghall:
    add "bg dininghall"

    imagebutton:
        xpos 0
        ypos 364

        focus_mask True

        auto "dhalltohall %s"

        action Jump("draw_corrG1")

    imagebutton:
        xalign 1.0
        ypos 380

        focus_mask True

        auto "dhalltokitchen %s"

        action Jump("draw_kitchen")

    imagebutton:
        xpos 650
        ypos 350

        focus_mask True

        auto "carwyndefault %s"

        action Jump("carintro")

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_dhall:
    if currentlocation != "dhall":
        scene bg dininghall_full with fade
        $ currentlocation = "dhall"
    elif currentlocation == "dhall":
        scene bg dininghall_full

    call screen dininghall

label carintro:
    if dhallread[0] == 0:
        np "There's a gaunt man hunched over at the table, scribbling in a notebook and muttering to himself."
        np "He doesn't seem to notice as we approach."

        show darya neutral with dissolve2
        dk "{size=+10}Ahoy! How goes it?{/size}"

        np "The man flinched thanks to Darya's outburst, his sudden movement leaving a streak of ink across his page."
        np "He slowly stood up, pushed his chair in, and glared at us."

        hide darya with fastDissolve

        show darya neutral at twoleft
        show carwyn angy at tworight
        with fastDissolve

        "{uk}Man With Book{/uk}" "How dare you, were you never educated in the proper manners with which to navigate the social domain around an artist at work!?"
        show carwyn tipped 
        show darya grumpy
        with fastDissolve
        "{uk}Man With Book{/uk}" "Were you raised in a barn? Or perhaps by wolves?"

        show darya threat with fastDissolve
        dk "{piracow}Ye would never catch me alive in such a filthy place! I were raised by the sea herself, upon the deck of a glorious vessel.{/piracow}"

        #ht "{bt=h5-p5-s2.0}testing{/bt}"
        #ht "{sc=3}testing{/sc}"
        #ht "{swap=te@t3@0.2}te{/swap}{swap=st@57@0.15}st{/swap}{swap=ing@1n6@0.17}ing{/swap}"

        show carwyn ha with fastDissolve
        "{uk}Man With Book{/uk}" "Your terrid implication that the filth of the ocean doesn't outweigh the stench of the land further evidences your lowly status."

        show darya hm with fastDissolve

        "{uk}Man With Book{/uk}" "To think such a simpleton as you could conceivably conclude to manifest in the same sphere as I."
        show carwyn angy with fastDissolve
        "{uk}Man With Book{/uk}" "Such utter lack of consternation at the disruption of another's deliberation and personal space indicates aforesaid senselessness."
        show carwyn ango with fastDissolve
        "{uk}Man With Book{/uk}" "Perhaps your ilk merely finds it appropriate to construct a tomb upon someone else's misery."

        np "How can you upset someone this much with so few words Darya..."
        np "I should step in before someone's pride takes an irrepairable hit."

        show darya grumpy with fastDissolve

        pk "Terribly sorry about Darya there, but now that you've brought it up, what {i}is{/i} your craft? Also, what's your name if you don't mind. I'm Magpie."

        show carwyn neutral with fastDissolve
        cm "My name is Carwyn."
        show carwyn itme with fastDissolve
        cm "I am an artificer of the written word, a smith of elegance, composing the majesty of poetry."

        np "Is that slang for 'I'm unemployed'?"
        pk "Sounds... interesting."

        show carwyn tipped with fastDissolve
        cm "How striking that someone of your calibre would take an interest in humanity's finest of crafts."
        cm "Perhaps I was mistaken to judge you by the lamentable companion in your wake."
        show carwyn angy with fastDissolve
        cm "Alas, I must return to the construction of my masterpiece, and you must recommence your silence if you wish to persist in my presence."

        np "With one final scowl, he returns to the table and picks up his pen once more."

        hide carwyn
        hide darya
        with fastDissolve
        show darya hm with fastDissolve

        np "Darya leans in to whisper something to me."

        dk "{size=-10}Magpie, I'm not the only one who thinks he's a bit, um, eccentric, right?{/size}"
        dk "{size=-10}He freaked me out a little.{/size}"

        pk "{size=-10}Yeah he's definitely a little off.{/size}"

        hide darya with dissolve2

        $ asktotal += 1
        $ dhallread[0] = 1
        jump draw_dhall

    elif dhallread[0] == 1:
        np "I fear that invoking any more of Carwyn's wrath could be... annoying. Let's leave him alone."

        jump draw_dhall


#Kitchen*

screen kitchen:
    add "bg kitchen"

    imagebutton:
        xpos 400
        ypos 880

        focus_mask True

        auto "turnarrow2 %s"

        action Jump("draw_dhall")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 800
        ypos 300

        focus_mask True

        auto "nikolasdefault %s"

        action Jump("nikratintro")

    imagebutton:
        xpos 600
        ypos 300

        focus_mask True

        auto "ratnadefault %s"

        action Jump("nikratintro")

    add "darkborder":
        blend "multiply"
        alpha 0.8


label draw_kitchen:
    if currentlocation != "kitchen":
        scene bg kitchen_full with fade
        $ currentlocation = "kitchen"
    elif currentlocation == "kitchen":
        scene bg kitchen_full

    call screen kitchen


label nikratintro:

    if kitchenread[0] == 0:
        np "There's two people rooting through the cupboards, excitedly chittering."
        np "Despite seeming to be distracted, they notice us quickly as we approach."

        show ratna hai at twoleft
        show nikolas yeah at tworight
        with dissolve2

        "{uk}Both{/uk}" "Hello~!"
        
        hide ratna
        hide nikolas
        with fastDissolve

        show darya neutral with fastDissolve
        dk "Hi!!"

        pk "Hey there..."

        hide darya with fastDissolve

        show darya neutral at twoleft
        show nikolas aha at tworight
        with dissolve2

        "{uk}Green Headband{/uk}" "Do you want to hear a tale of dangers untold and foul beasts unknown!"

        show darya yeah2 with fastDissolve
        dk "{piracow}Aye! Set the scene me-hearties.{/piracow}"
        hide darya with fastDissolve

        show nikolas neutral
        show ratna storytime at twoleft 
        with fastDissolve
        "{uk}Black Headband{/uk}" "Deep in the jungles of Peru..."

        show nikolas yaey with fastDissolve
        "{uk}Green Headband{/uk}" "Remnants of a monster hidden for {i}millions{/i} of years were uncovered by our intrepid explorer, but the path was not without strife."

        show ratna yousee with fastDissolve
        "{uk}Black Headband{/uk}" "The TITANOSAURUS, a brute weighing over 100 tonnes, made its presence known."

        show nikolas aha with fastDissolve
        "{uk}Green Headband{/uk}" "The fellowship had been searching for weeks, their supplies dwindling. They'd almost lost hope..."

        show ratna hmn with fastDissolve
        "{uk}Black Headband{/uk}" "Weathered surfaces were revealed to us, and our seemingly dire prospects came to fruition!"

        "{uk}Black Headband{/uk}" "And then-"

        show ratna neutral
        show nikolas neutral
        with fastDissolve        
        pk "Hold on, slow down. Can we get your names first, please?"

        show nikolas yeah with fastDissolve
        "{uk}Green Headband{/uk}" "They're Ratna!"

        show ratna hai with fastDissolve
        rh "And he's Nikolas! Anyway-"
        show ratna yousee with fastDissolve

        np "Despite my half-hearted efforts, they don't miss a beat in continuing their rambling. "

        show nikolas aha with fastDissolve

        np "Darya's on the edge of her seat but I zoned out a while ago."

        show ratna heh with fastDissolve
        rh "And that, my friends, is how I discovered the fourth largest titanosaur skeleton."

        hide nikolas with fastDissolve

        show darya yeah1 at tworight with fastDissolve
        dk "{piracow}So ye be a palaeontologist?{/piracow}"

        show ratna hai with fastDissolve
        rh "Yes! A discoverer of ancient beasts! Of both the foul and fascinating."

        hide ratna with fastDissolve

        show nikolas whoo at twoleft with fastDissolve
        nl "An archivist of a time before paper! As I am an archivist of the lands! A cartographer by trade."

        dk "{piracow}Yarr, a man without a map be like the sky without the stars.{/piracow}"

        show nikolas neutral with fastDissolve

        pk "You two are awfully in sync, are you, like, friends?"

        hide nikolas
        hide darya
        with fastDissolve

        show nikolas neutral at tworight
        show ratna owo at twoleft
        with fastDissolve

        rh "Nik helps with mapping out dig sites for me, so I'd consider us friends."

        show ratna neutral 
        show nikolas ahey
        with fastDissolve
        nl "We don't speak too often, but we've technically known each other for years!"

        pk "Interesting coincidence you're both here together, then."

        show nikolas eh 
        show ratna neutral
        with fastDissolve
        nl "Not really, because I don't know anyone else here! And I know quite a lot of people, so statistically I think it checks out."
        show nikolas neutral with fastDissolve
        nl "More importantly, I'm currently working on a map of this place. I noticed a couple locked doors, plus the barricaded stairs, so it might be important to visualise the floorplan."
        nl "Once I'm done I can give you a copy if you want?"

        pk "That'd be pretty handy actually, thanks."

        np "Ratna peers over to the map in Nikolas's hands."

        show ratna yousee with fastDissolve
        rh "Oh yeah, we should probably get back on that actually, seems like there's still some places yet to add. Talk to you later!"

        hide ratna with fastDissolve

        show darya neutral at twoleft with fastDissolve
        dk "Bye!"

        show nikolas yeah with fastDissolve
        nl "See ya!"

        pk "Yeah, goodbye."

        hide darya
        hide nikolas
        with dissolve2



        $ asktotal += 1
        $ kitchenread[0] = 1
        jump draw_kitchen
    elif kitchenread[0] == 1:
        np "I don't want to get dragged into another session of these two's rambling so I won't approach them again."

        jump draw_kitchen


#Medbay*

screen medbay:
    add "bg medbay"

    imagebutton:
        xpos 300
        ypos 880

        focus_mask True

        auto "turnarrow2 %s"

        action Jump("draw_corrG2")

        if wiggle:
            at buttup2

    imagebutton:
        xpos 800
        ypos 300

        focus_mask True

        auto "valkyriedefault %s"

        action Jump("valkevintro")

    imagebutton:
        xpos 1000
        ypos 300

        focus_mask True

        auto "kevindefault %s"

        action Jump("valkevintro")

    add "darkborder":
        blend "multiply"
        alpha 0.8


label draw_medbay:
    if currentlocation != "medbay":
        scene bg medbay_full with fade
        $ currentlocation = "medbay"
    elif currentlocation == "medbay":
        scene bg medbay_full

    call screen medbay


label valkevintro:

    if medbayread[0] == 0:
        np "There's two people sat on one of the beds, having a chat. They turn to us as we enter."

        show kevin neutral with dissolve2
        "{uk}Man in Medical Scrubs{/uk}" "Hello there you two!"
        hide kevin with fastDissolve

        show kevin neutral at tworight
        show darya yeah1 at twoleft
        with fastDissolve

        dk "Hey there!"
        dk "{piracow}I be Darya, and this here be Magpie.{/piracow} What about you?"

        np "I give a small wave at the mention of my name."

        show kevin yeep with fastDissolve
        ka "I'm Kevin, and this is my best friend Valkyrie!"

        hide darya with fastDissolve

        show valkyrie neutral1 at twoleft with fastDissolve
        vl "Heya."

        show kevin neutral with fastDissolve
        pk "Out of curiosity, are you two investigating this place? It's an awfully odd hangout spot if not."

        show valkyrie tipped with fastDissolve
        vl "Oh yeah, we've been having a look around ever since we woke up."
        show valkyrie aaan with fastDissolve
        vl "Kevin was super excited to check out the medical facilities and see what they had in stock."
        show valkyrie neutral1 with fastDissolve


        hide kevin 
        show darya hm at tworight 
        with fastDissolve
        dk "Did you {i}know{/i} there'd be medical facilities when you first woke up?"

        pk "After you read the 'dorm rules' sign it's a reasonable assumption to make, to be fair."

        hide valkyrie with fastDissolve

        show kevin aya at twoleft with fastDissolve
        ka "Nah, just stumbled across it as we were wandering about."
        show kevin hrm with fastDissolve
        ka "It's not like there's many rooms to this place, after all..."

        pk "A medical bay isn't normally a place someone is super excited to visit, any particular reason why it caught your eye?"

        show darya neutral with fastDissolve

        dk "People can be excited about anything, Magpie."

        show kevin neutral with fastDissolve
        ka "Ah, see, I'm currently studying to become a nurse, an anesthetist specifically."

        hide darya with fastDissolve
        
        show valkyrie neutral1 at tworight with fastDissolve
        vl "An anesthetist is in charge of monitoring a patient's vital signs, as well as giving anesthetics, pain killers, and the like."

        show kevin aya with fastDissolve
        ka "I've spent a lot of time in a ward during my placement, so I really wanted to see what this place was like."
        ka "Despite it's small size its quite similar to what I'm familiar with."

        hide valkyrie with fastDissolve

        show darya hh at tworight with fastDissolve
        dk "Okay, you're the nurse that Nin suggested we talk to."
        dk "Is there anything you could tell us about this?"

        np "She pulled up her sleeve, revealing the scar beneath."

        show kevin sad with fastDissolve
        ka "Oh yeah, that..."
        show kevin sad2 with fastDissolve
        ka "Me and Kyrie saw those too, based on how it's been sewn back up, and how neat it is, its definitely a post-surgery scar of sorts."
        show kevin sad with fastDissolve
        ka "But I can't work out the purpose, my best guess is that it was to implant something in us or otherwise modify that part of the inside of our forearm."
        ka "And since it's mostly past the 'hurting' part of recovering and just starting to itch, it's clear to me they've been healing for at least a few days to a week or so."
        ka "Which would mean we've been unconscious for a while, which is worrying."

        $ clues_text[7].append("Kevin suggests that the (seemingly surgical) scars on our arms could be indicative that something was modified about or implanted into our forearms. They look like they've been healing for a while, so how long was it since we were knocked out?")
        "Notes on 'Scars on Arm' have been updated."

        hide darya with fastDissolve

        show valkyrie thatbad at tworight with fastDissolve
        vl "We settled on deciding to leave it be for now, since it currently isn't causing any harm and we can't do much about it."
        vl "Besides, Kevin isn't technically qualified yet. {size=-10}Nor is he even technically a surgeon...{/size}"

        show kevin sad2 with fastDissolve
        ka "'Sides, surgeries near major arteries can go really wrong really quickly, and I don't think the facilities here are suitable to handle sudden and extreme bloodloss."

        pk "Shame, you even seem to be wearing the right clothes for it. Those are medical scrubs, right?"

        show kevin hrm with fastDissolve
        ka "Nah, this is a dressing gown, I don't go out on the town in medical garments."
        show kevin sys 
        show valkyrie neutral1
        with fastDissolve
        ka "Well, I don't {i}go out{/i} in pyjamas usually, either..."

        hide kevin with fastDissolve

        show darya ask2 at twoleft with fastDissolve
        dk "You're in pyjamas?"
        show darya ask1 with fastDissolve
        dk "Anyway, I was wondering what you did, Valkyrie, since Kevin's just told us all about his work."

        show valkyrie um with fastDissolve
        vl "Oh, right, um. I'm a computer scientist, specifically I work in cyber security at one of Reawaken Immunity's hospitals."
        show valkyrie aaan with fastDissolve
        vl "It's the same one that Kevin's interning at, actually."

        hide darya with fastDissolve

        show kevin blep at twoleft with fastDissolve
        ka "You say that like it was coincidence, you know I chose the same one on purpose."

        show kevin neutral 
        show valkyrie neutral1
        with fastDissolve

        pk "Huh, how long have you two known each other then?"
        pk "Must've been a while if you're basing your life plans on one another."

        show kevin yeep with fastDissolve
        ka "We've known each other since the start of A-levels, so about 6 years now."

        show valkyrie aaan with fastDissolve
        vl "Yeah, I finished my computer science degree {i}a couple{/i} years earlier than Kev's medical degree is taking him."
        show valkyrie tipped with fastDissolve
        vl "So I basically got to choose where we ended up working at."
        vl "Not like we didn't talk it through though, of course."

        hide kevin with fastDissolve

        show darya neutral at twoleft with fastDissolve
        dk "Working alongside someone you deeply care about as a long term plan sounds nice."

        hide darya
        hide valkyrie
        with fastDissolve

        np "Kevin and Valkyrie quickly share pained grimaces before the latter speaks up."

        show kevin nope at twoleft
        show valkyrie neutral2 at tworight
        with fastDissolve

        ka "Hold on, before you go any further, yes, Kyrie is the light of my life, but it is entirely platonic please don't get the wrong idea!"
        show kevin hrm with fastDissolve
        ka "So many people do! {size=-10}It's a little upsetting...{/size}"

        show valkyrie thatbad with fastDissolve
        vl "Sorry if that sounded super hasty, we really needed to clear it up as soon as we could."
        vl "It's a bit silly what people assume, Kev's mum had the wrong idea for 3 years. Though it's a little funny looking back on it."
        show valkyrie tipq 
        show kevin neutral
        with fastDissolve
        vl "Oh, speaking of, are you two friends? You seem to get along well."

        np "I was taken aback for a moment. I've barely spoken this whole time, how did she come to a conclusion like {i}that{/i}?"

        show valkyrie neutral1 with fastDissolve

        pk "Honestly? We met like half an hour ago when she barged into my room, we've been teaming up to investigate the place but I wouldn't call us friends."
        np "Darya looked momentarily wounded before recovering her usual stance."

        show kevin aya with fastDissolve
        ka "We technically just bumped into each other as well, since our rooms were right next to each other."
        show kevin neutral with fastDissolve
        ka "It was pretty nice seeing a familiar face after waking up in a weird place."

        hide valkyrie with fastDissolve

        show darya yeah1 at tworight with fastDissolve
        dk "{piracow}Aye, the same be true for me and Phantom Magpie and now she be part of me loyal crew!{/piracow}"

        hide kevin with fastDissolve

        show valkyrie tipq2 at twoleft with fastDissolve
        vl "Wait hold on, Phantom Magpie? Like the 'robin hood style phantom thief' the news keeps talking about?"
        vl "I think I recognize your getup, now that I think about it."

        hide darya with fastDissolve

        show kevin yeep at tworight with fastDissolve
        ka "Yeah actually, I'm certain now, that's you isn't it?"

        show valkyrie heh with fastDissolve
        pk "Y-yeah, that's me."
        np "Still wish I hadn't dug my own grave by telling Darya earlier, there's no way for me to lie out of this anymore."

        ka "Woah, I never expected to meet you in the flesh, that's really neat!"

        np "I nervously side-eye Valkyrie the cyber-cop for a moment."

        show valkyrie tipq2 with fastDissolve
        vl "What's that look for?"

        pk "Just wondering if you'd have anything against me, given that you work in security and all..."

        show valkyrie heh 
        show kevin neutral
        with fastDissolve
        vl "Well, from what I've heard, you enjoy stealing from rich people right? I can get behind that."
        show valkyrie aaan with fastDissolve
        vl "You know why I work in a hospital? Cus I want to protect the vulnerable."
        show valkyrie thatbad with fastDissolve
        vl "If a hacker gets into the hospital network, they can shut off ventilators or hold life support systems hostage until the money is coughed up."
        show valkyrie neutral1 with fastDissolve
        vl "What you're doing? Love it."

        ka "I also think you're kinda cool actually."

        np "They've definitely misunderstood something somehow, but I'm going to let it slide. I'd rather I stay in their good books."

        show kevin sys with fastDissolve
        ka "Anyway, we should probably get back to checking out this infirmary."
        ka "I haven't finished looking through all the chemicals, and there's some pretty dangerous stuff in here."

        hide valkyrie with fastDissolve

        show darya yikes at twoleft with fastDissolve
        dk "It'll probably be a good idea to make an inventory of that, then. There's some people I don't quite trust here."

        show kevin sad with fastDissolve
        ka "Oh dear, I better get on that quickly, then!"
        show kevin neutral with fastDissolve
        ka "See ya for now!"

        show darya bois with fastDissolve
        dk "Farewell!"

        np "Me and Valkyrie quietly wave goodbye."

        hide darya
        hide kevin
        with fastDissolve

        $ asktotal += 1
        $ medbayread[0] = 1
        jump draw_medbay

    elif medbayread[0] == 1:
        np "The two of them are carefully looking through the cupboards while chatting, as Kevin seems to be checking out and arranging some of the chemicals."

        jump draw_medbay


#Corridor H1

screen corrH1:
    add "bg corrh1"

    imagebutton:
        xpos 856
        ypos 364

        focus_mask True

        auto "h1door %s"

        if flagA != 2:
            action Jump("draw_liftroom")
        else:
            action Jump("lockedH1door")

    imagebutton:
        xpos 1460
        ypos 830

        focus_mask True

        auto "right arrow2 %s"

        action Jump("draw_corrG2")

        if wiggle:
            at buttup2

    add "darkborder":
        blend "multiply"
        alpha 0.8

label draw_corrH1:
    if currentlocation != "corrH1":
        scene bg corrh1_full with fade
        $ currentlocation = "corrH1"
    elif currentlocation == "corrH1":
        scene bg corrh1_full

    call screen corrH1

label lockedH1door:

    if flagA == 2 and corrH1read[0] == 0:
        np "I try to open the door that the suspicious 'Exit {emoji}{color=aa0000}🤍{/color}{/emoji}' sign pointed to but find it locked."
        pk "Yeah that makes sense, didn't think it'd be that easy."
        np "But if I still had my lockpicks on me then this {i}would've{/i} been that easy."

        show darya yeah1 with dissolve2
        dk "Let me try."

        if corrDdoorread[0] == 1:
            pk "It didn't work out super well when you tried opening a blocked door earlier, though."
        else:
            pk "Not sure why you'd be able to when I couldn't."
        
        show darya hm with fastDissolve
        dk "It can't hurt to try..."

        np "No matter the force she used, the door stayed firmly shut."

        show darya hh with fastDissolve
        if corrDdoorread[0] == 1:
            dk "{size=-5}Maybe I should just start leaving sealed doors be...{/size}"
        else:
            dk "{size=-5}Yeah I should've just taken your word on it.{/size}"

        pk "At least you tried?"
        
        dk "Let's just keep looking around."

        pk "Oh, yeah sure."

        hide darya with dissolve2

        $ asktotal += 1

        $ corrH1read[0] = 1

        jump draw_corrH1
    elif flagA == 2 and corrH1read[0] == 1:
        np "Unfortunately there's no getting through here right now."

        jump draw_corrH1


#Corridor H2

screen corrH2:
    imagebutton:
        xpos 1500
        ypos 830

        focus_mask True

        auto "turnarrow %s"

        action Jump("draw_liftroom")

    imagebutton:
        xpos 750
        ypos 450

        focus_mask True

        auto "left arrow %s"

        action Jump("draw_corrG2")

label draw_corrH2:
    if currentlocation != "corrH2":
        scene bg corrh2 with fade
        $ currentlocation = "corrH2"
    elif currentlocation == "corrH2":
        scene bg corrh2

    call screen corrH2

#Lift Room

screen liftroom:
    imagebutton:
        xpos 1400
        ypos 880

        focus_mask True

        auto "turnarrow %s"

        action Jump("draw_corrH2")


label draw_liftroom:
    if currentlocation != "liftroom":
        scene bg liftroom with fade
        $ currentlocation = "liftroom"
    elif currentlocation == "liftroom":
        scene bg liftroom

    call screen liftroom


#============#
# STORY HOPS #
#============#

label daryaburstpandoraroom:
    scene bg pandora_full

    np "I think that's everything, there wasn't really anything helpful but at least I know a bit more about the situation."
    np "All of a sudden I hear footsteps outside, and then a rattling at the door."

    pk "Hello, who's-"

    play sound "audio/bang.wav"


    scene bg daryaatdoor with hpunch

    "{uk}Pirate!?{/uk}" "{piracow}{size=+20}AHOY!!!{/size}{/piracow}"

    pk "AAH!"
    pk "Who the hell are you!?"
    pk "And is that a {i}sword{/i}!??"

    dk "I'm Darya!"
    dk "{piracow}And foam it may be, 'tis real in me heart.{/piracow}"

    scene bg pandora_full with dissolve

    show darya neutral
    dk "{piracow}I be a pirate captain!{/piracow}"

    pk "Yeah, okay. I can... see that much."
    pk "But it doesn't help."
    pk "What are you doing here??"

    show darya yeah1 with fastDissolve
    dk "{piracow}I heard ye scrabbling around and had to know who else be here.{/piracow}"

    pk "Cool cool, next questions: where are we and can you drop the accent?"

    show darya hh with fastDissolve
    dk "{piracow}Arg, I know not where we be...{/piracow}"
    show darya anger with fastDissolve
    dk "{piracow}But the pirate stays, matey.{/piracow} I like it."

    np "Okay. Her dropping the pirate in the last sentence aside..."
    show darya neutral with fastDissolve
    pk "Hold on, let me process this for a second. Then we can start from the beginning."
    pk "So, who are you?"

    show darya yeah2 with fastDissolve
    dk "{piracow}I be Captain Darya Bateau, at yer service.{/piracow}"
    
    pk "That cannot be your real name! That's the french word for 'boat'!"

    show darya ohyeah with fastDissolve
    dk "{piracow}A true Captain be needing many aliases.{/piracow}"
    show darya neutral with fastDissolve
    dk "Anyhoo, {piracow}what be your name?{/piracow}"

    pk "I'm... Phantom Magpie."
    np "If you're using an alias, so am I. Don't really feel like telling some stranger my real name, Pandora, just yet anyway."

    show darya hm with fastDissolve
    dk "{piracow}Arg, ye name be familiar, where do I know ye from.{/piracow}"

    #np "Let's downplay this a little bit."
    pk "I uh, steal things...?"
    pk "You {i}might{/i} have seen me on the news?"

    show darya yeah1 with fastDissolve
    dk "{piracow}We be one and the same then. I'm a pirate and you be...{/piracow} whatever you are."

    pk "Well, I'm usually called a 'Phantom Thief', I think. Since I steal from rich people to help poorer folks."

    show darya neutral with fastDissolve
    dk "{piracow}That be a noble occupation, I suppose ye be in yer element here: the unknown and the dangerous.{/piracow}"

    np "I wouldn't really consider this 'in my element', I've literally been kidnapped."

    show darya ask1 with fastDissolve
    dk "To continue, {piracow}I saw other doors on me way in. Do you wish to join me crew and investigate?{/piracow}"

    np "Okay, so I don't trust this woman one bit."
    np "However..."
    np "I was planning on exploring outside of this room anyway. And having someone with me might make it easier... and safer."
    pk "Yeah sure, I'll tag along."
    hide darya with dissolve2

    np "She's insane."
    np "God I hope anyone else we stumble onto is more normal."

    ht "Having other people in the room can sometimes bring up different dialogue as they may notice things that Pandora doesn't."
    ht "Clicking on the door will bring up the option to leave."

    $ daryaroom = True

    jump draw_pandora_room

label allintroviewed:
    np "After checking out every room, I decided it was probably best to head back to the dorms to recuperate."
    pk "Since we've been everywhere now, I'm going to head back to my room for a bit."

    show darya neutral with dissolve2
    dk "Oh, I'll head back with you."
    show darya hm with fastDissolve
    dk "{size=-10}It's safer if we stick together...{/size}"

    np "..."

    scene black with dissolve

    np "We make our way back to the dorms... together."

    scene bg corrc1_full with dissolve

    np "However, there was a surprise waiting for us when we returned."

    show dexter ack with dissolve2
    "{uk}Man in Sunglasses{/uk}" "Ack!"
    show dexter eek with fastDissolve
    "{uk}Man in Sunglasses{/uk}" "Um, hello- hi- uh-"
    show dexter notgood2 with fastDissolve
    "{uk}Man in Sunglasses{/uk}" "Wait, no- bye!"
    hide dexter with dissolve2

    np "Before we had any time to process him, the jittery man scuttled into the room with the lizard on the door."
    np "Me and Darya shared a puzzled look, but after only a few seconds he re-emerged with a new visage."
    
    show dexter yeahh with dissolve2
    "{uk}Man in Sunglasses{/uk}" "Hi. How's it going?"
    hide dexter with fastDissolve

    show dexter ohyeah at tworight
    show darya ask2 at twoleft
    with fastDissolve

    dk "Um..."

    pk "Are you alright? You seemed pretty shaken just a moment ago."

    show darya neutral 
    show dexter strained
    with fastDissolve

    "{uk}Man in Sunglasses{/uk}" "Oh, absolutely. I'm swell, just- just wasn't expecting to run into anyone."
    "{uk}Man in Sunglasses{/uk}" "Anyway, hi, what'cha been up to? Everything all good?"
    show dexter notgood with fastDissolve
    "{uk}Man in Sunglasses{/uk}" "Wait, hold on, I mean, what are you two called?"
    show dexter fguns with fastDissolve
    ds "I'm Dexter, but for you, it's Dex."
    show dexter neutral with fastDissolve

    pk "Call me Magpie."

    show darya yeah1 with fastDissolve
    dk "Nice to meet you, Dexter, I'm Darya."

    show dexter question with fastDissolve
    ds "The same to you Capt'n. Oh, and, um, what's up with your getup? ...and the, uh, sword?"

    show darya ohyeah 
    show dexter ng2
    with fastDissolve
    dk "{piracow}Ye be correct in calling me captain, have a licence with me name on it, after all.{/piracow}"
    dk "'Darya Vene, Captain of the mighty vessel, the Dragonflight!'"
    show darya bois with fastDissolve
    dk "{piracow}Though ye need not worry about the blade, 'tis only foam.{/piracow}"

    show dexter hmmnss with fastDissolve
    ds "That's cool actually! I- I can- It's not quite the same, but I have a pilot's licence, I can fly pretty well, used to operate commercial airlines."

    show darya yeah1 with fastDissolve
    dk "{piracow}Aye, I be the same, my ship has a mighty legacy and carried passengers many across the Bristol Channel.{/piracow}"
    show darya yeah2 with fastDissolve
    dk "The freedom of the ocean, the feeling of the wind in my hair and the waves beneath the deck, it's unparalleled."
    show darya neutral with fastDissolve

    np "Ohh! Her boat is a ferry! Doesn't quite live up to the vibe she exudes."

    show dexter ng2 with fastDissolve
    ds "Yeah, it was- it was nice being in the sky..."
    show dexter cris with fastDissolve
    ds "{size=-10}Though for the last 5 years I...{/size}"

    show darya hm with fastDissolve
    dk "What was that last bit?"

    show dexter strained with fastDissolve
    ds "Just. Mumbling to myself...!"
    ds "Aaaanyway, you caught me just heading back to my room-"

    np "Despite clearly never having left the dorms, he begins a stiff turn back to his room."

    stop music fadeout 1.5

    np "However, the speakers flared to life as a cold, metallic, yet distinctly {i}human-like{/i}, voice rang out, interrupting any thoughts we might have had."

    hide darya
    hide dexter 
    with dissolve2

    "{uk}Voice Over Speakers{/uk}" "Apologies for the inconvenience, the problems causing an issue with my delay in appearance have just been rectified."
    "{uk}Voice Over Speakers{/uk}" "The door labelled 'exit' has just been unlocked, I would like all of you to come join me here."
    "{uk}Voice Over Speakers{/uk}" "And I do mean {b}every one of you.{/b}"

    np "The speakers crackled as they powered down, leaving us to ruminate in silence what we'd just heard."

    show darya sad at twoleft
    show dexter eek at tworight
    with dissolve2

    play music "audio/threat.mp3" fadein 1.0

    dk "What- what. Is something terrible happening after all?"

    show dexter aaaa with fastDissolve
    ds "Aah-aha! Oh no..."
    hide dexter with dissolve

    pk "We... We should go, right?"

    dk "A-aye. Probably in our best interests."

    np "We turned to go ask Dexter if he was coming with us, only to see him pressed against the wall, curled into himself and breathing raggedly."

    show dexter aaaa at tworight with dissolve

    ds "No- no- this has to be them- they found me. They found me... Ahaa..."

    pk "Oh god, you're really not alright, are you?"

    ds "Not again, I- I can't go through that again..."

    np "He was desperately holding back sobs."

    show darya worry with fastDissolve
    dk "We should probably try and bring him with us, that speaker voice said {i}everyone{/i} needed to come."
    dk "I really don't want to upset whoever's on the other end of it."

    stop music fadeout 1.5

    np "I reach out to Dexter, about to nudge him. But Florus then opened his door and stepped out."

    hide darya
    hide dexter 
    with fastDissolve

    show florus neutral with fastDissolve

    play music "audio/wandering.mp3" fadein 1.0

    fc "Oh. Heya. I suppose we heed the call?"
    hide florus with dissolve2

    show darya hm at twoleft
    show florus neutral at tworight
    with dissolve2

    dk "Dexter here isn't having a good time of it, so we're trying to get him to come with us."

    show florus blerg with fastDissolve
    fc "Well, if he doesn't want to go it's his prerogative..."
    show florus ey with fastDissolve
    fc "I'll tag along if you're heading over there, though."

    show darya yeah1 with fastDissolve
    dk "The more the merrier."

    np "As if an ironic response from the universe, Emilio turned the corner at that exact moment."

    hide darya
    hide florus 
    with fastDissolve

    show emilio welcome with fastDissolve
    eb "{piracow}Howdy folks! Quite a gathering we have here, ain't it-{/piracow}"
    show emilio grumpy with fastDissolve
    eb "..."

    hide emilio with fastDissolve

    show emilio grumpy at tworight
    show darya grumpy at twoleft
    with fastDissolve

    np "The air grows somehow tenser, as he and Darya lock eyes."

    dk "{piracow}We meet again, foul wretch.{/piracow}"

    eb "{piracow}I see ya're still sneakin' about, corruptin' our fair companions.{/piracow}"

    pk "This is seriously not the time, did you not hear the creepy voice or what?"

    show emilio neutral with fastDissolve
    eb "{piracow}I humbly apo-{/piracow} I mean, you're right."
    show emilio spin with fastDissolve
    eb "We can put our differences aside for a moment, {i}can't we{/i}?"

    dk "Hmm... Sure..."
    show darya yikes with fastDissolve
    dk "But only because it's probably safer."

    pk "*sigh* Glad we resolved that. Let's go."

    hide darya
    hide emilio 
    with dissolve2

    np "Thankfully Dexter had calmed down a little, and he followed closely behind us, fidgeting, as we made our way to the formerly locked door."

    stop music fadeout 1.5

    scene bg liftroom_full with fade

    play music "audio/lonely room.mp3" fadein 1.0

    np "Several people had made it there beforehand."

    show assbot neutral at twoleft
    show assbot neutral at tworight as assbot2
    with dissolve2

    np "A dozen or so large robots, roughly 6 and a half feet tall, stood against the walls."
    np "But more pressing was the blue painted one standing in front of the lift."

    hide assbot
    hide assbot2
    with fastDissolve

    show maizey neutral with dissolve2
    "{uk}Large Robot{/uk}" "Five more, that makes thirteen. Not quite everyone."
    hide maizey with dissolve2

    show nin oof with dissolve2
    nt "You're dead silent aside from when you're counting people who come in."
    nt "What's your goal here?"

    hide nin with fastDissolve

    show nin oof at tworight
    show carwyn ha at twoleft
    with fastDissolve

    cm "Find bliss in the fiend's silence."

    show nin uncomf with fastDissolve
    nt "Ugh."

    hide nin with dissolve2

    show nikolas eugh at tworight with fastDissolve
    nl "Can you at least {i}try{/i} to speak normally please."

    hide carwyn with dissolve2

    show ratna ehm at twoleft with fastDissolve
    rh "Maybe best not antagonise him."

    show nikolas hehn with fastDissolve
    nl "Yeah, he might write an angry sonnet about me."

    show ratna ha2 with fastDissolve

    np "They both snicker."

    hide ratna
    hide nikolas 
    with dissolve2

    show belinda letsee at twoleft
    show osanne neutral at tworight
    with fastDissolve

    bl "Um, any thoughts on that thing? You seem to know a lot about... magic."

    show osanne blung with fastDissolve
    of "That mechanical beast means nothing to me."

    show belinda ehg with fastDissolve
    bl "Hmm, I was hoping it would be something more interesting."

    hide belinda
    hide osanne 
    with dissolve2

    show valkyrie ehq at twoleft
    show kevin hrm at tworight
    with fastDissolve

    ka "Nothing seems to be happening, maybe we should head back out?"

    show valkyrie thatbad with fastDissolve
    vl "I'm not sure that's an option with that strange robot watching us..."

    hide valkyrie
    hide kevin 
    with dissolve2

    show maizey angry with fastDissolve
    "{uk}Large Robot{/uk}" "We have waited long enough, where are the others? The remaining two humans, I mean, that horse needn't come."

    pk "Huh?"

    "{uk}Large Robot{/uk}" "As per my last request, {b}everyone{/b} must be present."
    "{uk}Large Robot{/uk}" "Can Ainsley and Fabrice please make their way to the room marked 'exit'."

    np "At that moment I realised that everything it had said was still coming from over the speakers at the back of the room and not the robot itself."

    hide maizey with dissolve2

    np "Silence draped us under the robot's frightful glare."
    np "A short while later, two more people - a short, muscular woman with a bow, and a tall man in a dress - crept through the door."

    show ainsley neutral at twoleft
    show fabrice neutral at tworight
    with dissolve2

    "{uk}Both{/uk}" "..."

    hide ainsley
    hide fabrice 
    with dissolve2

    show maizey neutral with fastDissolve
    "{uk}Large Robot{/uk}" "It would be impertinent of you to refuse an introduction, please state your names to the group."
    hide maizey with dissolve2

    show ainsley neutral at twoleft
    show fabrice neutral at tworight
    with fastDissolve

    "{uk}Both{/uk}" "..."

    show ainsley sigh with fastDissolve
    "{uk}Archer{/uk}" "I'll go first."
    show ainsley hwa with fastDissolve
    av "I'm sure you just heard, but it's Ainsley."

    hide fabrice with dissolve2

    show ratna shock at tworight with fastDissolve
    rh "Hold on! It's you! From the forest!"

    show ainsley oh with fastDissolve
    av "Wait yeah, you were there right before-"

    hide ratna
    hide ainsley
    with dissolve2

    show maizey angry with fastDissolve
    mm "Hey! I gave you time for introductions, not chatter."

    np "The two quickly quietened down."

    hide maizey with dissolve2

    show ainsley neutral at twoleft
    show fabrice neutral at tworight
    with fastDissolve

    "{uk}Man in Flower Dress{/uk}" "..."

    show fabrice ack with fastDissolve
    ff "Hi... I'm Fabrice..."

    show ainsley sigh with fastDissolve
    av "More importantly, and while I'm here, why did you take my arrows yet leave me my bow?"
    av "Since I'm not allowed to talk to the others I assume I'm at least allowed to ask questions."

    hide ainsley
    hide fabrice 
    with dissolve2

    show maizey exp with fastDissolve
    "{uk}Large Robot{/uk}" "The arrows were confiscated as they are sharp and could cause serious undue harm to your bunkmates."
    show maizey neutral with fastDissolve
    "{uk}Large Robot{/uk}" "You were left the bow as it is known to be important to you."
    hide maizey with dissolve2

    show ainsley really with fastDissolve
    av "Hm."
    hide ainsley with dissolve2

    pk "Hey Fabrice, are those cat ears?"
    np "There's already two Manifests here, it wouldn't be too weird if there was a third, right?"

    show fabrice pensive with fastDissolve
    ff "... It's a headband..."

    pk "Oh, okay."

    hide fabrice with dissolve2

    show maizey neutral with fastDissolve
    "{uk}Large Robot{/uk}" "Now that each of you have given your names, it is my turn."
    mm "You may address me as 'Maizey'."

    np "Ah, so she {i}is{/i} meant to look like the same cereal mascot I saw doodled in my room."
    np "Wait a second-"
    pk "Hey, why are you painted to look like a cereal mascot?"

    show maizey exp with fastDissolve
    mm "I was in need of an avatar to speak to you through as I am not personally going to enter the bunker. And this design seemed recognisable, appropriate, and easy to paint."

    $ clues_text[5].append("It seems as though the avatar for our kidnapper(s?) is painted to look like Maizey, and I guess they decided to introduce themself(selves?) through this doodle.")
    $ clues[5] = "Doodle of Bunker Manager"
    "Notes on 'Doodle of Cereal Mascot' have been updated, and renamed to 'Doodle of Bunker Manager'."

    show maizey neutral with fastDissolve
    mm "And now that the pleasantries are over, I can inform you that your room keys are ready for collection."
    show maizey smug2 with fastDissolve
    mm "Management has been made aware of the delay, but will not apologise."
    show maizey neutral with fastDissolve
    mm "The keys will be labelled with your name, and should have a keychain of your animal attached."
    show maizey exp with fastDissolve
    mm "If you are unsure what yours is, it will match the symbol on your door."
    show maizey neutral with fastDissolve
    mm "Management has also provided a set of electronic notepads, which will come with a set of profiles of each of you, and a note taking app."
    mm "It does not matter which one you take, they are not personalised; however please only take one."
    hide maizey with dissolve2

    np "Another robot from the edge of the room makes it's way to the centre and stands there, holding a box of what I can only assume are the notepads and keys."
    #$ testclue.append("MMM")
    np "There's a few seconds of still silence and exchanged hesistant glances before people begin to gingerly make their way over to the box."
    np "I stand back and wait for the crowd to die down before going to get my own."
    np "As expected, the key with my name on is attached to a keychain shaped like a bird. If this is a pattern then 'Management' might know more than they should."

    $ clues_text[1].append("Apparently there was a managerial delay on us getting our room keys, and each of them seem to have a silhouette keychain of an animal on them that may be related to Manifests somehow given that mine looks kinda like a magpie. These same silhouettes were also present drawn on the front of the doors in the dorms.")
    "Notes on 'Bedroom Door' have been updated."

    np "I pull up my profile as I head back to the edge of the room, curious as to what information they might have on me."

    $ profileselect = 12
    $ allowedP = False
    $ quick_menu = False
    window hide dissolve
    show screen profiles with dissolve

    pause 1.5

    window auto

    np "Despite their showmanship, there's surprisingly little information on here. They don't even have my real name."
    np "My Manifest is correctly identified, but that's not really impressive given that I pretty much publicly flaunt that on TV."
    np "More importantly, I hope they at least have Darya's full name because I really want to know what it actually is after all the stupidity she's put me through."

    $ profileselect = 3
    window hide dissolve
    show screen profiles with dissolve

    pause 1.5

    window auto

    np "It takes a single glance to realise their lack of information on me might be a fluke."
    np "I'll have a look at the other profiles in a moment, but right now there's something more pressing."

    hide screen profiles with dissolve
    $ quick_menu = True

    pk "Hey, Darya."

    show darya hm with dissolve2
    dk "Huh, yeah?"

    pk "Look at this a second."
    np "I hold up my tablet with her profile visible."

    show darya ask2 with fastDissolve
    dk "Wh-"

    pk "This is the single most pirate-y name I've seen in my life! Why the hell were you introducing yourself like that earlier?"
    pk "'Darya Kidwell', you might as well be called 'Blackbeard'!"

    show darya hh with fastDissolve
    dk "{piracow}A-argh, well-{/piracow}... {size=-10}It's... personal information{/size}"

    pk "Then why pick some of the worst aliases anyone's ever heard in their life?"

    show darya worry with fastDissolve
    dk "{size=-5}I thought they sounded cool...{/size}"

    np "As much as the LARPing bugs me, with this, maybe she was born for it."
    pk "Look, your real name sounds cool as well, if it was me, I'd lean into it."

    hide darya with dissolve2

    np "I turn and leave a befuddled Darya behind, deciding to have a look at some of the other profiles."

    $ profileselect = 11
    $ allowedP = False
    $ quick_menu = False
    window hide dissolve
    show screen profiles with dissolve

    pause 1.5

    window auto

    np "Despite everything, I'm glad for her that these people at least seem to respect her botany prowess enough to note it down."

    $ profileselect = 4
    window hide dissolve
    show screen profiles with dissolve

    pause 1.5

    window auto

    np "It is a shame that these are generally pretty bare-bones though."
    np "There isn't any extra info on what he mentioned earlier."
    np "Though it is interesting to note that only me and Osanne seem to have proper details on our Manifests."

    $ profileselect = 1
    window hide dissolve
    show screen profiles with dissolve

    pause 1.5

    window auto

    np "Is this picture of her the only one they could get? If I recall what she said earlier, this might be security footage from when she stole Luna and Sol."

    $ profileselect = 5
    window hide dissolve
    show screen profiles with dissolve

    pause 1.5

    window auto

    np "Oh this must be that previous horse he mentioned, it's got markings that Dakota doesn't."
    np "Plus Emilio himself looks a lot younger here, I'd place him at about 15?"

    $ profileselect = 13
    window hide dissolve
    show screen profiles with dissolve

    pause 1.5

    window auto

    np "There's probably nothing of value to be gleamed from these right now, so I'll shelve looking at more until later."

    hide screen profiles with dissolve
    $ allowedP = True
    $ quick_menu = True
    $ pactive = True

    show nin uncomf with dissolve2
    nt "Excuse me? How the hell do you have all this information about us?"
    hide nin with fastDissolve
    show nin uncomf at twoleft with fastDissolve

    show belinda letsee at tworight with fastDissolve
    bl "More importantly, how did you get these pictures of us? I'm not sure how anyone other than Eclipse should have the security footage this was taken from."

    hide nin with dissolve2

    show valkyrie ehq at twoleft with fastDissolve
    vl "Well, you'd be surprised how easy it can be to get a hold of CCTV footage with the right hacking infrastructure."
    show valkyrie thatbad with fastDissolve
    vl "... Or the right connections."
    show valkyrie bleh with fastDissolve
    vl "And some of these seem to be taken from the internet or newspapers, which for sure wouldn't be hard for a large company to get their hands on."

    hide belinda with dissolve2

    show ratna ehm at tworight with fastDissolve
    rh "Oh yeah, some of us are technically public figures cus of our work. In that case our details wouldn't be that hard to find."

    hide ratna
    hide valkyrie 
    with fastDissolve

    np "The room grew into a cacophony of discussion as everyone called out theories, blending all their words together indecipherably."
    np "Amongst the chaos, I noticed that Dexter, standing nearby, seemed to be panicking badly."

    show dexter aaaa with dissolve2
    ds "Oh no, no nono... I was right, it {i}is{/i} them. Ngaaa...."
    hide dexter with dissolve2

    show belinda ohnono with dissolve2
    bl "Wait, hold on-"
    hide belinda with fastDissolve
    
    np "Despite not being very close to us, Belinda somehow noticed Dexter and quickly made her way over."

    show dexter cris at twoleft
    show belinda sadsmile at tworight 
    with fastDissolve

    ds "Wha-"

    bl "Hey there um, Dexter, right? Are you feeling alright? I noticed th-"

    hide dexter
    hide belinda
    with fastDissolve

    show maizey neutral with dissolve2
    mm "Now that you have all received your keys and tablets it is time for me to continue my explanation."

    np "The sound of Maizey's voice once more echoes silence amongst the rest of us."

    mm "Firstly, onto the reasons why you have been taken to this bunker."
    show maizey exp with fastDissolve
    mm "One of those reasons is that we need a sample group to demonstrate some, let's say, products that our sponsors need subjects for."
    mm "Every couple of weeks during your time here, one of our lovely sponsors will provide us a product for you to test."
    hide maizey with fastDissolve

    show carwyn angy with dissolve2
    cm "Would you care to disclose any of the applicable particulars regarding the systems you shall be subjecting us to?"
    hide carwyn with dissolve2

    show maizey neutral with fastDissolve
    mm "You will not be told any of the products in advance, as preparation may bias you to the testing."
    hide maizey with fastDissolve

    show nin uncomf with dissolve2
    nt "Did you really need to kidnap us f-"
    hide nin with fastDissolve

    show nin uncomf at twoleft
    show nikolas eugh2 at tworight
    with fastDissolve

    nl "There's so many people out there willing do stuff like this, {i}voluntarily!{/i}"

    hide nin with fastDissolve

    show ratna ehm at twoleft with dissolve2
    rh "Agreed, I don't yet see why this was all necessary - bit of a big show for some product testing, yeah?"

    hide nikolas with fastDissolve

    show ainsley sigh at tworight with dissolve2
    av "More importantly than that, I was wondering how we would be acquiring food in this situation."

    hide ratna
    hide ainsley
    with fastDissolve

    show maizey neutral with dissolve2 
    mm "Manag-"
    hide maizey with fastDissolve

    show florus confused with dissolve2
    fc "Oh yeah, what about water? Are we connected to a pipe network?"
    hide florus with fastDissolve

    show maizey exp with dissolve2 
    mm "Management has-"
    hide maizey with fastDissolve
    
    show kevin sad2 with dissolve2
    ka "Wait what about prescription medications? I uh-"
    hide kevin with fastDissolve

    show kevin sad2 at twoleft
    show fabrice ack at tworight
    with fastDissolve

    ff "Yeah, I... woke up without my inhaler... so..."

    hide kevin
    hide fabrice
    with fastDissolve

    show maizey upset with dissolve2 
    mm "Listen to m-"
    hide maizey with fastDissolve

    show emilio despair with dissolve2
    eb "Hang on, what about our families? Are any of them-"
    hide emilio with fastDissolve

    show maizey peeved with hpunch 
    stop music
    mm "{size=+20}As I have been {b}trying{/B} to say.{/size}"
    show maizey angry with fastDissolve
    mm "Management has everything handled. Stop asking questions at this time."
    mm "I had not yet finished speaking."
    show maizey exp with fastDissolve
    play music "audio/threat.mp3" fadein 6.0
    mm "As well as the sponsorships, I have been instructed to inform you about the fact that you will be, ah, 'participating in a death game' for the duration of your stay."
    show maizey neutral with fastDissolve

    pk "What!?"
    np "My voice escaped me and I quickly put a hand to my mouth as the rest of the room erupted similar cries of shock."

    mm "The detailed rules for this 'game' will be elaborated on later, for now I will advise that the death of your bunkmates will be {b}mandatory{/b} for prolonged survival."
    show maizey exp with fastDissolve
    mm "The bunker will be made inhospitable, and only through a murderous death shall the affliction be alleviated."
    mm "And if the rest of you wish to also prove your will to survive, you must find the one who did it to obtain a more permament reprieve."
    mm "However, I also will add that at this moment Management has not yet declared any method of 'escape' or way of leaving this bunker, unless you wish to attempt to find one yourselves."
    show maizey smug2 with fastDissolve
    mm "Though I am assured that you will find no such thing."
    mm "This lift behind me may be called the 'exit', but I can guarantee that it goes to nowhere."
    hide maizey with fastDissolve

    show nin oof with dissolve2
    nt "What do you mean? {i}Why{/i} can't you elaborate now? It's important to the cohesion of the group that we have all the information we need."
    hide nin with fastDissolve

    show nin oof at twoleft
    show emilio bad at tworight
    with dissolve2

    eb "How dare you try and force such a thing upon us."

    hide nin
    hide emilio
    with fastDissolve

    show ratna droopy at twoleft
    show nikolas eugh2 at tworight
    with dissolve2

    rh "Oh no this {i}really{/i} isn't good..."

    nl "What the hell!?"

    hide ratna
    hide nikolas
    with fastDissolve

    show osanne terror at twoleft
    show florus flinch at tworight
    with dissolve2

    fc "Uhh, uhhh-"

    of "{size=-10}WHAT!{/size}"

    hide osanne
    hide florus
    with fastDissolve

    show valkyrie thatbad at twoleft
    show kevin sad at tworight
    with dissolve2

    vl "Honestly I probably should've expected something like this."

    show kevin sad3 with fastDissolve
    ka "Huh? This is awful! How could you have thought something like this would happen?"

    vl "Call it pessimism born from being kidnapped."

    hide valkyrie
    hide kevin
    with fastDissolve

    show ainsley bad at twoleft
    show fabrice ack at tworight
    with dissolve2

    av "... I don't think there's anything hopeful that can proceed a statement like that..."

    ff "Ah, uh, oh no, this isn't..."

    hide ainsley
    hide fabrice
    with fastDissolve

    np "The panicked shouting once more blended together as I tried to stifle my own outcry."
    np "Amidst it all Belinda had stayed calm. She patted a paralyzed Dexter on the shoulder, took a step away from him, then cleared her throat and began to address the group."

    stop music fadeout 2.0

    show belinda sadsmile with dissolve2 #she needs another one here (like nin still needs a few more aswell)
    bl "Listen, everyone, I understand that what we've just heard is frankly, terrifying, and you're understandably shaken."

    play music "audio/Haunting Haze.mp3" fadein 1.0

    bl "Most of you barely know anyone here, and trust will be hard to come by. However, the last thing we need right now is to see one another as enemies."
    show belinda neutral with fastDissolve
    bl "It's important that we temper our fears before they get the better of us, so take a deep breath in, steady yourself-"

    hide belinda with fastDissolve

    show belinda strained at twoleft
    show nin uncomf at tworight
    with dissolve2

    nt "I understand what you're trying to do, but empty words aren't going to give us an action plan or solve anything."

    hide nin with fastDissolve

    show carwyn ango at tworight with dissolve2
    cm "I refuse to stand idly and 'steady' my emotions in the face of such a foul force that dares to defile the preciousness of the sanctity of life."

    show belinda ohno with fastDissolve

    cm "An acute insult to challenge our rights to exist upon this plane in such a flagrant display of heinous sin."

    hide carwyn
    hide belinda
    with fastDissolve

    show darya threat with dissolve2
    dk "{piracow}Listen t' me ye foul beast.{/piracow}"
    hide darya with fastDissolve

    np "Darya, who'd somehow been quiet until this moment, pointed the tip of her sword directly at Maizey, who was stood stock still."

    stop music fadeout 1.0
    scene black with dissolve

    show screen keyscr
    $ renpy.movie_cutscene("images/darya_attack.ogv")
    hide screen keyscr

    scene black with dissolve

    #fade into darya body CG here
    scene bg daryafuckingdies with dissolve

    $ statuses[3] = "Unknown"

    np "Panic wracks my body. {i}Is-{/i}"
    np "{i}Is she dead?{/i}"

    #show maizey neutral with dissolve2
    mm "There is one thing I failed to mention prior."
    mm "In each of your left arms we have implanted a device. At my or Management's will the device shall trigger."
    mm "Body wracked with pain, consciousness will fail you."
    mm "As the device is so carefully wrapped around an artery, repeated use could easily prove fatal."
    mm "Since disturbance to the device can also inadvertently trigger it, it is in your best interests to comply."
    #hide maizey with dissolve2

    scene black with dissolve

    np "All eyes were transfixed on Darya's body as Maizey finished her explanation."
    np "I could feel the dread set in as both the air and pit in my gut became heavy."
    np "I couldn't see a way out of this monster's grasp, it was a game of survival and nothing more."
    np "Every person in this room was now a potential enemy, and yet..."
    np "If I wanted to survive I couldn't afford to make any."
    np "Only the future could tell what horrors awaited us when the 'game' began."

    scene black with fastDissolve
    $ quick_menu = False
    "END OF PROLOGUE/ ALPHA/ DEMO"


ht "Game will close if you progress past this text box." #failsafe so i dont close the game by accident while testing cutscenes that sit on the script precipice

# This ends the game.

return
