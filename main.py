import time

'''
--------------------------
Name: The Void
Purpose: To entertain and to quiz people on course material

Author: Brighton Zhang

Created: date 01/26/2021
--------------------------
'''

#play again
def play():
    answer = input("Would you like to play? Yes or No: ")
    
    while answer.lower().strip() != "yes" and answer.lower().strip() != "no":
        time.sleep(1.5)
        print ("Type a viable option!")
        time.sleep(1.5)
        answer = input("Would you like to play? Yes or No: ")
   
    if answer.lower().strip() == "yes":
        print("")
        time.sleep(1.5)
        print("--------")
        print("The Void")
        print("--------")
        print("")
        time.sleep(2)
        print("Your game will begin shortly.")
        time.sleep(4)
        introduction()

    elif answer.lower().strip() == "no":
        print("")
        time.sleep(1.5)
        print("See you next time!")
          
#intro/part 1

def introduction():
    print("")
    print("You are in deep slumber.")
    time.sleep(3)
    print("With the distinct voices in the background, you wake up to the morning sun.")
    time.sleep(3)
    print("Feeling groggy, you toss and turn to try to fall back asleep. Your phone rings and you reach to grab it. Something tickles your palm. You are suddenly met with a eerie creature laying under your bed.")
    time.sleep(5)
    print("Looks like the creature came from the ancient underground caves called the void. The creature is purple and small.")
    time.sleep(4)
   
    option_one = input("You can kick it or run outside. Kick or Run?: ")
    print("")

    while option_one.lower().strip() != "run" and option_one.lower().strip() != "kick":
        print("Type a viable option!")
        time.sleep(1.5)
        option_one = input(" You can kick it or run outside. Kick or Run?: ")

    if option_one.lower().strip() == "kick":
        time.sleep(1.5)
        print("You kick it with all of your might. The creature lets out a terrifying shriek, but slowly shrivels away. What is going on? You grab your bag and you run outside.")
        
        time.sleep(6)
        print("You are now outside. Many ominous creatures roam the lands of earth. How did this all happen overnight? You suddenly spot a vast hole a few hundred meters north. You start sprinting across the field towards it.")
        time.sleep(7)
        pathone()

    elif option_one.lower().strip() == "run":
        time.sleep(1.5)
        print("You grab your bag and you run outside. Many ominous creatures now roam the lands of earth. How did this all happen overnight? Where is everyone? You look off into the distance. A huge hole has seemed to open. What is it?")
        print("")
        pathone()

#First Path
def pathone():
    print("As you are sprinting across the field, you suddenly trip over a small chest. ")
    
    chest_one = input("Would you like to open the chest? Yes/No: ")
    print("")

    while chest_one.lower().strip() != "yes" and chest_one.lower().strip() != "no":
        print("Type Yes or No!")
        chest_one = input("Would you like to open the chest? Yes/No: ")

    if chest_one.lower().strip() == "yes":
        print("You open up the chest. Inside contains a few bandages. You pick up the item.")
        bandages = 1

    elif chest_one.lower().strip() == "no":
        print("You decide to ignore the chest. You stand up and continue running towards the hole.")

    time.sleep(3)
    print("You approach the hole cautiously. However, the ground suddenly starts to crack. You try to run, but the hole splits at an alarming pace. Tripping over a rock, you fall into the void of darkness. You look up, and see your beloved village crumble into bits and pieces. ") 
    time.sleep(6)
    name = input("You suddenly realize that you had forgotten your name, so you decide to name yourself. State your name:")

    while name == (""):
        print("Please state an actual name.")
        time.sleep(1)
        name = input("You suddenly realize that you had forgotten your name, so you decide to name yourself. State your name:")

    if name != (""):
        time.sleep(1.5)
        print(" That's an interesting name,", name)
        time.sleep(1.5)
        print("You are knocked out unconcious after the fall. It is a miracle you survived.")
        time.sleep(1.5)
        print("Many hours pass and you finally wake up. Your head feels light, and you have a slight migraine. Your injuried are serious, and your entire left leg is bleeding.")
        time.sleep(3)
        print("The entire cave is pitch black and you can't see a thing.")
        time.sleep(1.5)
        print("Where are you?")
        time.sleep(1.5)
        
        if bandages == 1:
            print("You notice a buldge in your left pocket. You remember that you had picked up the bandages on the field earlier. You apply the bandages.")
            time.sleep(3)
            print("You stand up, ignoring the excrutiating pain. You suddenly bump into something.")
            time.sleep(1.5)
            pathtwo()
        
        else:
            print("You stand up and brush yourself off. What even happened? You limp around when you suddenly bump into hard object.")
            time.sleep(1.5)
            paththree()


def pathtwo():
    print("Oops, it seems to be just a table. You skim the surface and you find a lantern. Surprisingly, it still has some power left. Maybe someone was here previously?")
    time.sleep(3)
    print("As you flick the switch of the lantern, it illuminates your surroundings and you spot a knife on the table.")
    time.sleep(3)
    knife = input("Would you like to pick up the knife? Yes/No: ")
    print("")

    if knife.lower().strip() == "yes":
        time.sleep(1.5)
        print("You pick up the knife.")
        pathfive()
        
    elif knife.lower().strip() == "no":
        time.sleep(1.5)
        print("You decide to ignore the knife.") 
        time.sleep(1.5) 
        print("You continue to venture deeper and deeper into the cave. You left leg is still bleeding, and you feel a bit hazy. You then spot a pair of rotten bananas")
        time.sleep(3.5)
        banana = input("Would you like to Eat or Ignore the Banana? Eat/Ignore: ")
        
        while banana.lower().strip() != "eat" and banana.lower().strip() != "ignore":
            time.sleep(1.5)
            print("Type Eat or Ignore!")
            banana = input("Would you like to eat them or ignore them? Eat/Ignore ")
        
        if banana.lower().strip() == "eat":
            time.sleep(1.5)
            print("You gobble up the bananas in spite of your taste buds. However, the bananas seemed to be a bait for a trap someone had set up! ")
            time.sleep(3)
            print("A net swoops down and you get captured. You then get stuck in the net for many weeks and you eventually die of hunger.")
            time.sleep(2)
            death_five = input("Would you like to go back or quit? Back/Quit: ")
        
            while death_five.lower().strip() != "back" and death_five.lower().strip() != "quit":
                time.sleep(1.5)
                print("Type Back or Quit!")
                death_five = input("Would you like to go back or quit? Back/Quit: ")
        
            if death_five.lower().strip() == "back":
                time.sleep(1.5)
                paththree()
            
            elif death_five.lower().strip() == "quit":
                time.sleep(1.5)
                print("See you next time!")
          
        elif banana.lower().strip() == "ignore":
            time.sleep(1.5)
            print("You ignore the bananas. Good choice, however, you encounter a strange monster. It glares at you with its gleaming eyes. You throw the bananas, but they seem to have no effect! You then sprint at max speed, going right past the creature.")
            time.sleep(4)
            print("You make a quick turn, and you lose track of the monster.")
            time.sleep(1.5)
            print("Phew. You start going deeper into the cave when you feel a bit thirsty")
            time.sleep(1.5)
            print("You drink the last few gulps from your water bottle.")
            time.sleep(1.5)
            print("Suddenly, the ground begins to rumble. A great rift splits in front of you, as if someone was making an entrance for you.")
            time.sleep(2)
            print("As you enter the hole, bright light flushes into your eyes and you squint. You look around, and you spot a shadow. It appears that the mysterious figure has been the culprit for the incidences all along!")
            time.sleep(4)
            print("You approach slowly, but you suddenly stop. The shadowy figure seems to a mage and casts a spell on you. You then suddenly faint and collapse.")
            time.sleep(3)
            print("You are unconcious again...")
            time.sleep(1.5)
            print("You wake up sweating on the cold, rocky ground. The mysterious lights still illuminate the room. You stand up, but you suddenly hear something inside of your head.")
            time.sleep(3)
            print("Answer at least 6 questions in this quiz correctly and I will let you escape!")
            time.sleep(1.5)
            print("Each room will have 4 locked doors with one correct answer, go through the correct door to proceed, good luck.")
            time.sleep(1.5)
            print("Confused, you dust yourself off and you get ready.")
            time.sleep(1.5)
            quiz()

def paththree():
    print("Oops, it seems to be just a table. You skim the surface and you find a lantern. Surprisingly, it still has some power left. Maybe someone was here previously?")
    time.sleep(1.5)
    print("As you flick the switch of the lantern, it illuminates your surroundings and you spot a knife on the table.")
    time.sleep(1.5)
    knife = input("Would you like to pick up the knife? Yes/No: ")
    print("")

    while knife.lower().strip() != "yes" and knife.lower().strip() != "no":
        time.sleep(1.5)
        print("Type Yes or No!")
        time.sleep(1.5)
        knife = input("Would you like to pick up the knife? Yes/No: ")
    
    #Splits off path here due to cyclomatic complexity
    if knife.lower().strip() == "yes":
        time.sleep(1.5)
        print("You pick up the knife.")
        time.sleep(1.5)
        pathfour()
        
    elif knife.lower().strip() == "no":
        time.sleep(1.5)
        print("You decide to ignore the knife.")  
        time.sleep(1.5)
        print("You continue to venture deeper and deeper into the cave. Your left leg is still bleeding, and you feel a bit hazy. You then spot a pair of rotten bananas")
        time.sleep(3)
        banana = input("Would you like to Eat or Ignore the Banana? Eat/Ignore: ")
        
        while banana.lower().strip() != "eat" and banana.lower().strip() != "ignore":
            time.sleep(1.5)
            print("Type Eat or Ignore!")
            time.sleep(1.5)
            banana = input("Would you like to eat them or ignore them? Eat/Ignore ")
        
        if banana.lower().strip() == "eat":
            time.sleep(1.5)
            print("You gobble up the bananas in spite of your taste buds. However, the bananas seemed to be a bait for a trap someone had set up! ")
            time.sleep(3)
            print("A net swoops down and you get captured. You then bleed out after a few days.")
            time.sleep(1.5)
            death_one = input("Would you like to go back or quit? Back/Quit: ")
        
            while death_one.lower().strip() != "back" and death_one.lower().strip() != "quit":
                time.sleep(1.5)
                print("Type Back or Quit!")
                time.sleep(1.5)
                death_one = input("Would you like to go back or quit? Back/Quit: ")
        
            if death_one.lower().strip() == "back":
                time.sleep(1.5)
                paththree()
            
            elif death_one.lower().strip() == "quit":
                time.sleep(1.5)
                print("See you next time!")
          
        elif banana.lower().strip() == "ignore":
            time.sleep(1.5)
            print("You ignore the bananas. Good choice, however, you encounter a strange monster. It glares at you with its gleaming eyes. You throw the bananas, but they seem to have no effect! You try to limp away, but you eventually hit a dead end.")
            time.sleep(3)
            print('In your last moments, you think,"If only I had a weapon to defend myself with..."')
            time.sleep(1.5)
            death_two = input("Would you like to go back or quit? Back/Quit: ")

            while death_two.lower().strip() != "back" and death_two.lower().strip() != "quit":
                time.sleep(1.5)
                print("Type Back or Quit!")
                time.sleep(1.5)
                death_two = input("Would you like to go back or quit? Back/Quit: ")
        
            if death_two.lower().strip() == "back":
                time.sleep(1.5)
                paththree()
            
            elif death_two.lower().strip() == "quit":
                time.sleep(1.5)
                print("See you next time!")


def pathfour():
    print("You continue to venture deeper and deeper into the cave. You left leg is still bleeding, and you feel a bit hazy. You then spot a pair of rotten bananas")
    time.sleep(3)
    banana = input("Would you like to Eat or Ignore the Banana? Eat/Ignore: ")
        
    while banana.lower().strip() != "eat" and banana.lower().strip() != "ignore":
        time.sleep(1.5)
        print("Type Eat or Ignore!")
        time.sleep(1.5)
        banana = input("Would you like to eat them or ignore them? Eat/Ignore ")
        
    if banana.lower().strip() == "eat":
        time.sleep(1.5)
        print("You gobble up the bananas in spite of your taste buds. However, the bananas seemed to be a bait for a trap someone had set up! ")
        time.sleep(3)
        print("But, you have you trusty knife with you! You cut the net and escape, but a monster suddenly appears before you.")
        time.sleep(2)
        print("You try to limp away, but you hit a dead end. You put your back against the wall due to your bleeding leg. As the monster approaches, it raises its claws.")
        time.sleep(3)
        print("It attempts to slash you, but you perfectly time it and duck in the nick of time. You then take the opportunity to skewer its insides.")
        time.sleep(3)
        print("After venturing for a few more hours, you unfortunately bleed out.")
        time.sleep(1.5)
        death_three = input("Would you like to go back or quit? Back/Quit: ")
        
        while death_three.lower().strip() != "back" and death_three.lower().strip() != "quit":
            time.sleep(1.5)
            print("Type Back or Quit!")
            time.sleep(1.5)
            death_three = input("Would you like to go back or quit? Back/Quit: ")
        
        if death_three.lower().strip() == "back":
            time.sleep(1.5)
            paththree()
            
        elif death_three.lower().strip() == "quit":
            time.sleep(1.5)
            print("See you next time!")
          
    elif banana.lower().strip() == "ignore":
        time.sleep(1.5)
        print("You ignore the bananas. Good choice, however, you encounter a strange monster. It glares at you with its gleaming eyes. You throw the bananas, but they seem to have no effect! You try to limp away, but you eventually hit a dead end.")
        time.sleep(3)
        print("You then reach for your knife and grip it tightly. You take a deep breath and you sprint at max speed towards the creature. You drive a knife through its insides, skewering it.")
        time.sleep(3)
        print("Phew. You start going deeper into the cave when you feel a bit thirsty")
        time.sleep(1.5)
        print("You drink the last few gulps from your water bottle.")
        time.sleep(1.5)
        print("Suddenly, the ground begins to rumble. A great rift splits in front of you, as if someone was making an entrance for you.")
        time.sleep(3)
        print("As you enter the hole, bright light flushes into your eyes and you squint. You look around, and you spot a shadow. It appears that the mysterious figure has been the culprit for the incidences all along!")
        time.sleep(3)
        print("You approach slowly, but you suddenly stop. The shadowy figure seems to a mage and casts a spell on you. You then suddenly faint and collapse.")
        time.sleep(3)
        print("You are unconcious again...")
        time.sleep(1.5)
        print("You wake up sweating on the cold, rocky ground. The mysterious lights still illuminate the room. You stand up, but you suddenly hear something inside of your head.")
        time.sleep(3)
        print("Answer at least 6 questions in this quiz correctly and I will let you escape!")
        time.sleep(1.5)
        print("Each room will have 4 locked doors with one correct answer, go through the correct door to proceed, good luck.")
        time.sleep(3)
        print("Confused, you dust yourself off and you get ready.")
        time.sleep(1.5)
        altquiz()


def pathfive():
    print("You continue to venture deeper and deeper into the cave. You left leg is still bleeding, and you feel a bit hazy. You then spot a pair of rotten bananas")
    time.sleep(1.5)
    banana = input("Would you like to Eat or Ignore the Banana? Eat/Ignore: ")
        
    while banana.lower().strip() != "eat" and banana.lower().strip() != "ignore":
        time.sleep(1.5)
        print("Type Eat or Ignore!")
        time.sleep(1.5)
        banana = input("Would you like to eat them or ignore them? Eat/Ignore ")
        
    if banana.lower().strip() == "eat":
        time.sleep(1.5)
        print("You gobble up the bananas in spite of your taste buds. However, the bananas seemed to be a bait for a trap someone had set up! ")
        time.sleep(3)
        print("But, you have you trusty knife with you! You cut the net and escape, but a monster suddenly appears before you.")
        time.sleep(3)
        print("You try to run away, but you hit a dead end. As the monster approaches, it raises its claws.")
        time.sleep(1.5)
        print("It attempts to slash you, but you perfectly time it and duck in the nick of time. You then take the opportunity to skewer its insides.")
        time.sleep(3)
        print("After the fight, you sit down to take a break. How are you even going to get out?")
        time.sleep(1.5)
        print("A few hours pass and you're extremely dehydrated. You reach for your bottle in your bag to drink the last few gulps")
        time.sleep(3)
        print("Suddenly, the ground begins to rumble. A great rift splits in front of you, as if someone was making an entrance for you.")
        time.sleep(3)
        print("As you enter the hole, bright light flushes into your eyes and you squint. You look around, and you spot a shadow. It appears that the mysterious figure has been the culprit for the incidences all along!")
        time.sleep(3)
        print("You approach slowly, but you suddenly stop. The shadowy figure seems to a mage and casts a spell on you. You then suddenly faint and collapse.")
        time.sleep(3)
        print("You are unconcious again...")
        time.sleep(1.5)
        print("You wake up sweating on the cold, rocky ground. The mysterious lights still illuminate the room. You stand up, but you suddenly hear something inside of your head.")
        time.sleep(3)
        print("Answer at least 6 questions in this quiz correctly and I will let you escape!")
        time.sleep(1.5)
        print("Each room will have 4 locked doors with one correct answer, go through the correct door to proceed, good luck.")
        time.sleep(3)
        print("Confused, you dust yourself off and you get ready.")
        time.sleep(1.5)
        quiz()

    elif banana.lower().strip() == "ignore":
        time.sleep(1.5)
        print("You ignore the bananas. Good choice, however, you encounter a strange monster. It glares at you with its gleaming eyes. You throw the bananas, but they seem to have no effect! You try to limp away, but you eventually hit a dead end.")
        time.sleep(3)
        print("You then reach for your knife and grip it tightly. You take a deep breath and you sprint at max speed towards the creature. You drive a knife through its insides, skewering it.")
        time.sleep(3)
        print("However, it still manages to live. With your knife still in its body, you have no other weapon to protect yourself with.")
        time.sleep(1.5)
        print("It then violently slashes you, leaving you to bleed out in the cave.")
        time.sleep(1.5)
        death_six = input("Would you like to go back or quit? Back/Quit: ")
        
        while death_six.lower().strip() != "back" and death_six.lower().strip() != "quit":
            time.sleep(1.5)
            print("Type Back or Quit!")
            time.sleep(1.5)
            death_six = input("Would you like to go back or quit? Back/Quit: ")
        
        if death_six.lower().strip() == "back":
            time.sleep(1.5)
            pathfive()
            
        elif death_six.lower().strip() == "quit":
            time.sleep(1.5)
            print("See you next time!")


def altquiz():
    time.sleep(1.5)
    print("")
    print("Loading Quiz...")
    print("")
    time.sleep(1.5)
    print("Type the letter that corresponds with the answer!")
        
    questions_correct = 0

    time.sleep(1.5)
    print("")
    print("A. DPI")
    print("B. Refresh rate")
    print("C. Clock Speed")
    print("D. Memory Speed")
    print("")
    time.sleep(1.5)
    question_one = input("Which of these measurements apply to the CPU?: ")
    
    if question_one.lower().strip() == ("c"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")
       
    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")

    time.sleep(1.5)
    print("")
    print("A. Refresh Rate")
    print("B. Watts")
    print("C. DPI")
    print("D. Mbps")
    print("")
    time.sleep(1.5)
    question_two = input("Which of these measurements apply to Wifi Networking?: ")
        
    if question_two.lower().strip() == ("d"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")
        
    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")

    time.sleep(1.5)
    print("")
    print("A. Adware")
    print("B. Spyware")
    print("C. Computer Virus")
    print("D. Computer Worm")
    print("")
    time.sleep(1.5)
    question_three = input("A standalone malware computer program that replicates itself in order to spread to other computers: ")
        
    if question_three.lower().strip() == ("d"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")
        
    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")

    time.sleep(1.5)
    print("")
    print("A. Computer Virus")
    print("B. Ransomware")
    print("C. Adware")
    print("D. Spyware")
    print("")
    time.sleep(1.5)
    question_four = input("A type of malware from cryptovirology that threatens to publish the victim's data or perpetually block access to it unless the cyber actor is paid: ")
        
    if question_four.lower().strip() == ("b"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")
        
    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")

    time.sleep(1.5)
    print("")
    print("A. Polling Rate")
    print("B. Refresh Rate")
    print("C. Efficiency Rating")
    print("D. Spyware")
    print("")
    time.sleep(1.5)
    question_five = input("Which of the terms mentioned above relate to a computer mouse?: ")
        
    if question_five.lower().strip() == ("a"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")
        
    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")
    
    time.sleep(1.5)
    print("Unfortunately, halfway through the quiz, you bleed out due to your leg. Maybe you should patch that wound up next time... ")
    time.sleep(1.5)
    death_eight = input("Would you like to go to the start of the quiz or restart the game? Quiz/Quit/Restart: ")
        
    while death_eight.lower().strip() != "back" and death_eight.lower().strip() != "quit":
        time.sleep(1.5)
        print("Type Back or Restart!")
        time.sleep(1.5)
        death_eight = input("Would you like to go back to the start of the game? Yes/No: ")

    if death_eight.lower().strip() == "yes":
        time.sleep(1.5)
        pathone()
    
    #Cyclomatic complexity limiting options again. Max 15

def quiz():
    time.sleep(1.5)
    print("")
    print("Loading Quiz...")
    print("")
    time.sleep(1.5)
    print("Type the letter that corresponds with the answer!")
        
    questions_correct = 0

    time.sleep(1.5)
    print("")
    print("A. DPI")
    print("B. Refresh rate")
    print("C. Clock Speed")
    print("D. Memory Speed")
    print("")
    time.sleep(1.5)
    question_one = input("Which of these measurements apply to the CPU?: ")
    
    if question_one.lower().strip() == ("c"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")
       
    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")

    time.sleep(1.5)
    print("")
    print("A. Refresh Rate")
    print("B. Watts")
    print("C. DPI")
    print("D. Mbps")
    print("")
    time.sleep(1.5)
    question_two = input("Which of these measurements apply to Wifi Networking?: ")

   
    if question_two.lower().strip() == ("d"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")
  
    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")

    time.sleep(1.5)
    print("")
    print("A. Adware")
    print("B. Spyware")
    print("C. Computer Virus")
    print("D. Computer Worm")
    print("")
    time.sleep(1.5)
    question_three = input("A standalone malware computer program that replicates itself in order to spread to other computers: ")
        
    if question_three.lower().strip() == ("d"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")
        
    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")

    time.sleep(1.5)
    print("")
    print("A. Computer Virus")
    print("B. Ransomware")
    print("C. Adware")
    print("D. Spyware")
    print("")
    time.sleep(1.5)

    question_four = input("A type of malware from cryptovirology that threatens to publish the victim's data or perpetually block access to it unless the cyber actor is paid: ")
        
    if question_four.lower().strip() == ("b"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")
        
    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")

    time.sleep(1.5)
    print("")
    print("A. Polling Rate")
    print("B. Refresh Rate")
    print("C. Efficiency Rating")
    print("D. Spyware")
    print("")
    time.sleep(1.5)
    question_five = input("Which of the terms mentioned above relate to a computer mouse?: ")
        
    if question_five.lower().strip() == ("a"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")
        
    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")
        
    time.sleep(1.5)
    print("")
    print("A. Random Access Memory")
    print("B. Hard Drive")
    print("C. Motherboard")
    print("D. GPU")
    print("")
    time.sleep(1.5)
    question_six = input("Serves as a connection between the various different parts of a computer system. For example, it transfers data from the CPU to the GPU: ")
        
    if question_six.lower().strip() == ("c"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")
        
    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")

    time.sleep(1.5)
    print("")
    print("A. Windows")
    print("B. macOS")
    print("C. Linux")
    print("D. Android")
    print("")
    time.sleep(1.5)
    question_seven = input("Most popular operating system used in the world: ")
        
    if question_seven.lower().strip() == ("a"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")
        
    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")

    time.sleep(1.5)
    print("")
    print("A. Mechanical Switch")
    print("B. DPI")
    print("C. GHZ")
    print("D. Refresh Rate")
    print("")
    time.sleep(1.5)
    question_eight = input("Which of the terms mentioned above relate to a Keyboard?: ")
        
    if question_eight.lower().strip() == ("a"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")

    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")

    time.sleep(1.5)
    print("")
    print("A. Megabytes Per Second")
    print("B. Megabits Per Second")
    print("C. 1000 Kilobytes Per Second")
    print("D. Kilobits Per Second")
    print("")
    time.sleep(1.5)
    question_nine = input("What does Mbps stand for? ")
        
    if question_nine.lower().strip() == ("b"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")
        
    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")

    time.sleep(1.5)
    print("")
    print("A. Double Data rate")
    print("B. Mechanical Switch")
    print("C. Refresh Rate")
    print("D. Clock Speed")
    print("")
    time.sleep(1.5)
    question_ten = input("What term mentioned above related to a GPU?: ")
        
    if question_ten.lower().strip() == ("d"):
        questions_correct += 1
        time.sleep(1.5)
        print("")
        print("Correct!")
        print("")
        
    else:
        time.sleep(1.5)
        print("")
        print("Wrong!")
        print("")

    if questions_correct >= 6:
        time.sleep(1.5)
        ending()

    else:
        time.sleep(1.5)
        print("Unfortunately, that quiz was life or death. You failed to answer 6 questions correctly and as a result, you remain trapped in the rooms for all of eternity. ")

        time.sleep(2.5)
        death_seven = input("Would you like to go to the start of the quiz or restart the game? Quiz/Quit/Restart: ")
        
        while death_seven.lower().strip() != "back" and death_seven.lower().strip() != "quit":
            time.sleep(1.5)
            print("Type Back or Restart!")
            time.sleep(1.5)
            death_seven = input("Would you like to go back to the start of the quiz? Yes/No: ")

        if death_seven.lower().strip() == "yes":
            time.sleep(1.5)
            play()
        #Cyclomatic Complexity limiting options again. Max 15
def ending():
    time.sleep(1.5)
    print("You have successfully answered more than 6 questions on the quiz! The mysterious figure keeps its promise and lets you go. You head up to the surface, only to realize that your world is still in chaos.")
    time.sleep(2.5)
    print("You then decide to go rogue and venture the world. The End.")
    time.sleep(1.5)
    end = input("Would you like to quit or restart the game? Quit/Restart: ") 
    
    while end.lower().strip() != "back" and end.lower().strip() != "quit":
        time.sleep(1.5)
        print("Type Restart or Quit!")
        time.sleep(1.5)
        end = input("Would you like to go to restart the game or quit? Quit/Restart: ")
        
    if end.lower().strip() == "quit":
        time.sleep(1.5)
        print("See you next time!")

    elif end.lower().strip() == "restart":
        time.sleep(1.5)
        play()

play()


