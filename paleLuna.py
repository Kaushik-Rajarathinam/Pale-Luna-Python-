# Game by Kaushik Rajarathinam
# Recreation of the game PALE LUNA. 


#IMPORT MODULES
import random
import time
import math
GOLD = 0
SHOVEL = 0
ROPE = 0
HOLE = 0

# Define Commands
def introGame():
    global SHOVEL
    global GOLD
    global ROPE
    print("V.1.2")
    print()
    time.sleep(0)
    print("PALE LUNA")
    time.sleep(0)
    print()
    print("Program created by: Kaushik Rajarathinam")
    print("This game is a recreation of the Original Pale Luna Creepypasta.")
    print()
    time.sleep(1)
    s = input("Press enter to begin: ")
    if s == "{s":
        print()
        print("-- { DEVELOPER > SKIP TO PLAYGAME()")
        playGame()
    elif s == "{s2":
        GOLD = 1
        SHOVEL = 1
        ROPE = 1
        print()
        print("-- { DEVELOPER > SKIP TO PART3()")
        part3()
    elif s == "{sE":
        GOLD = 1
        SHOVEL = 1
        ROPE = 1
        print()
        print("-- {DEVELOPER > SKIP TO PLAYGAME6()")
        playGame6()
    else:
        print()
        print()
        startGame()

def startGame():
    global SHOVEL
    global GOLD
    global ROPE
    time.sleep(2)
    print()
    print("You are in a dark room. Moonlight shines through the window.")
    time.sleep(0.5)
    #-----------------------------------------------------------------------------
    print("There is GOLD in the corner, along with a SHOVEL and a ROPE.")
    time.sleep(0.1)
    print("There is a DOOR to the EAST")
    print()
    print()
    time.sleep(2)
    print("Command?")
    print()
    time.sleep(0.5)
    print("You can see a DOOR here.")
    print()
    playGame()

def playGame():
    global GOLD
    global SHOVEL
    global ROPE
    s = input(">")
    if s == "PICK UP GOLD":
        if GOLD == 0:
            time.sleep(2.5)
            print("-- Taken")
            GOLD = 1
            print()
            playGame()
        else:
            print("-- You have already picked this item up.")
            print()
            playGame()
    elif s == "EXIT DOOR":
        part2()

    elif s == "PICK UP SHOVEL":
        if SHOVEL == 0:
            time.sleep(2.5)
            print("-- Taken")
            SHOVEL = 1
            print()
            playGame()
        else:
            print("-- You have already picked this item up.")
            print()
            playGame()
    elif s == "PICK UP ROPE":
        if ROPE == 0:
            time.sleep(2.5)
            print("-- Taken")
            ROPE = 1
            print()
            playGame()
        else:
            print("-- You have already picked this item up.")
            print()
            playGame()
    elif s == "PICK UP GOLD, SHOVEL, ROPE":
        time.sleep(1.4)
        print("-- GOLD   > Taken.")
        print("-- SHOVEL > Taken.")
        print("-- ROPE   > Taken.")
        ROPE = 1
        GOLD = 1
        SHOVEL = 1
        print()
        playGame()

    else:
        time.sleep(1)
        print("-- I don't understand that.")
        print()
        playGame()

def part2():
    time.sleep(2)
    print()
    print("Reap your reward.")
    print()
    time.sleep(2)
    print("PALE LUNA SMILES AT YOU!")
    time.sleep(1)
    print()
    print()
    print("You are in a forest. There are ")
    time.sleep(0.1)
    print("paths to the NORTH, WEST, and EAST.")
    print()
    time.sleep(1)
    print("Command?")
    print()
    playGame2()

def playGame2():
    global SHOVEL
    global GOLD
    global ROPE
    s0 = input(">")
    if s0 == "USE GOLD":
        if GOLD == 1:
            time.sleep(2.5)
            GOLD = 1
            print("-- Not now.")
            print()
            playGame2()
        else:
            print("-- You have no such item.")
            print()
            playGame2()
    elif s0 == "USE SHOVEL":
        if SHOVEL == 1:
            time.sleep(1.4)
            SHOVEL = 1
            print("-- Not here.")
            print()
            playGame2()
        else:
            print("-- You have no such item.")
            print()
            playGame2()
    elif s0 == "USE ROPE":
        if ROPE == 1:
            time.sleep(1.4)
            ROPE = 2
            print("-- You've already used this item.")
            print()
            playGame2()
        else:
            print("-- You have no such item.")
            print()
            playGame2()
    elif s0 == "EAST":
        print()
        part3()
    elif s0 == "WEST":
        print()
        gameOver()
    elif s0 == "NORTH":
        print()
        gameOver()
    else:
        print("-- I don't understand that.")
        print()
        playGame2()

def part3():
    time.sleep(0.5)
    print()
    print("Reap your reward.")
    print()
    time.sleep(0.5)
    print("PALE LUNA SMILES AT YOU!")
    time.sleep(1)
    print()
    print()
    print("You are in a forest. There are ")
    time.sleep(0.1)
    print("paths to the NORTH, WEST, and EAST.")
    print()
    time.sleep(1)
    print("Command?")
    print()
    playGame3()

def playGame3():
    global SHOVEL
    global GOLD
    global ROPE
    s0 = input(">")
    if s0 == "USE GOLD":
        if GOLD == 1:
            time.sleep(1.4)
            GOLD = 1
            print("-- Not now.")
            print()
            playGame3()
        else:
            print("-- You have no such item.")
            print()
            playGame3()
    elif s0 == "USE SHOVEL":
        if SHOVEL == 1:
            time.sleep(1.4)
            SHOVEL = 1
            print("-- Not here.")
            print()
            playGame3()
        else:
            print("-- You have no such item.")
            print()
            playGame3()
    elif s0 == "USE ROPE":
        if ROPE == 1:
            time.sleep(1.4)
            ROPE = 1
            print("-- You've already used this item.")
            print()
            playGame3()
        else:
            print("-- You have no such item.")
            print()
            playGame3()

    elif s0 == "NORTH":
        if ROPE == 1:
            if GOLD == 1:
                if SHOVEL == 1:
                    print()
                    part4()
                else:
                    part4()
            else:
                part4()
        else:
            part4()
    elif s0 == "EAST":
        print()
        gameOver()
    elif s0 == "WEST":
        print()
        gameOver()
    else:
        print("-- I don't understand that. Type in the given direction.")
        print()
        playGame3()

def part4():
    time.sleep(0.5)
    print()
    print("Reap your reward.")
    print()
    time.sleep(0.5)
    print("PALE LUNA SMILES AT YOU!")
    time.sleep(1)
    print()
    print()
    print("You are in a forest. There are ")
    time.sleep(0.1)
    print("paths to the SOUTH and EAST.")
    print()
    time.sleep(1)
    print("Command?")
    print()
    playGame4()

def playGame4():
    global SHOVEL
    global GOLD
    global ROPE
    s0 = input(">")
    if s0 == "USE GOLD":
        if GOLD == 1:
            time.sleep(1.4)
            GOLD = 1
            print("-- Not now.")
            print()
            playGame4()
        else:
            print("-- You have no such item.")
            print()
            playGame4()
    elif s0 == "USE SHOVEL":
        if SHOVEL == 1:
            time.sleep(1.4)
            SHOVEL = 1
            print("-- Not here.")
            print()
            playGame4()
        else:
            print("-- You have no such item.")
            print()
            playGame4()
    elif s0 == "USE ROPE":
        if ROPE == 1:
            time.sleep(1.4)
            ROPE = 1
            print("-- You've already used this item.")
            print()
            playGame4()
        else:
            print("-- You have no such item.")
            print()
            playGame4()

    elif s0 == "SOUTH":
        print()
        part5()

    elif s0 == "EAST":
        print()
        gameOver()
    elif s0 == "GOBBLE":
        print()
        gameOver()
    else:
        print("-- I don't understand that. Type in the given direction.")
        print()
        playGame4()

def part5():
    time.sleep(0.5)
    print()
    print("Reap your reward.")
    print()
    time.sleep(0.5)
    print("PALE LUNA SMILES AT YOU!")
    time.sleep(1)
    print()
    print()
    print("You are in a forest. There are ")
    time.sleep(0.1)
    print("paths to the WEST and EAST.")
    print()
    time.sleep(1)
    print("Command?")
    print()
    playGame5()

def playGame5():
    global SHOVEL
    global GOLD
    global ROPE
    s0 = input(">")
    if s0 == "USE GOLD":
        if GOLD == 1:
            time.sleep(1.4)
            GOLD = 1
            print("-- Not now.")
            print()
            playGame5()
        else:
            print("-- You have no such item.")
            print()
            playGame5()
    elif s0 == "USE SHOVEL":
        if SHOVEL == 1:
            time.sleep(1.4)
            SHOVEL = 1
            print("-- Not here.")
            print()
            playGame5()
        else:
            print("-- You have no such item.")
            print()
            playGame5()
    elif s0 == "USE ROPE":
        if ROPE == 1:
            time.sleep(1.4)
            ROPE = 1
            print("-- You've already used this item.")
            print()
            playGame5()
        else:
            print("-- You have no such item.")
            print()
            playGame5()

    elif s0 == "WEST":
        print()
        part6()

    elif s0 == "EAST":
        print()
        gameOver()
    elif s0 == "GOBBLE":
        print()
        gameOver()
    else:
        print("-- I don't understand that. Type in the given direction.")
        print()
        playGame5()

def part6():
    print()
    time.sleep(1)
    print("PALE LUNA SMILES WIDE")
    print()
    time.sleep(2)
    print("There are no paths")
    print()
    time.sleep(1)
    print("PALE LUNA SMILES WIDE")
    print()
    time.sleep(2)
    print("The ground is soft")
    print()
    time.sleep(1)
    print("Here")
    time.sleep(1)
    print()
    print("Command?")
    print()
    playGame6()

def playGame6():
    global SHOVEL
    global GOLD
    global ROPE
    global HOLE
    s = input(">")
    if s == "DIG HOLE":
        if SHOVEL == 1:
            if HOLE == 0:
                time.sleep(1.4)
                HOLE = 1
                print("-- You dug a hole.")
                print()
                playGame6()
            else:
                print("-- You cannot dig another hole.")
                print()
                playGame6()
        else:
            print("-- You weren't able to dig a hole with your hands!")
            print()
            playGame6()
    elif s == "DROP GOLD":
        if HOLE == 1:
            if GOLD == 1:
                time.sleep(1.4)
                GOLD = 2
                print("-- You dropped GOLD into the hole.")
                print()
                playGame6()
            else:
                print("-- You don't have any such thing.")
                print()
                playGame6()
        else:
            time.sleep(1.4)
            print("-- You dropped GOLD onto the ground.")
            GOLD = 0
            print()
            playGame6()
    elif s == "PICK UP GOLD":
        if GOLD == 0:
            if HOLE == 0:
                time.sleep(1.4)
                print("-- Taken.")
                GOLD = 1
                print()
                playGame6()
            else:
                print("-- You can't pick up the GOLD in the hole.")
                print()
                playGame6()
        elif GOLD == 1:
            print("-- You cannot pick up no such thing.")
            print()
            playGame6()
        elif GOLD == 2:
            if HOLE == 1:
                print("-- You cannot pick up GOLD from the hole.")
                print()
                playGame6()
            else:
                print("Fatal Error.") # IMPOSSIBLE CONDITIONS
        else:
            print("Fatal Error.") # IMPOSSIBLE CONDITIONS

    elif s == "EAST":
        print("-- There are no paths.")
        print()
        playGame6()
    elif s == "WEST":
        print("-- There are no paths.")
        print()
        playGame6()
    elif s == "SOUTH":
        print("-- There are no paths.")
        print()
        playGame6()
    elif s == "NORTH":
        print("-- There are no paths.")
        print()
        playGame6()
    elif s == "FILL HOLE":
        if HOLE == 1:
            if GOLD == 2:
                time.sleep(1.4)
                print("-- You filled hole.")
                HOLE = 0
                time.sleep(1)
                print()
                endGame()
            else:
                time.sleep(1.4)
                print("-- You filled hole.")
                HOLE = 0
                print()
                playGame6()
        else:
            print("-- There is no hole to fill.")
    else:
        print("-- I don't understand that.")
        print()
        playGame6()

def endGame():
    print()
    time.sleep(1)
    print("Congratulations!")
    print("---- 40.24248 ----")
    print("---- -121.4434 ----")
    time.sleep(2)
    print("Game. Finished")
    time.sleep(1)
    print()
    s = input("Enter to Continue or type quit: ")
    if s == "quit":
        print()
        print("Thanks for playing...")
        time.sleep(2)
    else:
        final()

def final():
    time.sleep(2)
    input("You finally realize that the those numbers")
    input(" in the end of the game were coordinates")
    input("of Longitude and Latitude. Upon using the maps")
    input(" you locate the spot near Lassen Volcanic Park.")
    input()
    input("You decide to trek alone to spot because you ")
    input(" believe that the creator of the game has left")
    input("some treasure behind. You journey in the forest.")
    input("You follow sets of paths.")
    input()
    input("You then start to oddly notice that the paths you")
    input(" take match the same paths in the game. You start")
    input("to wonder that something seems a bit off.")
    input()
    input("You then reach a spot where there were no more paths, just")
    input(" like in the game. You are confused until you notice that")
    input("You were stepping on uneven ground. Taking your shovel, you")
    input(" begin to dig, hoping for some lost treasure until. ")
    input("the decaying head of blond girl showed up...")
    input()
    input("Then everything gets put in your head...")
    input("Pale luna smiles wide...")
    input("Gold... Blond Hair.")
    input("Reap your reward... choke the girl with the rope...")
    input("PALE LUNA SMILES WIDE.")
    input("Drop Gold... fill hole...")
    input()
    input("The next thing you do, you call the cops immediately. The girl")
    input(" was identified as Karen Paulsen, 11 years old. She was")
    input("missing for a year and a half according the San Diego Police.")
    input("The rest of Karen's body was never found...")

def gameOver():
    global GOLD
    global SHOVEL
    global ROPE
    print("Sorry, but you lost...")
    time.sleep(4)
    print()
    print("Try Again? ('Yes'/'No')")
    s = input(">")
    if s == "y" or "yes" or "YES" or "Yes":
        print()
        SHOVEL = 0
        ROPE = 0
        GOLD = 0
        startGame()
    else:
        print()
        print("What a loser..")
        time.sleep(2)
#COMMANDS RUN HERE
introGame()
