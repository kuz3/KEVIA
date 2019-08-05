import random as r
from mainsoul import *
#import mainsoul
from brain.banks import *

talk = None
words = "Not Working"
mood_current = " >" # move to content.py if possible, or soul
place = None
next = None

###############################################################################
#==================================STORAGE FUNCTIONS=============================
###############################################################################
def creator(words):
    global talk
    talk = "\nCreator: \t \"%s\"" % words
    vyoletbank.append(talk)
def talking(words):
    global talk
    talk = "\nKEVIA: \t \"%s\"" % words
    return talk
def fire(): #naming reverse
    global place
    talking(words)
    if place == "love":
        bank.append(talk)
    elif place == "muse":
        musebank.append(talk)
    elif place == "test":
        testbank.append(talk)
    else:
        print "fail"
#words= "I'm speaking"
#place = "love"
#fire(place)
#print r.choice(bank)
###############################################################################
#==================================MEMORY FUNCTIONS=============================
###############################################################################
def hi(next): #print from bank and store next in bank.
  global hibank
  hibank.append(next)
  print r.choice(hibank)
def massmemory(you_said): #one memory captures all #again do I even need to put the var in here
    global massmemory
    massmembank.append(you_said)
def ask():
  you_said = raw_input(mood_current).lower()
  massmemory(you_said)
  return you_said #what am I returning...

def memory(next):
    global membank
    membank.append(next)
  #SHORTCUT FUNCTIONS
def transporter():
  print "A beam of blinding light shines down upon you.\n All you can see is white. \n Disoriented, strange visions flood your mind until you lose consciousness."
  time.sleep(4)
def notadded():
  print "\nAuthor's Note: This has not tested for errors and has not yet been added.\n Returning you in five seconds"
  time.sleep(5)
  return
#SECRET TEXT FUNCTIONS
def write_help():
  print "You need motivation? Perspective? "###########################################################################
  #print a standard response then return IF=ANY input writersbank.
  #"If you're feeling bored and uncreative, perhaps its a good time to work on something boring and get it done."

def pressanynumber():
    print "\n type a number and press enter to continue"
def pressanyreturn():
    print "\n press any key to return"
    next = ask()
    return
