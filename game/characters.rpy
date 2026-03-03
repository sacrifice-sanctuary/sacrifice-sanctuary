# CHARACTERS
# Callbacks for character voicing
# Constants used for character colours
# Character definitions

# Voice Callback Functions

default bleep = True

define PHFile = "beep1.ogg"

init python: 

    renpy.music.register_channel("Bleep", mixer="voice", tight=True, buffer_queue=True) #setting up the voice bleeps to play on a new channel that uses the pre-built 'voice' volume slider

    def beepVoice(event, interact=True, SFile="beep1.ogg", Char="", **kwargs): #for characters who have a set of 3 randomised beep sounds for their voice
        if not interact:
            return

        if event == "show":
            beep = 0
            while beep < 100:
                SFile = Char + "_" + str(renpy.random.randint(1,3)) + ".ogg"
                renpy.music.queue(SFile, channel="Bleep", loop=False)
                beep += 1
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="Bleep", fadeout=0.4)


    def singleCall(event, interact=True, SFile="beep1.ogg", **kwargs): #for characters who make a single noise as their entire line (eg horse neigh)
        if not interact:
            return

        if event == "show":
            renpy.music.queue(SFile, channel="Bleep", loop=False)


    def narratorCall(event, interact=True, **kwargs): #for characters who use a single beep sound for their voice
        if not interact:
            return

        if event == "show":
            renpy.music.queue("beep1.ogg", channel="Bleep", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="Bleep", fadeout=0.4)

# RBG Colours for each team
RED = "22B14C"
ORANGE = "FF7F27"
GREEN = "22B14C"
BLUE = "00A2E8"
PURPLE  = "A349A4"

# Outline width in pixels
WHO_OUTLINE_WIDTH = 2
WHAT_OUTLINE_WIDTH = 1

# Outline is a tuple of size, colour, x offset, y offset
RED_NAME_OUTLINE = [(WHO_OUTLINE_WIDTH, "B1171D", 0, 0)]
ORANGE_NAME_OUTLINE = [(WHO_OUTLINE_WIDTH, "C4621F", 0, 0)]
GREEN_NAME_OUTLINE = [(WHO_OUTLINE_WIDTH, "188638", 0, 0)]
BLUE_NAME_OUTLINE = [(WHO_OUTLINE_WIDTH, "0284BC", 0, 0)]
PURPLE_NAME_OUTLINE = [(WHO_OUTLINE_WIDTH, "783678", 0, 0)]

RED_TEXT_OUTLINE = [(WHAT_OUTLINE_WIDTH, "6C4D4E", 0, 0)]
ORANGE_TEXT_OUTLINE = [(WHAT_OUTLINE_WIDTH, "7A6659", 0, 0)]
GREEN_TEXT_OUTLINE = [(WHAT_OUTLINE_WIDTH, "506C58", 0, 0)]
BLUE_TEXT_OUTLINE = [(WHAT_OUTLINE_WIDTH, "5B707B", 0, 0)]
PURPLE_TEXT_OUTLINE  = [(WHAT_OUTLINE_WIDTH, "725872", 0, 0)]

define ht = Character("System", color="3366FF", who_outlines=[(2, "02648C", 0, 0)], what_outlines=[(1, "5B707B", 0, 0)], callback=narratorCall) # red=ED1C24, green=22B14C, purple=A349A4, orange=FF7F27, blue=00A2E8
define uk = DynamicCharacter('UKName', color="666666", who_outlines=[(2, "333333", 0, 0)], what_outlines=[(1, "777777", 0, 0)], callback=beepVoice, cb_Sfile=PHFile, cb_Char="pandora")
define np = Character("Pandora", color="2092C8", who_outlines=[(2, "0284BC", 0, 0)], what_color="0784B9", what_outlines=[(1, "02648C", 0, 0)], alt="Pandora thoughts")

# BLUE TEAM
define pk = Character("Pandora", color="00A2E8", who_outlines=BLUE_NAME_OUTLINE, what_outlines=BLUE_TEXT_OUTLINE, callback=beepVoice, cb_Char="pandora") # blue
define dk = Character("Darya", color="00A2E8", who_outlines=BLUE_NAME_OUTLINE, what_outlines=BLUE_TEXT_OUTLINE, callback=beepVoice, cb_Char="darya")
define eb = Character("Emilio", color="00A2E8", who_outlines=BLUE_NAME_OUTLINE, what_outlines=BLUE_TEXT_OUTLINE, callback=beepVoice, cb_Char="emilio")
define fc = Character("Florus", color="00A2E8", who_outlines=BLUE_NAME_OUTLINE, what_outlines=BLUE_TEXT_OUTLINE, callback=beepVoice, cb_Char="florus")

# GREEN TEAM
define bl = Character("Belinda", color="22B14C", who_outlines=GREEN_NAME_OUTLINE, what_outlines=GREEN_TEXT_OUTLINE, callback=beepVoice, cb_Char="belinda") # green
define ds = Character("Dexter", color="22B14C", who_outlines=GREEN_NAME_OUTLINE, what_outlines=GREEN_TEXT_OUTLINE, callback=beepVoice, cb_Char="dexter")
define av = Character("Ainsley", color="22B14C", who_outlines=GREEN_NAME_OUTLINE, what_outlines=GREEN_TEXT_OUTLINE, callback=beepVoice, cb_Char="ainsley")

# RED TEAM
define rh = Character("Ratna", color="ED1C24", who_outlines=RED_NAME_OUTLINE, what_outlines=RED_TEXT_OUTLINE, callback=beepVoice, cb_Char="ratna") # red
define nl = Character("Nikolas", color="ED1C24", who_outlines=RED_NAME_OUTLINE, what_outlines=RED_TEXT_OUTLINE, callback=beepVoice, cb_Char="nikolas")
define ff = Character("Fabrice", color ="ED1C24", who_outlines=RED_NAME_OUTLINE, what_outlines=RED_TEXT_OUTLINE, callback=beepVoice, cb_Char="fabrice")

# PURPLE TEAM
define of = Character("Osanne", color="A349A4", who_outlines=PURPLE_NAME_OUTLINE, what_outlines=PURPLE_TEXT_OUTLINE, callback=beepVoice, cb_Char="osanne") # purple
define ka = Character("Kevin", color="A349A4", who_outlines=PURPLE_NAME_OUTLINE, what_outlines=PURPLE_TEXT_OUTLINE, callback=beepVoice, cb_Char="kevin")
define vl = Character("Valkyrie", color="A349A4", who_outlines=PURPLE_NAME_OUTLINE, what_outlines=PURPLE_TEXT_OUTLINE, callback=beepVoice, cb_Char="valkyrie")

# ORANGE TEAM
define cm = Character("Carwyn", color="FF7F27", who_outlines=ORANGE_NAME_OUTLINE, what_outlines=ORANGE_TEXT_OUTLINE, callback=beepVoice, cb_Char="carwyn") #orange
define nt = Character("Nin", color="FF7F27", who_outlines=ORANGE_NAME_OUTLINE, what_outlines=ORANGE_TEXT_OUTLINE, callback=beepVoice, cb_Char="nin")
define dh = Character("Dakota", color="FF7F27", who_outlines=ORANGE_NAME_OUTLINE, what_outlines=ORANGE_TEXT_OUTLINE, callback=singleCall, cb_SFile="neigh.mp3")

define mm = Character("Maizey", color="7A4C0E", who_outlines=[(WHO_OUTLINE_WIDTH, "523309", 0, 0)], what_outlines=[(WHAT_OUTLINE_WIDTH, "52493E", 0, 0)], callback=beepVoice, cb_Char="maizey")
