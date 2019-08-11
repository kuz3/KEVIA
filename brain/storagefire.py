##############################################################################
#==================================STORAGE FUNCTIONS=============================
###############################################################################
from banks import *

name = "death" #nuke these vars?
words = "worderror"
place = "nowhere"
talk = "talkerror"

def fire(store):
    global name
#    global words
#    global talk
    global place
    talk = "\n%s: \t \"%s\"" % (name, store)
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
    elif place == "good":
        goodbank.append(talk)
    elif place == "bad":
        badbank.append(talk)  
    else:
        print "fail"
