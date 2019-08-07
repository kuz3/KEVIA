#===========================================================================
#-------------------RANDOM SPEECH OUTPUT FUNCTIONS--------------------------
#===========================================================================
import random as r
import brain.banks as b

def wisshot(): #used from start
    print r.choice(b.wisbank)
def writeshot(): #used on master toggle
    print r.choice(b.writersbank)
def moteshot(): #used on master toggle
    print r.choice(b.motebank)
def loveshot(): #used where?
    print r.choice(b.wisbank)
def hishot(): #used if next is hi
    print r.choice(b.hibank)
def museshot(): #used if ?
    print r.choice(b.musebank)#
def stealshot(): #used if ?
    print r.choice(b.bank)
def vyshot(): #used if next is vy
    print r.choice(b.vyoletbank)
#def goodshot(): #never used
#    print r.choice(b.bank)
#def badshot(): #never used
#    print r.choice(b.bank)

#def shot(): #used if
#    print r.choice(b.bank)
