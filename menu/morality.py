#move morality somewhere else..
import time as t
from mainbrain import *
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
  print "Tell me a noun." #using OOP I can set more than one attribute to a noun. Apples are bad and red and green.
  noun = ask()
  print "is %s \n1. good \nor \n2. bad?" % noun
  while next != "1" or next != "2":
    next = ask()
    if next == "1":
      global goodbank
      goodbank.append(noun)
      print "KEVIA: I have added %s to my list of good things." % noun #"\n Here is my current memory of good things: %s " % (noun, goodbank)
      #print "Thanks."
      s.say(goodbank)
      som.setmood()
      #next.
    elif next == "2":
      global badbank
      badbank.append(noun)
      #print "I have added %s to my list of good things.\n Here is my current memory of good things: %s " % (noun, goodbank)
      #print "would you like to go back?"
      #All humans are mortal. Socrates is a human. Therefore, Socrates is mortal.
      som.setmood()
