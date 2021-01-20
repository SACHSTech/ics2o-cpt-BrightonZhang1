import time

#play again
def playagain():
    answer = input("Would you like to play/play again? Y or N: ")
    while answer != "Y" and answer != "N":
        time.sleep(1.5)
        print ("Type a viable option!")
        time.sleep(1.5)
        answer = input("Would you like to play/play again? Y or N: ")
    if answer == "Y":
        time.sleep(1.5)
        print("Ok. We will begin shortly.")
        time.sleep(4)
        introduction()
    elif answer == "N":
        time.sleep(1.5)
        print("See you next time!")
          
#intro/part 1
def introduction():
    print("You are in deep slumber.")
    time.sleep(3)
    print("With the distinct voices in the background, you wake up to the morning sun.")
    time.sleep(3)
    print("You feel groggy. Trying to go back to sleep, you are suddenly met with a eerie creature laying under your bed.")
    time.sleep(5)
    print("Looks like the creature came from the ancient underground caves called the void. The creature is purple and small.")
    time.sleep(4)
    option_1 = input(" You can kick it or run outside. Kick or Run?: ")
    
    while not(option_1 == "Run" or "Kick" ):
        print("Type a viable option!")
        time.sleep(1.5)
        option_1 = input(" You can kick it or run outside. Kick or Run?: ")

    if option_1 == "Kick":
        time.sleep(1.5)
        print("You kick it with all of your might. The creature lets out a terrifying shriek, but slowly shrivels away. You Run outside.")
        print("")

    elif option_1 == "Run":
        time.sleep(1.5)
        print("You run outside, only to find ominous creatures roaming around. You look off into the distance. A huge hole has seemed to open. What is it? You head over the hole to peer over the edge")
        print("")

def pathone():
    print("You approach the hole cautiously. However, the ground suddenly starts to crack. You try to run, but the hole splits at an alarming pace. Tripping over a rock, you fall into the void of darkness. You look up, and see your beloved village crumble into bits and pieces. ") 
    
    name = input("You suddenly realize that you had forgotten your name, so you decide to name yourself. State your name:")

    while name == (""):
      print("State an actual name.")
      name = input("You suddenly realize that you had forgotten your name, so you decide to name yourself. State your name:")


playagain()


