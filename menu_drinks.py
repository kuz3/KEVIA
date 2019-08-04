import time as t 
from brain import *
def drink_start(): #D TEXT INTRO
    print "KEVIA: \t \"An adventurous spirit after my own heart. Splendid!\""
    t.sleep(3)
    print "Kevia fumbles with a console of buttons."
    t.sleep(3)
    print "Text illuminates from the bar in front of you. "
    t.sleep(2)
    drink_menu()

def drink_menu(): #D MENU
    global next
    print "\n\tDRINKS\n\n\t\tGlass of Water\t\t1\n\t\tMelon Choly \t\t2\n\t\tInstant Sanity\t\t3\n\t\t\'Lego Network\'\t\t4\n\t\tNapkin\t\t\t5"
    #6. ENDGAME. with passwords to access.
    while next != "1" or next != "2" or next != "3" or next != "4" or next != "5":
        next = ask()
        if next == "1":
            print "KEVIA: \t \"A refined choice for a clean soul. Here you are.\""
            t.sleep(2)
            glass()
        if next == "2":
            print "KEVIA: \t \"A refined choice for a clean soul. Here you are.\""
            t.sleep(2)
            glass()
