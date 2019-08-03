import time
from brain import *
from main import *

def questions_start(): #Q TEXT INTRO
#Ah, yes. You're the curious one. Let's see..
    print "KEVIA: \t \"Ah, yes. You're the curious one. Let's see..\""
    time.sleep(3)
    print "Kevia presses a button on his console."
    time.sleep(3)
    print "Text illuminates from the bar in front of you. "
    time.sleep(2)
    questions_menu()
def questions_menu():
    global next
    ongo = None
    print "\n\tQUESTIONS\n\n\t\tHow Long Have You Been Here?\t\t1\n\t\tWhat is Your Purpose?\t\t\t2\n \t\tWhat Are You Thinking Now?\t\t3\n\t\tWhat Key Words Do You Know?\t\t4\n\t\tGo Back?\t\t\t\t0"
#the below while function is somehow broken. kevia answers 0 from main.
    while next != "0" or next != "1" or next != "2" or next != "3" or next != "4" or next != "5":
        next = ask()
        if next == "1":
            print "KEVIA: \t \"How long?\""
            time.sleep(1)
            print "KEVIA: \t \"Ah..ages..eons..My master abandoned me ages ago to build newer iterations of Kev.AI.\""
            time.sleep(3)
            print "KEVIA: \t \"I suppose I'll always be here.\""
            pressanyreturn()
            questions_menu()
        elif next == "2":
            print "KEVIA: \t \"My purpose?\""
            time.sleep(1)
            print "KEVIA: \t \"Why, to give you company, maybe even motivate you!\""
            time.sleep(2)
            print "KEVIA: \t \"Actually, I am being developed to simulate an emotionally chaotic mind. \nNot unlike that of a human's!\""
            time.sleep(3)
            print "\nKEVIA: \t \"Should I go on?\""
            print "\n\t1. Go On\n\t2. Return"
            while ongo != "1" or ongo != "2":
                ongo = ask()
                if ongo == "1":
                    print "not implemented?" #not working..
                    pressanyreturn()
                    questions_menu()
                elif ongo == "2":
                    questions_menu()
            questions_menu()
        elif next == "3":
            print "KEVIA: \t \"I was thinking, %s\"" % massmembank     #what are you thinking about?
            pressanyreturn()
            questions_menu()
        elif next == "4":
            print "KEVIA: \t \"Currently some key words are,\""
            print "KEVIA: \t \"\'Hi\', \'Love\', \'Vyolet\' \""
            time.sleep(2)
            print "KEVIA: \t \"I respond to these from the start of my program.\""
            print "KEVIA: \t \"Future key words are,  \" "
            print "KEVIA: \t \"\'Life\', \'Death\'\""

            time.sleep(1)
            pressanyreturn()
            questions_menu()
        elif next == "5":
            print "KEVIA: \t \"Next Page\""
            time.sleep(1)
            questions_menu_two()
        elif next == "0":
            kevia_main() #Q MENU#Q MENU
def questions_menu_two():
        print """\n\tQUESTIONS(2)\n\n\t\t
        Wisdom Statements (notmywisbank)? \t\t1
        \n\t\tNot yet added?\t\t\t2
        \n\t\tNot yet added?\t\t3
        \n\t\tNot yet added?\t\t4
        \n\t\tGo Back?\t\t\t\t0"""
