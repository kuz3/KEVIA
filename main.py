from importall import *
update = "08.17.19"
#KELA...
#from kevia import master # breaks kevia.py
spa.fireall()
def toggle(master, priorities, note):
    if master == "y":
        global next
        bs.mastershot()
        t.sleep(2)
        print priorities
    #    print note
        t.sleep(3)
        bs.moteshot()
        t.sleep(3)
        bs.masterwordshot()
        t.sleep(5)
        bs.prayershot()
        t.sleep(5)
        while next != "fire": #this has failed to execute before.
            bs.museshot()
            next = ask()
#            bs.moteshot()
            #t.sleep(3)
            bs.prayershot()
            t.sleep(5)
#            bs.masterwordshot()
            #t.sleep(3)
            bs.writeshot()
            t.sleep(3)
        kevia_main()
    else:
        start()
def start():
    print "KEVIA: \t \"Initializing\""
    t.sleep(1)
#    print "KEVIA: \t \"...\""
#    t.sleep(1)
#    print "KEVIA: \t \"..\""
#    t.sleep(1)
#    print "KEVIA: \t \".\""
#    t.sleep(1)
    print "KEVIA: \t \"last updated: %s\"" % update
#    t.sleep(1)
#    print "KEVIA: \t \".\""
#    t.sleep(1)
#    print "KEVIA: \t \".\"\n"
    t.sleep(1)
    kevia_main()
def kevia_main():
    global next
    print "Kevia hums and shines a glass cup with an old rag."
    t.sleep(3)
    print """
    \n1. Love!
    \n2. Questions Menu(In Development)
    \n3. Drink Menu(In Development)
    \n4. Morality(In Development)
    \n5. Knowledge(Tentative)""" #rename. Access to Secrets of Adulthood, Law of VideoGaming Life, The other Lists.
    while next != "1" or next != "2":
#        global next
        next = ask()
#START CHOICES

        if next == "1":
            menup.positivity()
        elif next == "2":
            menuq.questions_start()
        elif next == "3":
            menud.drink_start()
        elif next == "4":
            menum.morality()
        elif next == "5":
            write_help()
        elif next == "0":
            kevia_main()
        elif "hi" or "hey" or "hello" in next:
            hi(next)
        elif "love" in next:
            bs.loveshot()
        elif "vyolet" in next:
            bs.vyoletshot()
        elif "exit" or "kill" or "quit" in next:
            s.say("Press CTRL-C to kill me and restart. ")
        else:
            bs.wisshot()
            memory(next) #this memory captures only else output. shouldn't store numbers and such.

#SECRET TEXT FUNCTIONS
def write_help():
  print "You need motivation? Perspective? "###########################################################################
  #print a standard response then return IF=ANY input writersbank.
  #""
