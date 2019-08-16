#===========================================================================
#-------------------RANDOM SPEECH OUTPUT FUNCTIONS--------------------------
#===========================================================================
import random as r
import brain.banks as b
import brain.speechfire as s
def masterwordshot():
    print
    s.say("Some words for you,")
    print(", ".join(r.sample(b.masterwordbank, k=5)))

def wisshot(): #used from start
    print r.choice(b.wisbank)
def writeshot(): #used on master toggle
    print r.choice(b.writebank)
def moteshot(): #used on master toggle, and morality good
    print r.choice(b.motebank)
def loveshot(): #if love in next
    print r.choice(b.wisbank)
def hishot(): #used if next is hi
    print r.choice(b.hibank)
def museshot(): #used if ?
    print r.choice(b.musebank)#
def stealshot(): #used if ?
    print r.choice(b.bank)
def vyshot(): #used if next is vy
    print r.choice(b.vybank)
def mastershot():
    print r.choice(b.masterbank)
def prayershot():
    print r.choice(b.prayerbank)
#    print "working"
#def goodshot(): #never used
#    print r.choice(b.bank)
#def badshot(): #never used
#    print r.choice(b.bank)

#def shot(): #used if
#    print r.choice(b.bank)
