from kevia_brain import * 
import time
#TASK LIST: TEXT:
#UNIMPORTED TEXT----------------------- move lots of unimported text here.
#LIFE: Don't worry so much about what other people think of you,
#focus on your words and actions. People remember when you encourage them
#and support them, and that is what they will love you for. And
#you don't do it for their love, you do it because you love them.
#That will bring you social fulfillment far more than fitting in.
#WRITING:
#PERSPECTIVE:
#--------------------------
#LIFE KNOWLEDGE
#WRITING KNOWLEDGE
#REDEFINE KEVIA AS YOUR BRAIN. THIS IS HOW YOU REMEMBER. EVERYTHING. THIS IS ALSO YOU.
#EXPRESSED IN BYTES.

#REDEFINE QUESTIONS AS 3 PARTS. 1. MY MENTAL ASSISTANT AND LEGACY. 2. 3.
#MORALITY START WITH ARISTOTLE y
                                        #Import Law of VideoGaming Life
#common questions for chatbot.
#for wisbank it would be nice to use a dictionary.
#learn your limitations and where to grow.
#add next function for morality (isolate code in trinket to help focus)
#create questions menu. X
#add love statements
#add vyolet statements
#add writer statements
# ask misc musing statements
#add questions page 2.
#CREATE MORALITY SYSTEM. WHERE TO START.... ISOLATE CODE IN TRINKET TO FOCUS. Tomorrow.
#RECENTLY DONE

#VARS
priorities = "\nKEVIA: \t \"currently you have, Me, the Book, Medium, and Textbroker. Have fun!\""
#And also Insta which sends to twitter and facebook quotes beautifully

###############################################################################
#==================================STORAGE============================
###############################################################################
### This is where all new input is sent in

#talking(words)
#banklove()

#deprecated below
#notmywisbank() #call
#vyoletbank.append('NextTruth')

#make this a start function:
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
#            print "user selected drink menu"
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
        elif "love" in next:
            vyolet()
        else:
            print random.choice(wisbank)
            memory(next) #this memory captures only else output. shouldn't store numbers and such.
# IF TALKING
def drink_start(): #D TEXT INTRO
    print "KEVIA: \t \"An adventurous spirit after my own heart. Splendid!\""
    time.sleep(3)
    print "Kevia fumbles with a console of buttons."
    time.sleep(3)
    print "Text illuminates from the bar in front of you. "
    time.sleep(2)
    drink_menu()
def drink_menu(): #D MENU
    global next
    print "\n\tDRINKS\n\n\t\tGlass of Water\t\t1\n\t\tMelon Choly \t\t2\n\t\tInstant Sanity\t\t3\n\t\t\'Lego Network\'\t\t4\n\t\tNapkin\t\t\t5"
    #6. ENDGAME. with passwords to access.
    while next != "1" or next != "2" or next != "3" or next != "4" or next != "5":
        next = ask()
        if next == "1":
            print "KEVIA: \t \"A refined choice for a clean soul. Here you are.\""
            time.sleep(2)
            glass()
        if next == "2":
            print "KEVIA: \t \"A refined choice for a clean soul. Here you are.\""
            time.sleep(2)
            glass()
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
#MOOD FUNCTIONS
def questions_menu_two():
    print """\n\tQUESTIONS(2)\n\n\t\t
    Wisdom Statements (notmywisbank)? \t\t1
    \n\t\tNot yet added?\t\t\t2
    \n\t\tNot yet added?\t\t3
    \n\t\tNot yet added?\t\t4
    \n\t\tGo Back?\t\t\t\t0"""
def mood_main():
    notadded()
#LEARN FUNCTIONS
def morality():
  global next
  noun = None
  #tell me a good or bad
  #tell me something new. i will decide if its good or bad. based on a dictionary.
  #i will be able to set my mood by a percentage.
  #eventually i will have to learn OOP.
  print "Tell me a noun." #using OOP I can set more than one attribute to a noun. Apples are bad and red and green.
  noun = ask()
  print "is %s \n1. good \nor \n2. bad?" % noun
  while next != "1" or next != "2":
    next = ask()
    if next == "1":
      global goodbank
      goodbank.append(noun)
      print "KEVIA: I have added %s to my list of good things."#"\n Here is my current memory of good things: %s " % (noun, goodbank)
      print "Thanks."
      #next.
    elif next == "2":
      global badbank
      badbank.append(noun)
      print "I have added %s to my list of good things.\n Here is my current memory of good things: %s " % (noun, goodbank)
      print "would you like to go back?"
      #All humans are mortal. Socrates is a human. Therefore, Socrates is mortal.

#BRAIN FUNCTIONS (rename later)
#outside call TEXT FUNCTIONS (rename later)
def glass():
    print "\nYou are standing on a floating glass path in endless space. \nStars are all you can see in this infinity."
    notadded()
    drink_menu()
def vyolet():
    print random.choice(vyoletbank)



###################

#start()
kevia_main() #comment out when running
#questions_menu()
