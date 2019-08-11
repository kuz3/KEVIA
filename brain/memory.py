from brain.banks import *
import consciousness.moodcurrent as c
import random as r
import brain.speechfire as s

###############################################################################
#==================================MEMORY FUNCTIONS=============================
###############################################################################

def hi(next): #store next in bank and shoot r
  global hibank
  hibank.append(s.yas(next))
  print r.choice(hibank)
def massmemory(you_said): #one memory captures all #again do I even need to put the var in here
    global massmemory
    massmembank.append(you_said)
def ask():
  you_said = raw_input(c.mood_current).lower()
  massmemory(you_said)
  return you_said #what am I returning...

def memory(next):
    global membank
    membank.append(next)
