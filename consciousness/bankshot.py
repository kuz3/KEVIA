#===========================================================================
#-------------------RANDOM SPEECH OUTPUT FUNCTIONS--------------------------
#===========================================================================
import random as r
import brain.banks as b
def vyshot():
    print r.choice(b.vyoletbank)
def wisshot():
    print r.choice(b.wisbank)
