import time
import random
from colorama import Fore

# manages input from user
def getcmd(cmdlist, name):
    i = 0
    i2 = 0
    while i2 == 0:
        cmd = ((input("\n" + name + ">")))
        if cmd in cmdlist:
            return (cmd)
            i2 = 1
        elif i == 2 and cmd != "quit":
            print("\nEnter your choices as detailed in the game.")
            print("or insert 'quit' to leave the game.")
        elif cmd == "quit":
            print("\n----------------")
            time.sleep(1)
            print("Sadly you return to your homeland without fame or fortune...")
            time.sleep(5)
            exit()
        else:
            print("\n Enter your choices as detailed in the game")
            i = i + 1


# works well:
def cmdchange(name, itemList, item1, item2, item3):
    myitems = [item1, item2, item3]
    end = 0
    while end != "1":
        print(Fore.WHITE + "Are you happy with your choice or would you like")
        print("to change something?")
        print("1. I'm happy!")
        print("2. change")
        cmdlist = ["1", "2"]
        end = getcmd(cmdlist, name)
        if end == "1":
            return myitems
        elif end == "2":
            print("What would you like to change?")
            print("1." + myitems[0])
            print("2." + myitems[1])
            print("3." + myitems[2])
            cmdlist = ["1", "2", "3"]
            num = getcmd(cmdlist, name)
            print("Choose another item from what lies on the ground:")
            cmdlist=[]
            for count, word in enumerate(itemList):
                print(count, ".", word)
                cmdlist.append(str(count))
            cmd = getcmd(cmdlist, name)

            #myitems= [item1, item2, item3]
            while itemList[int(cmd)] in myitems:
                print("You've already put", itemList[int(cmd)], "in your backpack.")
                print("Please choose another item.")
                cmd = getcmd(cmdlist, name)
            if num == "1":
                print("You put", itemList[int(cmd)], "in your bag and throw away", item1, "!")
                myitems[0] = itemList[int(cmd)]
            elif num == "2":
                print("You put", itemList[int(cmd)], "in your bag and throw away", item2, "!" )
                myitems[1] = itemList[int(cmd)]
            elif num == "3":
                print("You put", itemList[int(cmd)], "in your bag and throw away", item3, "!" )
                myitems[2] = itemList[int(cmd)]
            print("This is your stuff:")
            for count, word in enumerate(myitems):
                print(count, ".", word)
                cmdlist.append(str(count))


def magic(saying):
    print("... oh... something strange lies in the air...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("... it feels like...")
    time.sleep(2)
    print("... magic.")
    time.sleep(2)
    tinker = random.randint(1, 3)
    return (tinker, len(saying))


def ragged():
    print("\n" * 200)
    print("You walk up to the ragged looking man and greet him.")
    print("He smiles a toothless grin and, with a strange accent, says:")
    print("`Buy me a cup of wine and I'll tell you of great treasure...`")
    time.sleep(2)


def guards():
    print("\n" * 200)
    print("You walk up to the dangerous looking guards and greet them.")
    print("The guards look up from their drinks and snarl at you:")
    print("`What do you want, barbarian?` One guard reaches for the hilt of his sword...")
    time.sleep(2)