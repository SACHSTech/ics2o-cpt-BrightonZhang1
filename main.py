import time

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
        print("You kick it with all of your might. The creature lets out a terrifying shriek, but slowly shrivels away. What is going on? You run outside.")
        
        time.sleep(6)
        print("You are now outside. Many ominous creatures roam the lands of earth. How did this all happen overnight? You suddenly spot a vast hole a few hundred meters north. You start sprinting across the field towards it.")
        time.sleep(7)
        pathone()


    elif option_one.lower().strip() == "run":
        time.sleep(1.5)
        print("You run outside. Many ominous creatures now roam the lands of earth. How did this all happen overnight? Where is everyone? You look off into the distance. A huge hole has seemed to open. What is it?")
        print("")
        pathone()

#First Path
def pathone():
    print("As you are sprinting across the field, you suddenly trip over a small chest. ")
    
    chest_one = input("Would you like to open the chest? Yes/No: ")
    print("")

    while chest_one.lower().strip() != "yes" or chest_one.lower().strip() != "no":
        print("Type Yes or No!")
        chest_one = input("Would you like to open the chest? Yes/No: ")

    if chest_one.lower().strip() == "yes":
        print("You open up the chest. Inside contains a few bandages and a knife. You pick up the items.")
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
        print("Many hours pass and you finally wake up. Your head feels light, and you have a slight migraine. Your injuried are serious, and your entire left leg is bleeding.")
        print("The entire cave is pitch black and you can't see a thing.")
        print("Where are you?")
        
        if bandages == 1:
            print("You notice a buldge in your left pocket. You remember that you had picked up the bandages on the field earlier. You apply the bandages.")
            print("You stand up, ignoring the excrutiating pain.")
            

        else:
            print("You stand up and brush yourself off. What even happened? You limp around when you suddenly bump into hard object.")
            paththree()



    

def paththree():
    print("Oops, it seems to be just a table. You skim the surface and you find a lantern. Surprisingly, it still has some power left. Maybe someone was here previously?")
    print("As you flick the switch of the lantern, it illuminates your surroundings and you spot a knife on the table.")
    knife = input("Would you like to pick up the knife? Yes/No: ")
    print("")

    while knife.lower().strip() != "yes" or knife.lower().strip() != "no":
        print("Type Yes or No!")
        knife = input("Would you like to pick up the knife? Yes/No: ")

    #Splits off path here due to cyclomatic complexity
    if knife.lower().strip() == "yes":
        print("You pick up the knife.")
        def pathfour()
        
    elif knife.lower().strip() == "no":
        print("You decide to ignore the knife.")  
        knife = 0
        print("You continue to venture deeper and deeper into the cave. You left leg is still bleeding, and you feel a bit hazy You then spot a pair of rotten bananas")
        banana = input("Would you like Eat or Ignore the Banana? Eat/Ignore: ")
        
        while banana.lower().strip() != "eat" or banana.lower().strip() != "ignore":
            print("Type Eat or Ignore!")
            banana = input("Would you like to eat them or ignore them? Eat/Ignore ")
        
        if banana.lower().strip() == "eat":
            print("You gobble up the bananas in spite of your taste buds. However, the bananas seemed to be a bait for a trap someone had set up! ")
            print("A net swoops down and you get captured. You then bleed out after a few days.")
            death_one = input("Would you like to go back or quit? Back/Quit: ")
        
            while death_one.lower().strip() != "back" or death_one.lower().strip() != "quit":
                print("Type Back or Quit!")
                death_one = input("Would you like to go back or quit? Back/Quit: ")
        
            if death_one.lower().strip() == "back":
                paththree()
            
            elif death_one.lower().strip() == "quit":
                print("See you next time!")
          
        elif banana.lower().strip() == "ignore":
            print("You ignore the bananas. Good choice, however, you encounter a strange monster. It glares at you with its gleaming eyes. You throw the bananas, but they seem to have no effect! You try to limp away, but you eventually hit a dead end.")
            print('In your last moments, you think,"If only I had a weapon to defend myself with..."')
            death_two = input("Would you like to go back or quit? Back/Quit: ")

            while death_two.lower().strip() != "back" or death_two.lower().strip() != "quit":
                print("Type Back or Quit!")
                death_two = input("Would you like to go back or quit? Back/Quit: ")
        
            if death_two.lower().strip() == "back":
                paththree()
            
            elif death_two.lower().strip() == "quit":
                print("See you next time!")

def pathfour()
    knife == 1
    print("You continue to venture deeper and deeper into the cave. You left leg is still bleeding, and you feel a bit hazy You then spot a pair of rotten bananas")
        banana = input("Would you like Eat or Ignore the Banana? Eat/Ignore: ")
        
    while banana.lower().strip() != "eat" or banana.lower().strip() != "ignore":
            print("Type Eat or Ignore!")
            banana = input("Would you like to eat them or ignore them? Eat/Ignore ")
        
    if banana.lower().strip() == "eat":
        print("You gobble up the bananas in spite of your taste buds. However, the bananas seemed to be a bait for a trap someone had set up! ")
        print("But, you have you trusty knife with you! You cut the net and escape, but a monster suddenly appears before you.")
        print("You try to limp away, but you hit a dead end. You put your back against the wall due to your bleeding leg. As the monster approaches, it raises its claws.")
        print("It attempts to slash you, but you perfectly time it and duck in the nick of time. You then take the opportunity to skewer its insides.")

            death_one = input("Would you like to go back or quit? Back/Quit: ")
        
        while death_one.lower().strip() != "back" or death_one.lower().strip() != "quit":
            print("Type Back or Quit!")
            death_one = input("Would you like to go back or quit? Back/Quit: ")
        
        if death_one.lower().strip() == "back":
            paththree()
            
        elif death_one.lower().strip() == "quit":
            print("See you next time!")
          
    elif banana.lower().strip() == "ignore":
        print("You ignore the bananas. Good choice, however, you encounter a strange monster. It glares at you with its gleaming eyes. You throw the bananas, but they seem to have no effect! You try to limp away, but you eventually hit a dead end.")
        print('')
        death_two = input("Would you like to go back or quit? Back/Quit: ")

        while death_two.lower().strip() != "back" or death_two.lower().strip() != "quit":
            print("Type Back or Quit!")
            death_two = input("Would you like to go back or quit? Back/Quit: ")
        
        if death_two.lower().strip() == "back":
            paththree()
            
        elif death_two.lower().strip() == "quit":
            print("See you next time!")



play() 