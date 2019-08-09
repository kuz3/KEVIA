
import consciousness.moodcurrent as c
import random as r
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
  you_said = raw_input(c.mood_current).lower()
  massmemory(you_said)
  return you_said #what am I returning...

def memory(next):
    global membank
    membank.append(next)
