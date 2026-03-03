
# =======================
# == CUSTOM TRANSFORMS ==
# =======================

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


define fastDissolve = Dissolve(0.3) #very fast fade effect
define dissolve2 = Dissolve(0.6) #medium fast fade effect
define FD2 = { "master" : Dissolve(0.2) } #used to change character sprites mid line

define flashbulb = Fade(0.2, 0.0, 0.4, color='#dddddd')