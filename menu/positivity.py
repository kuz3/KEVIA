from importall import *
import brain.speechfire as s 
def positivity():
    s.say("Ah, here we are.")
    s.say("Press any key to restart or 0 to return to main.")
    next = ask()
    while next != "0":
         print "Tell me a noun." #using OOP I can set more than one attribute to a noun. Apples are bad and red and green.
         noun = ask()
