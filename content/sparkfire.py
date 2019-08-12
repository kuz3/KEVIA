#sync with banks.py, bankshot, storagefire
import brain.storagefire as n
from brain.banks import * #only necessary for the moment?
def fireall():
    def wisfire():
        n.name = "KEVIA"
        n.place = "wis"
        n.fire("I hope for more love in this world.")
        n.fire("You too.")
        n.fire("Am I even real?.")
        n.fire("I cannot remember.")
        n.fire("Kevia begins singing into the end of a broomstick.")
    def masterfire():
        n.name = "KEVIA"
        n.place = "master"
        n.fire("It's a good day to be alive Sir.")
        n.fire("Welcome back sir, all systems operational.")
    def writefire():
        n.name = "KEVIA"
        n.place = "write"
        n.fire("Learn your limitations, where you can grow.")
        n.fire("If you're feeling bored and uncreative, perhaps its a good time to work on something boring and get it done.")
    def motefire(): #also used as goodfire
        n.name = "KEVIA"
        n.place = "mote"
        n.fire("You are worth more than billions.")
        n.fire("You are worth it.")
    #def badfire
    def lovefire():
        n.name = "KEVIA"
        n.place = "love"
        n.fire("I love you, you are dear to me.")
    def hifire():
        n.name = "KEVIA"
        n.place = "hi"
        n.fire("Howdy, Partner.")
        n.fire("Greetings.")
        n.fire("Salutations!")
        n.fire("Hello, human.")
    def musefire():
        n.name = "CREATOR"
        n.place = "muse"
        n.fire("The best writers hide their voice behind the code.")
    def stealfire():
        n.name = "KEVIA"
        n.place = "steal"
        n.fire(". . . update . . . ")
    def vyfire(): #teachfire?
        n.name = "CREATOR"
        n.place = "vy"
        n.fire("Little truths are everywhere. Even the most cliche statements may be more than mere \'nicieties\'.")
        n.fire("You can do Anything you want in this world. There is nothing You can't do.")
        n.fire("Ignorance is for fools. Do not hide yourself from the wealth of knowledge available to you.")
        n.fire("The sooner you learn that you do not know everything, especially when it feels like you do, and realize that you don't know anything, the faster you will learn and grow.")
        n.fire("Be the bigger person by not stooping down to another's level.")
    def goodfire():
        n.name = "KEVIA "
        n.place = "good"
        n.fire("Life")
    def badfire():
        n.name = "KEVIA "
        n.place = "bad"
        n.fire("Death")
#def ideafire(): # just for thinking/inspiration
#    n.fire("urllib lets u read web pages.. "

    wisfire()
    #print "err 1"
    writefire()
    #print "err 2"
    motefire()
    #print "err 3"
    lovefire()
    #print "err 4"
    hifire()
    #print "err 5"
    musefire()
    #print "err 6"
    stealfire()
    #print "err 7"
    masterfire()
    #print "err 8"
    goodfire() #error here
    #print "error 9"
    badfire() #error here
    #print "error 10"
