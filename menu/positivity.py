from importall import *
import main as m
def positivity():
    global next
    bs.hishot()
    t.sleep(2)
    bs.moteshot()
    t.sleep(3)
    bs.masterwordshot()
    t.sleep(4)
    bs.museshot()
    s.say("Press enter to say more or 0 to return to main.")
    next = ask()
    if next == "0":
        m.kevia_main()
    positivity()
    #while next != "fire":
    #    if next == "0":
    #        m.kevia_main()
    #    bs.museshot()
    #    next = ask()
