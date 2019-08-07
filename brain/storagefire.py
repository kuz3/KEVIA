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
    elif place == "love":
        lovebank.append(talk)
    elif place == "mote":
        bank.append(talk)
    elif place == "muse":
        musebank.append(talk)
    elif place == "test":
        testbank.append(talk)
    else:
        print "fail"
