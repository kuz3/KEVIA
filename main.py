from maincontent import *
from mainmenu import *
from brain import *
from content.sparkfire import *
import consciousness.bankshot as c
import random as r
import time as t
#from kevia import master # breaks kevia.py
def toggle(master, speech, priorities, motivational):
    if master == "y":
        global next
        print "%s" % priorities
        print "%s" % priorities

        while next != "fire":
            next = ask()
            c.wisshot
    else:
        start()
def start():
    print "KEVIA: \t \"Initializing\""
    t.sleep(2)
    print "KEVIA: \t \"...\""
    t.sleep(1)
    print "KEVIA: \t \"..\""
    t.sleep(1)
    print "KEVIA: \t \".\""
    t.sleep(1)
    print "KEVIA: \t \"last updated: 08.06.19\""
    t.sleep(1)
    print "KEVIA: \t \".\""
    t.sleep(1)
    print "KEVIA: \t \".\"\n"
    t.sleep(1)
    kevia_main()
def kevia_main():
    fireall()#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<!!!!!!!!!!!!!!!!!!!!!!!!!!
    global next
    print "Kevia hums and shines a glass cup with an old rag."
    t.sleep(3)
    print """
    \n1. Drink Menu
    \n2. Questions Menu
    \n3. Morality
    \n4. Knowledge(Tentative)""" #rename. Access to Secrets of Adulthood, Law of VideoGaming Life, The other Lists.
    while next != "1" or next != "2":
#        global next
        next = ask()
#START CHOICES
        if next == "1":
            drink_start()
        elif next == "2":
            questions_start()
        elif next == "3":
            morality()
        elif next == "4":
            write_help()
        elif next == "0":
            kev_main()
        elif "hi" in next:
            hi(next)
        elif "love" in next:
            c.loveshot()
        elif "vyolet" in next:
            c.vyoletshot()
        #elif "love" in next:
        #    love()
        else:
            c.wisshot()
            memory(next) #this memory captures only else output. shouldn't store numbers and such.
