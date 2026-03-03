# == TRANSFORMS ==

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

# == TRANSITIONS ==

# Dissolves
define dissolve_fast = Dissolve(0.3) 
define dissolve_medium = Dissolve(0.6)
# This can be used to change a characters sprite while they are speaking 
define dissolve_midline = { "master" : Dissolve(0.2) }

define flashbulb = Fade(0.2, 0.0, 0.4, color='#dddddd')