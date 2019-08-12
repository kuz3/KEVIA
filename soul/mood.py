#see notmycode/moodpotential
import time as t
import consciousness.moodcurrent as moc
import brain.speechfire as s
import consciousness.bankshot as bs
import brain.banks as b
import consciousness.shortcuts as cut

def setmood():
    if len(b.goodbank) == len(b.badbank):
        moc.mood_current = ":|"
        s.say("I know as many good things as I do bad things!")
    elif len(b.goodbank) > len(b.badbank):
        moc.mood_current = ":]"
        s.say("I now know more good things than bad things!")
        t.sleep(2)
        s.say("That makes me want to say,")
        t.sleep(2)
        bs.moteshot()
    elif len(b.goodbank) < len(b.badbank):
        moc.mood_current = ":["
        s.say("I know more bad things than good things!")
