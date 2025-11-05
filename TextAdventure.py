# Copyright (c) 2025 TheEmbersOfTwilight
# Licensed under the GNU Affero General Public License v3.0 (AGPL-3.0) for code.
# Creative assets and prose in this repository are licensed under CC BY-NC-SA 4.0 unless otherwise noted.
# See LICENSE-AGPLv3 and LICENSE-CC-BY-NC-SA-4.0 in the repository root for full license texts.
import time
import sys
question = "What do you say?"
choice = "What do you do?"
def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  
        time.sleep(delay)
Razor=False
Wand=False
door1=False
potion1=False
Apprentice=False
type_text("When you are given a choice, type the number associated with the option you would like to choose")
print()
type_text("Have a good experience")
print()
time.sleep(5)
type_text("You awaken in a dark, damp room on a grimy bed")
time.sleep(1)
print()
type_text("You see a shelf on the opposite side of the room from where you currently are.")
time.sleep(1)
print()
type_text("As you get up from the bed, you see that it is being held up by chains connected to the wall.")
time.sleep(1)
print()
type_text("You also see that one wall of the room is made of metal bars.")
time.sleep(1)
print()
while Wand == False:
    type_text(choice)
    time.sleep(1)
    print()
    print("1. Look through the bars")
    time.sleep(1)
    print("2. Look at the shelf")
    time.sleep(1)
    print("3. Inspect the bed")
    choice1=input()
    if choice1 == "1":
        type_text("You see many cells along the hall on the other side of the bars.")
        print()
        time.sleep(1)
        type_text(choice)
        time.sleep(1)
        print()
        print("1. Call out")
        time.sleep(1)
        print("2. Go back")
        choice2 = input()
        if choice2 == "1": 
            type_text("You call out down the empty halls and get no response")
            time.sleep(1)
            print()
            type_text("You walk back into the cell")
            print()
            time.sleep(1)
            continue
        else: 
            type_text("You walk back into the cell")
            print()
            time.sleep(1)
            continue
    elif choice1 == "2": 
        if Razor == True:
                type_text("You look at the shelf and see nothing of interest, you walk back into thhe middle of the cell")
                print()
                time.sleep(1)
                continue
        else:
            type_text("You look at the shelf and see a dull, old style razor")
            time.sleep(1)
            print()
            type_text(choice)
            time.sleep(1)
            print()
            print("1. Pick up the razor")
            time.sleep(1)
            print("2. Leave it")
            choice3=input()
            if choice3 == "1":
                time.sleep(1)
                type_text("You pick up the razor and walk back to the middle of the cell")
                print()
                Razor=True
                continue
            else:
                type_text("You leave it and walk back to the middle of the cell")
                print()
                continue
    elif choice1 == "3":
        type_text("You inspect the bed closer and see a compartment hidden under the mattress")
        print()
        time.sleep(1)
        type_text("In the compartment you see a stick that tapers near the end, it has complex designs carved into it")
        print()
        time.sleep(1)
        type_text("You feel an aura of energy emanating from it and your fingers tingle as you hold it")
        print()
        time.sleep(1)
        type_text("You walk back into the middle of the cell")
        print()
        time.sleep(1)
        Wand=True
type_text("You now see a silhouette of a door on the wall next to the bed")
time.sleep(1)
while door1 == False:
    print()
    type_text(choice)
    print()
    time.sleep(1)
    print("1. Inspect the silhouette")
    time.sleep(1)
    print("2. Inspect the stick")
    choice4=input()
    if choice4 == "2":
        type_text("You inspect the stick and see that its designs are reminiscent of those you have seen in drawings of wands in fantasy books")
        time.sleep(1)
        print()
        continue
    elif choice4 == "1":
        type_text("You inspect the silhouette and see that there is a small hole within it that would fit one end of the stick")
        print()
        time.sleep(1)
        type_text("You stick one end of the stick into the hole, it does not work")
        print()
        time.sleep(3)
        type_text("A few seconds later you realize it must be the other side that works, then stick that end in")
        print()
        time.sleep(1)
        type_text("The door swings open and you walk through")
        print()
        time.sleep(1)
        door1=True
    else:
        continue
type_text("You see a flash of light and your vison goes dark")
print()
time.sleep(3)
type_text("You awake from whatever has affected you, you have no idea how long you've been out but it feels as though it has been a while")
time.sleep(1)
print()
type_text("You see that you are in a room filled with books and beakers of all sorts, many of the beakers are filled with colorful liquids, while others are empty")
print()
time.sleep(1)
while potion1 == False:
    type_text(choice)
    print()
    time.sleep(1)
    print("1. Inspect the books")
    time.sleep(1)
    print("2. Inspect the beakers")
    time.sleep(1)
    choice5=input()
    if choice5 == "1":
        type_text("You take a closer look at the books and see a few of interest")
        time.sleep(1)
        print()
        print("The Secrets of Divination")
        time.sleep(1)
        print("The Sorcerer's Handbook of Draughts")
        time.sleep(1)
        print("How To Aid and Keep Thy Friends Forever")
        time.sleep(1)
        type_text("You decide against taking any of them as you feel a strange aura around them")
        print()
        time.sleep(1)
        continue
    elif choice5 == "2":
        type_text("You look closely at the beakers and see that one has a design on the glass identical to the one on the stick")
        print()
        time.sleep(1)
        type_text("You grab the beaker and pocket it, then hear a strange noise just a few moments later")
        print()
        time.sleep(3)
        potion1=True
    else:
        continue
type_text("You see a tall, robed figure approach you and loudly bellow")
print()
time.sleep(1)
type_text('"What are you doing in my sanctum?"')
print()
time.sleep(1)
type_text(question)
time.sleep(1)
print()
print("1. I'm lost and found this place")
time.sleep(1)
print("2. I'm your new apprentice")
choice6=input()
while Apprentice == False:
    if choice6 == "1":
        type_text('"How did you find this place, then? Did you come here from the prison?')
        print()
        time.sleep(1)
        Apprentice=True
    else:
        type_text('"I do not remember hiring a new apprentice"')
        print()
        type_text('"You are an imposter!"')
        print()
        time.sleep(1)
        type_text("He chants in a language you cannot understand and you feel light headed, you fall and your mind goes blank.")
        print()
        type_text("Game Over")
        print()
        sys.exit()
type_text('"Well then, I will help you for a short while. But do not touch my potions or spellbooks."')
print()
time.sleep(1)
type_text("The man walks you to a small room down a hall that appears as he walks over to the wall where he came from")
print()
time.sleep(1)
type_text("Inside the room is a small bed with what appears to be a down mattress")
print()
time.sleep(1)
type_text("There is also a side table next to the bed and a dresser on the opposite wall")
print()
time.sleep(1)
type_text('"Get some rest, and come talk to me in the morning"')
print()
time.sleep(1)
type_text("You lie down on the bed and quickly fall asleep")
print()
time.sleep(3)
type_text("To be continued...")