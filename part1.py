import time
import random2

# for colored Text:
import colorama
#from colorama import Fore

# import my functions:
# from Doc.howItGoes import * THIS LINE ISN'T WORKING
from functionsPart1 import *


# This is the intro for the adventure game
print("\n"*200)
print("<<Awesome Adventure for Andre>>")
print("\n"*3)
time.sleep(3)
print("A long time ago, a warrior strode forth from the frozen north.")
time.sleep(3)
print("Does this warrior have a name?")
name=input("> ")
print(name," the barbarian, sword in hand and looking for adventure.")
time.sleep(3)
print("However, evil is lurking nearby.... muhahahahahhahhhahha")
time.sleep(1)
print("A pair of bulbous eyes regards the hero...")
time.sleep(3)
print("Will", name, "prevail, and win great fortune...")
time.sleep(1)
print("Or die by the hands of great evil...?")
time.sleep(1)
print("\n"*3)
time.sleep(3)
print("Only time will tell....")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(5)
print("\n"*200)


#Here you get your characters strength, cr, health and luck
cr=0
strength=0
health=0
luck=0
print("The mountains of the north make for a hard life.")
print("Press enter to roll the dice and see how strong", name, "is:")
input()
strength=random.randint(1, 20)
print(Fore.GREEN + name, "has a strength value of", strength, ".")

print(Fore.WHITE + "It's a hard life indeed and all northerners are born warriors.")
print("Press enter to roll the dice and see the combat rating for", name, ".")
input()
cr=random.randint(1, 30)
print(Fore.GREEN + name, "has a combat rating of", cr, ".")

print(Fore.WHITE + "Your health is the total of your strength and your combat rating.")
input()
health= strength + cr
print(Fore.GREEN + name, "has a health value of", health, ".")

print(Fore.WHITE + "Everyone needs a certain amount of luck to survive.")
print("Press enter to roll the dice and see how lucky", name, "is.")
input()
luck=random.randint(1, 15)
if luck>13:
    print(name, "is indeed a lucky one and has a luck value of", luck, ".")
else:
    print(Fore.GREEN + name, "has a luck value of", luck, ".")
time.sleep(5)
print("\n"*200)


print(Fore.WHITE + "Here's your character stats:\n")
print(name)
print("Strength:", strength)
print("Combat rate:", cr)
print("Health:", health)
print("Luck:", luck)
print("\n"*5)
print("Press enter to pack your backpack...")
input()
print("\n"*200)
time.sleep(3)

#name = "Nadja"

#Here you choose a character
print("\n\nChoose a character:\n")
characters=[("wizzard", 10, 20, 40, "owl"), ("trainer", 20, 10, 40, "dog"), ("legend", 40, 20, 10, "horse")]   #tupel
print("0."+ characters[0][0])
print("1."+ characters[1][0])
print("2."+ characters[2][0])
cmdlist=["0", "1", "2"]
cmd = int(getcmd(cmdlist, name))
print(Fore.GREEN + "\n\nYou are a " + characters[cmd][0] + "!!!")
time.sleep(1)
print("\n" * 5)
print(Fore.WHITE+"Press enter to pack your stuff...")
input()
print("\n" * 200)


#Here you choose some Items:
myitems = []
itemList = ["an old cookbook", "a fishing rod", "gloves", "a good brush", "gaming cards", "candys"]
cmdlist=["0", "1", "2", "3", "4", "5"]
print(Fore.WHITE + "Luckily, you've found an old but quite nice backpack,")
print("but there's just space for a few things in there.\n")
print("Please pick 3 widgets from the list below.\n")
for count, word in enumerate(itemList):
    print(count, ".", word)
print("\nChoose your first item as insert the number of that item.")
cmd = getcmd(cmdlist, name)
item1 = itemList[int(cmd)]
print("You put", item1, "in your fancy backpack.")
item2 = item1
while item2 == item1:
    print("Please choose your second item.")
    item2 = itemList[int(getcmd(cmdlist, name))]
    if item2 == item1:
        print("You've already put", item2, "in your backpack.")
    else:
        item3 = item2
        print("You put", item2, "in your fancy backpack.")
        print("Please choose your third item.")
        while item3 == item2 or item3 == item1:
            item3 = itemList[int(getcmd(cmdlist, name))]
            if item3 == item2:
                print("You've already put", item2, "in your backpack.")
                print("Please choose another item.")
            elif item3 == item1:
                print("You've already put", item1, "in your backpack.")
                print("Please choose another item.")
            else:
                print(Fore.GREEN + "You've choosen", item1, ",", item2, "and", item3, "!")
                myitems = cmdchange(name, itemList, item1, item2, item3)
time.sleep(1)
print("\n" * 5)
print(Fore.WHITE+"Press enter to start your adventure...")
input()
print("\n" * 200)
time.sleep(3)


# Tinker is giving you something
saying=input(Fore.BLUE + "Wait... could you please write 'Thanks'?")
if saying == "Thanks":
    (tinker, factor) = magic(saying)
    if tinker == 1:
        health=health+factor
        print(Fore.WHITE + "The magical words '", saying, "' gives you", len(saying), " more health.")
    elif tinker == 2:
        luck=luck+factor
        print(Fore.WHITE +"The magical words '", saying, "' gives you", len(saying), " more health.")
    elif tinker == 3:
        strength = strength+factor
        print(Fore.WHITE +"The magical words '", saying, "' gives you", len(saying), " more health.")
    print("\n" * 5)
    time.sleep(3)
    print("Here's your character stats:\n")
    print(name)
    print("Strength:", strength)
    print("Combat rate:", cr)
    print("Health:", health)
    print("Luck:", luck)
    print("\n" * 5)
else:
    print("Good luck!")
print("Press enter to start your adventure...")
input()
print("\n"*200)
time.sleep(3)


# the actual start of the adventure:
print("\n"*200)
print("     You find yourself at a small inn.")
print("There's little gold in your purse but")
print("your sword is sharp, and you're ready for adventure.")
print("With you are three other customers.")
print("A ragged looking man, and a pair of dangerous")
print("looking guards.")
print("\n ------------")
print("Do you approach the...")
print("\n")
print("1. Ragged looking man")
print("2. Dangerous looking guards")
cmdlist = ["1", "2"]
cmd = getcmd(cmdlist, name)
if cmd == "1":
    ragged()
elif cmd == "2":
    guards()





#if __name__=="__main__":
    #start()
