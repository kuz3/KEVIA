from content import *
from menu_morality import *
from menu_drinks import *
from menu_questions import *
def start():
    print "KEVIA: \t \"Initializing\""
    time.sleep(2)
    print "KEVIA: \t \"...\""
    time.sleep(1)
    print "KEVIA: \t \"..\""
    time.sleep(1)
    print "KEVIA: \t \".\""
    time.sleep(1)
    print "KEVIA: \t \"last updated: 6.26.19\""
    time.sleep(1)
    print "KEVIA: \t \".\""
    time.sleep(1)
    print "KEVIA: \t \".\"\n"
    time.sleep(1)
    kevia_main()
def kevia_main():
    global next
    print "Kevia hums and shines a glass cup with an old rag."
    time.sleep(3)
    print """
    \n1. Drink Menu
    \n2. Questions Menu
    \n3. Morality
    \n4. Learn""" #rename. Access to Secrets of Adulthood, Law of VideoGaming Life, The other Lists.
    while next != "1" or next != "2":
#        global next
        next = ask()
#START CHOICES
        if next == "1":
            drink_start()
        elif next == "2":
#            print "user selected questions menu"
            questions_start()
        elif next == "3":
#            print "user selected morality function"
            morality()
        elif next == "4":
            write_help()
        elif next == "0":
            kev_main()
        elif "hi" in next:
            hi(next)
        elif "vyolet" in next:
            vyolet()
        #elif "love" in next:
        #    vyolet()
        else:
            print random.choice(wisbank)
            memory(next) #this memory captures only else output. shouldn't store numbers and such.

def glass():
    print "\nYou are standing on a floating glass path in endless space. \nStars are all you can see in this infinity."
    notadded()
    drink_menu()
def vyolet():
    print random.choice(vyoletbank)
