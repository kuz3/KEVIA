##############################################################################
#==================================STORAGE FUNCTIONS=============================
###############################################################################
from banks import *

name = "death" #nuke these vars?
words = "worderror"
place = "nowhere"
talk = "talkerror"

def fire():
    global name
    global words
    global talk
    global place
    talk = "\n%s: \t \"%s\"" % (name, words)
    if place == "wis":
        wisbank.append(talk)
    elif place == "master":
        masterbank.append(talk)
    elif place == "write":
        writebank.append(talk)
    elif place == "mote":
        motebank.append(talk)
    elif place == "love":
        lovebank.append(talk)
    elif place == "hi":
        hibank.append(talk)
    elif place == "muse":
        musebank.append(talk)
    elif place == "steal":
        stealbank.append(talk)
    elif place == "vy":
        vybank.append(talk)
    else:
        print "fail"