#move morality somewhere else..
from importall import *
import time as t
#from mainbrain import *
import soul.mood as som
import main as m
##############################
#LEARN FUNCTIONS
def morality():
    global next
    noun = None
    #tell me a good or bad
    #tell me something new. i will decide if its good or bad. based on a dictionary.
    #i will be able to set my mood by a percentage.
    #eventually i will have to learn OOP.
    s.say("Welcome to the prototype Morality Function.")
    t.sleep(1)
    s.say("I basically go ahead and..")
    s.say("Press any key to continue or 0 to return to main.")
    next = ask()
    while next != "0":
        print "Tell me a noun." #using OOP I can set more than one attribute to a noun. Apples are bad and red and green.
        noun = ask()
        print "is %s \n1. good \nor \n2. bad?" % noun
        while next != "1" or next != "2":
              next = ask()
              while noun != "1" or "2" or "0":
                if next == "1":
                    global goodbank
                    goodbank.append(noun)
                    print "KEVIA: I have added %s to my list of good things." % noun #"\n Here is my current memory of good things: %s " % (noun, goodbank)
                    #print "Thanks."
                    s.say(goodbank)
                    som.setmood()
                    cut.pressanyreturn() # cut?
                    morality()
                elif next == "2":
                    print "KEVIA: I have added %s to my list of bad things." % noun #"\n Here is my current memory of good things: %s " % (noun, goodbank)
                    global badbank
                    som.setmood()
                    badbank.append(noun)
                    cut.pressanyreturn()
                    morality()
    print "Press any key to return to main"
    m.kevia_main()
      #print "I have added %s to my list of good things.\n Here is my current memory of good things: %s " % (noun, goodbank)
      #print "would you like to go back?"
      #All humans are mortal. Socrates is a human. Therefore, Socrates is mortal.
