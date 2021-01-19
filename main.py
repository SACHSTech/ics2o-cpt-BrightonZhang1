import time

#play again
def playagain():
    answer = input("Would you like to play/play again? Y or N: ")
    if answer == "Y":
        time.sleep(1.5)
        print("Ok we will begin shortly")
        time.sleep(4)
        introduction()

    elif answer == "N":
        print("See you next time!")

#intro/part 1
def introduction():
    print("You are in deep slumber.")
    time.sleep(3)
    print("With the distinct voices in the background, you wake up to the morning sun.")
    time.sleep(1.5)
    time.sleep(3)
    print("You feel groggy. Trying to go back to sleep, you are suddenly met with a eerie creature laying under your bed.")
    time.sleep(1.5)
    print("Looks like the creature came from the ancient underground caves called the void. The creature is purple and small.")
    option_1 = input(" You can kick it or run outside. Kick or Run?: ")
    if option_1 == "Kick":
        print("You kick it with all of your might. The creature lets out a terrifying shriek, but slowly shrivels away. You Run outside.")
    
    elif option_1 == "Run":
        print("You run outside, only to find ominous creatures roaming around. You look off into the distance. A huge hole has seemed to open. What is it? You head over the hole to peer over the edge")
    
    else: 
        print("Type Kick or Run.")
        option_1 = input(" You can kick it or run outside. Kick or Run?: ")
        
            


playagain()


#name
name = input("You suddenly realize that you had forgotten your name, so you decide to name yourself. State your name:")

while name == (""):
    print("State an actual name.")
    name = input("You suddenly realize that you had forgotten your name, so you decide to name yourself. State your name:")