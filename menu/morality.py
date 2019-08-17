#move morality somewhere else..
from importall import *
import main as m
import soul.mood as som
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
    s.say("Eventually I want to be able to evaluate that,\n IF 'all humans are mortal, AND Socrates is a human, THEN Socrates is mortal.\' \nBut I'm still learning..")
    s.say("Press enter to continue or 0 to return to main.")
    next = ask()
    if next != "0":
        print "Tell me a noun." #using OOP I can set more than one attribute to a noun. Apples are bad and red and green.
        noun = ask()
        print "is %s \n1. good \nor \n2. bad?" % noun
        while next != "1" or next != "2" or next != "0":
            next = ask()
            if next == "1":
                global goodbank
                goodbank.append(noun)
                print "KEVIA: I have added %s to my list of good things." % noun #"\n Here is my current memory of good things: %s " % (noun, goodbank)
                #print "Thanks."
                s.say(goodbank)
                som.setmood()
                t.sleep(3)
                sc.pressanynumber()
                ok = ask()
                morality()
            elif next == "2":
                print "KEVIA: I have added %s to my list of bad things." % noun #"\n Here is my current memory of good things: %s " % (noun, goodbank)
                global badbank
                som.setmood()
                badbank.append(noun)
                ok = ask()
                morality()
#            elif next == "0":
    else:
        m.kevia_main()

    m.kevia_main()
      #print "I have added %s to my list of good things.\n Here is my current memory of good things: %s " % (noun, goodbank)
      #print "would you like to go back?"
      #
