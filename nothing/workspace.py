###FUUUUCKK MOST  of my problems were probably that i never
#commented out mainbrainpy!!!!
###############################################################################
#==================================STORAGE FUNCTIONS=============================
###############################################################################
from brain.banks import *
#import workspacetwo as w
name = "death"
words = "worderror"
place = "nowhere"
talk = "talkerror"
#def talking(): #why not merge into fire as one function
#BUT ALSO ASK ONLINE FOR HELP WITH MAKING THE CALL TO THE SECOND FUNCTION

def fire(): #naming reverse
    global name # may not keep like this
    global words
    global talk
    global place
    talk = "\n%s: \t \"%s\"" % (name, words)
    print talk
    print place
    if place == "love":
        lovebank.append(talk)
    elif place == "muse":
        musebank.append(talk)
    elif place == "test":
        testbank.append(talk)
    else:
        print "fail"
    #    actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
#def talking(): #why not merge into fire as one function
#BUT ALSO ASK ONLINE FOR HELP WITH MAKING THE CALL TO THE SECOND FUNCTION
#    global name # may not keep like this
#    global words
#    global talk
#    talk = "\n%s: \t \"%s\"" % (name, words)
#    return talk
#def fire(place): #naming reverse
#    talking()
#    print talk
#    print place
#    if place == "love":
#        lovebank.append(talk)
#    elif place == "muse":
#        musebank.append(talk)
#    elif place == "test":
#        testbank.append(talk)
#    else:
#        print "fail"

#def talking(): #why not merge into fire as one function
#BUT ALSO ASK ONLINE FOR HELP WITH MAKING THE CALL TO THE SECOND FUNCTION
#    w.name # may not keep like this
#    w.words
#    talkfire = "\n%s: \t \"%s\"" % (w.name, w.words)
#    talker = talkfire
#    print talker
#    return talkfire
#def fire(place): #naming reverse
#    talker = "errorfire"
#    talking()
#    print talker
#    print w.place
#    if w.place == "love":
#        lovebank.append(talker)
#    elif w.place == "muse":
#        musebank.append(talker)
#    elif w.place == "test":
#        testbank.append(talker)
#     else:
#         print "fail"
    #    actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2

#def creator(words):
