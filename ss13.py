import random

author = 'aftonweb'
welcome = 'Welcome to the Hell!'

life = 35

clowns = 0

hit = 0

clownattack = random.randrange(0, 4)

hitMultiplier = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 1]

weapon = {"Crowbar": 1, "Stechkin Pistol": 2, "Energy Crossbow": 3, "Energy Sword": 4, "Revolver": 5, "Balloon": 7}

supplies = ["Candy", "Cup Ramen", "Chips", "4no Raisins", "Dr.Gibb", "Baguette"]

inventory = {"Chips": 5,
             "Candy": 1,
             "Cup Ramen": 0,
             "4no Raisins": 0,
             "Dr.Gibb": 0,
             "Baguette": 0
             }

flavorText =             {"Candy": "Nougat love it or hate it",
			  "Cup Ramen": "A taste that reminds you of your school years.",
			  "Chips": "Commander Riker's What-The-Crisps",
			  "4no Raisins": "Best Raisins in the universe. Not sure why.",
			  "Dr.Gibb": "A delicious mixture of 42 different flavors.",
			  "Baguette": "Bon appetit!"
			 }
myWeapons = ["Crowbar"]

stations = ["Infinity Station", "Soviet Station", "Tau Ceti Station", "Animus Station"]
youAreHere = 0

def fightClowns(clowns):
    global life
    global hit
    
    if clowns != 0:
        print(str(clowns) + " clowns stagger towards you. Ready your " + str.lower(myWeapons[0]) + "!\n")
        attack = raw_input("Attack, or Run? (A for attack, R for run)\n")
        if (str.upper(attack) == "A"):
            print(str(clowns) + " clowns attacked you!")
            life = life - clownattack*clowns
            hit = (hitMultiplier[random.randrange(0, len(hitMultiplier))]*weapon[myWeapons[0]])
            if hit != 0:
                print("You successfully killed them!")
                print("Your life is now: " + str(life))
            if (hit == 0):
                print("That was a lucky miss. Next time you should attack! (You successfully runned)")
                return 0
    elif clowns == 0:
         print ("But Nobody Came!")
    else:
        hit = (hitMultiplier[random.randrange(0, len(hitMultiplier))]*weapon[myWeapons[0]])
        if hit > 0:
            life = life - clownattack
        print (str(clowns) + " attack you, but you killed them\n" "Life health is now " + str(life))


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
        if clowns != 0:
            attack = raw_input("Attack or Run? (A/R)\n")
            if str.upper(attack) == "A":
                hit = clowns * (hitMultiplier[random.randrange(0, len(hitMultiplier)-4)])
                life = life - hit
                print (str(clowns) + " clowns attacked you, and you killed them with your " + str(myWeapons[0]) + "\nLife health is now " + str(life))
            else:
                runAway = True
                print("You run away quietly, with no cool stuff.")
        else:
            print ("The room is empty of clowns, but full of cool stuff...")
        if (runAway != True):
            takeItem = raw_input("You found a " + foundItem + "\nEquip? (Y/N)")
            takeWeapon = raw_input("Cool! You found a " + foundWeapon + "\nEquip? (Y/N)")
            if str.upper(takeWeapon) == "Y": myWeapons.insert(0, foundWeapon)
            if str.upper(takeItem) == "Y": inventory[foundItem] += 1
            print ("Current weapon: " + str(myWeapons[0]))
            print ("Destruction power: " + str(weapon[myWeapons[0]]))
            print("Inventory:\n==========")
            for item in inventory:
                if(inventory[item] > 0):
                    print (item + ": " + str(inventory[item]))
            print("\n")
def lootBodies():
    global life
    global clownattack
    loot = raw_input("On your way you found the bodies. Would you like to loot the bodies? (Y/N)\n")
    if (str.upper(loot) == "Y"):
        if (random.randrange(0,9)>7):
            print("A clown was not yet dead!\n")
            hit = 1 * hitMultiplier[random.randrange(0, len(hitMultiplier))]
            life = life - clownattack
            print("Clown did " + str(hit) + " damage to you.\nYour life is " + str(life))
        else:
            foundItem = supplies[random.randrange(0, len(inventory)-1)]
            print("You found a " + foundItem)
            equip = raw_input("Equip? (Y/N)")
            if (str.upper(equip) == "Y"):
                inventory[foundItem] += 1
                print("Inventory: " + str(inventory))
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
def checkInventory():
    global life
    global flavorText
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
    

print ("Author: " + author)
print (welcome)

print ("\nLook, a small horde of clowns  approaches! Take this crowbar and go bash some heads!")

ready = raw_input("Ready to fight?\n")

if (str.upper(ready) != "Y"):
    print "Too bad, this is Infinity Station. You better get ready.\n"
else:
    print "Lock and load!\n"

fightClowns(3)
lootBodies()

print("Now let's go loot a room")
lootRoom()

print("You seem to be getting this on your own. Here's a candy bar to restore your health, and one for the road. \n")
inventory["Candy"] += 1

while (life > 0):
    print("Life: " + str(life))
    action = raw_input("What would you like to do now?\n1)Find more clowns\n2)Loot more rooms\n3)Leave the station\n4)Check inventory\n5)Change Weapon\n\n")
    if (action == "1"):

        fightClowns(random.randrange(0,10))
        if (life > 0) and clowns !=0:
            lootBodies()
        elif (life <= 0):
            break 
    elif (action == "2"):
        lootRoom()
    elif (action == "3"):
        leaveStation()
    elif (action == "4"):
        checkInventory()
    elif (action == "5"):
        changeWeapon()
    else:
        print("Invalid input!")

print("You died.")


