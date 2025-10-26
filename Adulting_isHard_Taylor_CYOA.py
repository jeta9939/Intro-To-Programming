#Introduction
Introduction = """Welcome to "Adulting is Hard." 
Today you are Ben, a normal human adult with bills to pay. 
Your goal is to get to work on time. If Ben is fired Game Over and run the code to play again. Good luck!"""
print(Introduction)

#variables
wakeUp = """Ben's alarm is going off, should he wake up and start the day, or hit the snooze button?
1 - Wake up and start the day
2 - Hit the snooze, it's only 15 minutes
"""

Coffee = """Ben needs caffeine to function, should he make a pot at home ore swing by starbucks on his way to work?
1 - Make a pot at home
2 - Spend exorbitant prices for coffee that tastes like chemicals
"""

Clothes = """But what should I wear? - Ben exclaims 
1 - Screw it, have Ben go to work in his pajamas
2 - Choose a nice business casual outfit in the closet
"""

Teeth = """Ben hates brushing his teeth, should he give it a try, or skip polishing his pearly whites?
1 - Brush and floss your teeth
2 - Nah
"""

Commute = """As Ben rushes out the front door to his car, he notices he has a flat! What should he do?
1 - Use his PTO and take the day off?
2 - Catch the next bus at the bus stop down the block
"""

#wakeUp
run = True
validChoice = False


while (validChoice == False):
    firstChoice = input(wakeUp)
    if (firstChoice == "1"):
        print("Ben grudgingly stretches awake and heaves himself up out of bed.")
        validChoice = True
    elif (firstChoice == "2"):
        print("Happily slapping the snooze button, Ben dives back under the covers. Ben slept through his alarm and missed work, Ben was fired")
        validChoice = True
    else:
        print("please enter 1 or 2")
        validChoice = False


#Coffee
run = True
validChoice = False

while (validChoice == False):
    secondChoice = input(Coffee)
    if (secondChoice == "1"):
        print("Slowly, Ben makes a decent cup of joe.")
        validChoice = True
    elif (secondChoice == "2"):
        print("Joe stopped by Starbies and was late to work, Ben was fired")
        validChoice = True
    else:
        print("please enter 1 or 2")
        validChoice = False


#Teeth
run = True
validChoice = False

while (validChoice == False):
    secondChoice = input(Teeth)
    if (secondChoice == "1"):
        print("Ben brushes and flosses his teeth until they are squeaky clean.")
        validChoice = True
    elif (secondChoice == "2"):
        print("""Ben happily skips this part of his routine, but when he gets to work his breath knocks out several coworkers
        including his boss and he is immediately fired after they come to""")
        validChoice = True
    else:
        print("please enter 1 or 2")
        validChoice = False


#Clothes
run = True
validChoice = False

while (validChoice == False):
    secondChoice = input(Clothes)
    if (secondChoice == "1"):
        print("Ben was excited to have his own personal PJ day at work, as soon as he entered the office - he was fired on the spot.")
        validChoice = True
    elif (secondChoice == "2"):
        print("Ben rifles through the closet and quickly chooses a smart business casual option for the day.")
        validChoice = True
    else:
        print("please enter 1 or 2")
        validChoice = False


#Commute
run = True
validChoice = False

while (validChoice == False):
    secondChoice = input(Commute)
    if (secondChoice == "1"):
        print("""Super thrilled, Ben bounded back into his home and went back to sleep, 
        he woke up in the afternoon to find a YOU'RE FIRED text on his phone display.""")
        validChoice = True
    elif (secondChoice == "2"):
        print("Annoyed, Ben trudges down to the Bus Stop, after a surprisingly calming ride, he entered his office and started work. CONGRATS You Win!")
        validChoice = True
    else:
        print("please enter 1 or 2")
        validChoice = False



#Claude helped me via the following chat: https://claude.ai/share/2c1c6af1-aa75-49ae-97e9-bf43d25c1d06