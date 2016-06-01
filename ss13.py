import random
import os
import time

author's = 'aftonweb, Julia'
welcome = 'Welcome to the Hell!'

life = 45

clowns = random.randrange(0, 4)

hit = 0

money = 0

clownattack = random.randrange(1, 2)

hitMultiplier = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 1]

weapon = {"Crowbar": 2, "Stechkin Pistol": 3, "Energy Crossbow": 4, "Energy Sword": 5, "Revolver": 6, "Balloon": 8, "Captain Laser": 12, "IVB": 11, "Replica Katana": 13, "Wand Of Autism" 10, "Firebutt" 7}

supplies = ["Candy", "Cup Ramen", "Chips", "4no Raisins", "Dr.Gibb", "Baguette", "Xenomeat", "The thing that you do not know", "Banana"]

inventory = {"Chips": 5,
             "Candy": 1,
             "Cup Ramen": 0,
             "4no Raisins": 0,
             "Dr.Gibb": 0,
             "Baguette": 0,
             "Xenomeat": 0,
             "The thing that you do not know": 0,
             "Banana": 1,
             }

flavorText = {"Candy": "Nougat love it or hate it",
	      "Cup Ramen": "A taste that reminds you of your school years.",
	      "Chips": "Commander Riker's What-The-Crisps",
	      "4no Raisins": "Best Raisins in the universe. Not sure why.",
	      "Dr.Gibb": "A delicious mixture of 42 different flavors.",
	      "Baguette": "Bon appetit!",
              "Xenomeat": "Uf...Xenomorph meat?WHAT THE FU...",
              "The thing that you do not know": "You do not know, what is this."
              "Banana": "Favorite clown food.Ha-ha. Not funny joke"
			 }
myWeapons = ["Crowbar"]

stations = ["Infinity Station", "Soviet Station", "Tau Ceti Station", "Animus Station", "Hippie Station"]
youAreHere = 0



def fightClowns(clowns):
    global life
    global hit
    global money
    clownhealth = random.randrange(2, 3) * clowns

    if clownhealth > 0:
        print(str(clowns) + " clowns stagger towards you. Ready your " + str.lower(myWeapons[0]) + "!\n")
        while clownhealth > 0:
            attack = raw_input("Attack, or Run? (A for attack, R for run)\n")
            attackclown = weapon[myWeapons[0]] * random.randrange(0, 2)
            if (str.upper(attack) == "A"):
                print(str(clowns) + " clowns attacked you!")
                if attackclown > 0:
                    print("You hit the clown!")
                    life = life - clownattack*clowns
                    clownhealth = clownhealth - attackclown
                    money = money + 1
                    print("Clown life is now: " +str(clownhealth))
                    print("Your life is now: " + str(life))
                    time.sleep(4)
                    os.system('cls')
                if (attackclown <= 0):
                    print("That was a lucky miss. Next time you should attack!")
                    life = life - clownattack*clowns
                    time.sleep(4)
                    os.system('cls')
                    
            elif str.upper(attack) == "R":
                  stumblee = random.randrange(0, 2)
                  stumble = random.randrange(1, 7)
                  if stumblee > 0:
                      print("Run away from the clowns, you have stumbled and lost " + str(stumble) + " hp")
                      life = life - stumble
                      return 0
                      time.sleep(4)
                      os.system('cls')
                  else:
                      print("Nothing was happened.")
def lootRoom():
    global life
    global clownattack
    runAway = False
    loot = raw_input("Loot this Room? (Y/N)\n")
    if(str.upper(loot) == "Y"):
        foundItem = supplies[random.randrange(0, len(supplies)-1)]
        foundWeapon = weapon.keys()[random.randrange(1, len(weapon)-1)]
        clowns = random.randrange(0, 2)
        print(str(clowns) + " clowns found in room.")
        time.sleep(4)
        os.system('cls')
        if clowns > 0:
            fightClowns(clowns)
        else:
            print ("The room is empty of clowns, but full of cool stuff...")
        if (runAway != True):
            takeItem = raw_input("You found a " + foundItem + "\nEquip? (Y/N)")
            takeWeapon = raw_input("Cool! You found a " + foundWeapon + "\nEquip? (Y/N)")
            if str.upper(takeWeapon) == "Y": myWeapons.insert(0, foundWeapon)
            if str.upper(takeItem) == "Y": inventory[foundItem] += 1
            time.sleep(4)
            os.system('cls')
            print ("Current weapon: " + str(myWeapons[0]))
            print ("Destruction power: " + str(weapon[myWeapons[0]]))
            print("Inventory:\n==========")
            for item in inventory:
                if(inventory[item] > 0):
                    print (item + ": " + str(inventory[item]))
            print("\n")
            time.sleep(4)
            os.system('cls')
def lootBodies():
    global life
    global clownattack
    loot = raw_input("On your way you found the bodies. Would you like to loot the bodies? (Y/N)\n")
    if (str.upper(loot) == "Y"):
        if (random.randrange(0,9)>7):
            print("A clown was not yet dead!\n")
            time.sleep(4)
            os.system('cls')
            fightClowns(clowns)
        else:
            foundItem = supplies[random.randrange(0, len(inventory)-1)]
            print("You found a " + foundItem)
            equip = raw_input("Equip? (Y/N)")
            if (str.upper(equip) == "Y"):
                inventory[foundItem] += 1
                print("Inventory: " + str(inventory))
            time.sleep(4)
            os.system('cls')
def leaveStation():
    global stations
    global youAreHere
    global life
    print("Where would you like to go? You are currently in " + stations[youAreHere])
    whereTo = ""
    i = 1
    for station in stations:
        if station != stations[youAreHere]:
            whereTo = whereTo + "   " + str(i) + ") " + station + "\n"
            i = i + 1
    stationIndex =  int(raw_input("I want to go to: " + "\n" + whereTo))
    youAreHere = stationIndex
    print("Welcome to " + stations[youAreHere])
    time.sleep(4)
    os.system('cls')
def checkInventory():
    global life
    global flavorText
    print ("Current Money: " + str(money))
    print ("Current weapon: " + str(myWeapons[0]))
    print ("Destruction power: " + str(weapon[myWeapons[0]]))
    print("Inventory:\n==========")
    i = 1
    invArray = []
    for item in inventory:
        if(inventory[item] > 0):
            print (str(i) + ") " + item + ": " + str(inventory[item]))
            invArray.append(item)
            i = i + 1
    print str(i) + ") Exit Inventory"
    inventoryIndex = int(raw_input("Select the item from the list.\n"))-1
    if inventoryIndex != len(invArray):
        myItem = invArray[inventoryIndex]
        if myItem == "Candy":
            life = life + 5
        elif myItem == "Xenomeat":
            xenorandom = random.randrange(-1, 3)
            xenodamage = random.randrange(3, 5)
            xenoheal = random.randrange(1, 4)
            if xenorandom == 0:
                print("Nothing was happened")
            elif xenorandom == 1:
                life = life - xenodamage
                print("You were poisoned!")
                print("Your life is now: " + str(life))
            elif xenorandom == 2:
                life = life + xenoheal
                print("Do you feel that taste great.")
                print("Your life is now: " + str(life))
        elif myItem == "The thing that you do not know":
            thingrandom = random.randrange(0, 4)
            if thingrandom == 1:
                print("Oh! You spawned clowns!")
                fightClowns(2)
            elif thingrandom == 0:
                print("Nothing was happened")
            elif thingrandom == 2:
                print("==========")
                print("*You hear ""HONK"" sound behind you!")
                print("Clown now HONK your ass, and you lost 3 hp.")
                print("==========")
                life = life - 3
        print flavorText[myItem]
        inventory[myItem] -= 1
def changeWeapon():
    print("Current weapon equipped: " + myWeapons[0])
    print ("Select weapon to equip from the list.")
    i = 1
    for weapon in myWeapons:
        print str(i) + ") " + weapon
        i += 1
    equip = int(raw_input("Equip:\n"))-1
    w = myWeapons.pop(equip)
    myWeapons.insert(0, w)

    print myWeapons[0] + " is equipped.\n"

def saveGame():
    savefile = open('save.sv', 'w')
    savefile.write('inventory = ' + str(inventory) + '\n')
    savefile.write('myWeapons = ' + str(myWeapons) + '\n')
    savefile.write('life = ' + str(life) + '\n')
    savefile.write('youAreHere = ' + str(youAreHere) + '\n')
    savefile.write('money = ' + str(money) + '\n')
    savefile.close()
    
def Shop():
    global money
    print('Welcome to the clown store!\nIn this store you can buy candy.\n')
    buyItem = input('1) Buy your candy(Price: 7 money).\n2)Get out of the shop.\n')
    if (buyItem == 1):
        if money > 7:
            goBuyItem = "Candy"
            inventory[goBuyItem] += 1
            money -= 7
            print("Candies treat!")
            time.sleep(4)
            os.system('cls')
        elif money < 7:
            print("You haven't enough money.")
            time.sleep(4)
            os.system('cls')
            Shop()
    elif (buyItem == 2):
        print("Ok.")
        time.sleep(4)
        os.system('cls')
        return 0
    else:
        time.sleep(4)
        os.system('cls')
        Shop()

print ("Author: " + author)
print (welcome)

print ("\nLook, a small horde of clowns  approaches! Take this crowbar and go bash some heads!")

ready = raw_input("Ready to fight?\n")

if (str.upper(ready) != "Y"):
    print "Too bad, this is Infinity Station. You better get ready.\n"
else:
    print "Lock and load!\n"

fightClowns(random.randrange(0, 4))
lootBodies()

print("Now let's go loot a room")
lootRoom()

print("You seem to be getting this on your own. Here's a candy bar to restore your health, and one for the road. \n")
inventory["Candy"] += 1

while (life > 0):
    time.sleep(4)
    os.system('cls')
    print("Life: " + str(life))
    action = raw_input("What would you like to do now?\n1) for find more clowns\n2)Loot more rooms\n3)Leave the station\n4)Check inventory\n5)Change Weapon\n6)Shop\n7)Save Game\n8)Load Game\n\n")
    if (action == "1"):
        fightClowns(random.randrange(0,5))
        if (life > 0) and clowns > 0:
            lootBodies()
        elif (life <= 0):
            break
    elif (action == "2"):
        lootRoom()
        time.sleep(4)
        os.system('cls')
    elif (action == "3"):
        leaveStation()
        time.sleep(4)
        os.system('cls')
    elif (action == "4"):
        checkInventory()
        time.sleep(4)
        os.system('cls')
    elif (action == "5"):
        changeWeapon()
        time.sleep(4)
        os.system('cls')
    elif (action == "6"):
        Shop()
        time.sleep(4)
        os.system('cls')
    elif (action == "7"):
        saveGame()
        time.sleep(4)
        os.system('cls')
    elif (action == "8"):
        savefile2 = open('save.sv', 'r')
        exec(savefile2.read())
        savefile2.close()
        time.sleep(4)
        os.system('cls')
    else:
        print("Invalid input!")

print("You died.")
time.sleep(4)



