from random import randint


class Character():
    def __init__(self):
        self.name = ""
        self.race = ""
        self.job = ""
        self.subjob = ""
        self.destination = ""
        self.currentmap = ""



class Missions():
    def __int__(self):
        self.currentmission = ""
        self.completedmission = []


class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.state = ""
        self.enemy = "Dreg"
        self.health = 1
        self.defense = 1
        self.light = 1
        self.level = 1
        self.explevel = 1
        self.experience = 1
        self.attack = 1
        self.intellect = 1
        self.discipline = 1
        self.strength = 1
        self.glimmer = 1
        self.moteoflight = 1
        self.vanguardmarks = 1
        self.commendations = 1
        self.made = 0
        self.primaryw = ""
        self.primaryammo = 1
        self.primarymaxammo = 1
        self.primaryconsumption = 1
        self.specialw = ""
        self.specialammo = 1
        self.specialmaxammo = 1
        self.heavyw = ""
        self.heavyammo = 1
        self.heavymaxammo = 1
        self.armorh = ""
        self.armorc = ""
        self.armorl = ""

    def levelup(self):
        if self.experience >= 1000:
            if self.explevel < 20:
                self.explevel += 1
                self.experience -= 1000
                print("Congratulations \nYou gained a level!")
                if self.experience >= 1000:
                    self.levelup()
        elif self.explevel >= 20:
                self.moteoflight += 1
                self.experience -= 1000
                print("You gained a 'Mote of Light'")
                if self.experience >= 1000:
                    self.levelup()

    def status(self):
        print("Name: %s" % self.name)
        print("Race: %s" % self.race)
        print("Class: %s" % self.job)
        print("Subclass: %s" % self.subjob)
        print("Level: %s" % self.explevel)
        print("'weapons' 'armor' or close'")
        status1 = input("Select one: ")
        if status1 == "weapons":
            print("Primary: %s" % self.primaryw)
            print("Special: %s" % self.specialw)
            print("Heavy: %s" % self.heavyw)
            print("\n")
            input("Press Enter to continue")
            print("\n")
            self.status()
        elif status1 == "armor":
            print("Helmet: %s" % self.armorh)
            print("Chest: %s" % self.armorc)
            print("Legs: %s" % self.armorl)
            print("\n")
            input("Press Enter to continue")
            print("\n")
            self.status()
        else:
            print("Menu closed")

    def createcharacter(self):
            self.name = input("Character Name: ")
            self.chooserace()

    def chooserace(self):
        print(race)
        selectrace = input("Choose a Race: ")
        if selectrace == "":
            print("Make sure you type it as displayed")
        elif selectrace == "Human":
            self.race = selectrace
            self.choosejob()
        elif selectrace == "Awoken":
            self.race = selectrace
            self.choosejob()
        elif selectrace == "Exo":
            self.race = selectrace
            self.choosejob()
        else:
            print("Make sure you type it as displayed")

    def choosejob(self):
        print(job)
        selectjob = input("Choose a Class: ")
        if selectjob == "":
            print("Make sure you type it as displayed")
        elif selectjob == "Titan":
            self.job = selectjob
            self.choosesubjob()
        elif selectjob == "Hunter":
            self.job = selectjob
            self.choosesubjob()
        elif selectjob == "Warlock":
            self.job = selectjob
            self.choosesubjob()
        else:
            print("Make sure you type it as displayed")

    def choosesubjob(self):
        if self.job == "Titan":
            selectsubjob = input("Choose a Subclass 'Defender' or 'Striker': ")
            if selectsubjob == "Defender":
                self.subjob = selectsubjob
                self.charactercomplete()
            elif selectsubjob == "Striker":
                self.subjob = selectsubjob
                self.charactercomplete()
            else:
                print("Make sure you type it as displayed")
        elif self.job == "Warlock":
            selectsubjob = input("Choose a Subclass 'Sunsinger' or 'Voidwalker': ")
            if selectsubjob == "Sunsinger":
                self.subjob = selectsubjob
                self.charactercomplete()
            elif selectsubjob == "Voidwalker":
                self.subjob = selectsubjob
                self.charactercomplete()
            else:
                print("Make sure you type it as displayed")
        elif self.job == "Hunter":
            selectsubjob = input("Choose a Subclass 'Gunslinger' or 'Bladedancer': ")
            if selectsubjob == "Gunslinger":
                self.subjob = selectsubjob
                self.charactercomplete()
            elif selectsubjob == "Bladedancer":
                self.subjob = selectsubjob
                self.charactercomplete()
            else:
                print("Make sure you type it as displayed")
        else:
            print("Make sure you type it as displayed")

    def charactercomplete(self):
        self.made += 1
        self.destination = "Earth"
        del Cmd['create character']
        """
        Cmd['status'] = Player.status
        Cmd['equip'] = Player.equip
        Cmd['inventory'] = Player.inventory
        """
        Cmd['menu'] = Player.menu
        Cmd['travel'] = Player.travel
        Cmd['orbit'] = Player.orbit
        Cmd['debug'] = Player.debugcommand

    def help1(self):
        print(Cmd.keys())

    def orbit(self):
        if self.made == 1:
            if self.destination != "Space":
                print("Do you want to return to orbit?")
                goorbit = input("'yes' or 'no': ")
                if goorbit == "yes":
                    print("Your ship gracefully swoops down and picks you up.")
                    self.destination = "Space"
                    if Cmd.keys() == 'shop':
                        del Cmd['shop']
                    elif Cmd.keys() == 'explore':
                        del Cmd['explore']
            else:
                print("You are already in orbit")
        else:
            print("Make a character first.")

    def travel(self):
        if self.made == 1:
            if self.destination == "Space":
                print(planets)
                answer = input("Where would you like to go? ")
                if answer == "earth":
                    self.destination = "Earth"
                    self.currentmap = ""
                    Cmd['explore'] = Player.explore
                    print("Initiating Warp Drive")
                    print("Welcome to Earth")
                elif answer == "tower":
                    self.destination = "Tower"
                    self.currentmap = ""
                    Cmd['shop'] = Player.shop
                    Cmd['explore'] = Player.explore
                    print("Initiating Warp Drive")
                    print("Welcome to the Tower")
                elif answer == "moon":
                    self.destination = "Moon"
                    self.currentmap = ""
                    Cmd['explore'] = Player.explore
                    print("Initiating Warp Drive")
                    print("Welcome to the Moon")
                elif answer == "venus":
                    self.destination = "Venus"
                    self.currentmap = ""
                    Cmd['explore'] = Player.explore
                    print("Initiating Warp Drive")
                    print("Welcome to Venus")
                elif answer == "mars":
                    self.destination = "Mars"
                    self.currentmap = ""
                    Cmd['explore'] = Player.explore
                    print("Initiating Warp Drive")
                    print("Welcome to Mars")
                else:
                    print(invalidinput)
            else:
                print("Go to Orbit first")
        else:
            print("Make a character first.")

    def inventory(self):
        print("%d glimmer, %d vanguard marks, %d Motes of light" % (self.glimmer, self.vanguardmarks, self.moteoflight))
        print("Primary Weapons: \n", primarywinv)
        print("Special Weapons: \n", specialwinv)
        print("Heavy Weapons: \n", heavywinv)
        print("Headgear: \n", armorhinv)
        print("Chest: \n", armorcinv)
        print("Legs: \n", armorlinv)
        list1 = input("Press enter to continue...")
        print("")

    def equip(self):
        print("What would you like to equip?")
        liste = input("'weapon', 'armor' or 'close': ")
        if liste == "weapon":
            liste = input("primary, special, or heavy? ")
            if liste == "primary":
                print("Choose a Primary weapon from below")
                print(primarywinv)
                equipweapon = input("Select One: ")
                if equipweapon in primarywinv:
                    if self.primaryw == "":
                        self.primaryw = equipweapon
                        primarywinv.remove(equipweapon)
                        print("Equipped: %s" % equipweapon)
                    else:
                        primarywinv.append(self.primaryw)
                        self.primaryw = equipweapon
                        primarywinv.remove(equipweapon)
                        print("Equipped: %s" % equipweapon)
                    print("\n")
                    self.equip()
                else:
                    print("Make sure you typed correctly")
            elif liste == "special":
                print("Choose a Special weapon from below")
                print(specialwinv)
                equipweapon = input("Select One: ")
                if equipweapon in specialwinv:
                    if self.specialw == "":
                        self.specialw = equipweapon
                        specialwinv.remove(equipweapon)
                        print("Equipped: %s" % equipweapon)
                    else:
                        specialwinv.append(self.specialw)
                        self.specialw = equipweapon
                        specialwinv.remove(equipweapon)
                        print("Equipped: %s" % equipweapon)
                    print("\n")
                    self.equip()
                else:
                    print(invalidinput)
            elif liste == "heavy":
                print("Choose a Special weapon from below")
                print(heavywinv)
                equipweapon = input("Select One: ")
                if equipweapon in heavywinv:
                    if self.heavyw == "":
                        self.heavyw = equipweapon
                        heavywinv.remove(equipweapon)
                        print("Equipped: %s" % equipweapon)
                    else:
                        heavywinv.append(self.heavyw)
                        self.heavyw = equipweapon
                        heavywinv.remove(equipweapon)
                        print("Equipped: %s" % equipweapon)
                    print("\n")
                    self.equip()
                else:
                    print(invalidinput)
            else:
                print(invalidinput)
        elif liste == "armor":
            list1 = input("head, chest, or legs? ")
            if list1 == "head":
                print("Choose which armor you want to equip")
                print(armorhinv)
                equiparmor = input("Select one: ")
                if equiparmor in armorhinv:
                    if self.armorh == "":
                        self.armorh = equiparmor
                        armorhinv.remove(equiparmor)
                    else:
                        armorhinv.append(self.armorh)
                        self.armorh = equiparmor
                        armorhinv.remove(equiparmor)
                    print("\n")
                    self.equip()
                else:
                    print(invalidinput)
            elif list1 == "chest":
                print("Choose which armor you want to equip")
                print(armorcinv)
                equiparmor = input("Select one: ")
                if equiparmor in armorcinv:
                    if self.armorc == "":
                        self.armorc = equiparmor
                        armorcinv.remove(equiparmor)
                    else:
                        armorcinv.append(self.armorc)
                        self.armorc = equiparmor
                        armorcinv.remove(equiparmor)
                    print("\n")
                    self.equip()
                else:
                    print(invalidinput)
            elif list1 == "legs":
                print("Choose which armor you want to equip")
                print(armorlinv)
                equiparmor = input("Select one: ")
                if equiparmor in armorlinv:
                    if self.armorl == "":
                        self.armorl = equiparmor
                        armorlinv.remove(equiparmor)
                    else:
                        armorlinv.append(self.armorl)
                        self.armorl = equiparmor
                        armorlinv.remove(equiparmor)
                    print("\n")
                    self.equip()
                else:
                    print(invalidinput)
            else:
                print(invalidinput)
        elif liste == "close":
            print("Menu closed")
        else:
            print(invalidinput)

    def explore(self):
        if self.destination == "Tower":
            if self.currentmap == "Tower Watch":
                print("Current Area: ", self.currentmap)
                print("Tower Hanger, Tower North, Traveler's Walk, or Hall of Guardians")
                list1 = input("Choose a location: ")
                self.currentmap = list1
            elif self.currentmap == "Tower Hangar":
                print("Current Area: ", self.currentmap)
                print("Return?")
                list1 = input("yes or no: ")
                if list1 == "yes":
                    self.currentmap = "Tower Watch"
            elif self.currentmap == "Tower North":
                print("Current Area: ", self.currentmap)
                print("Return?")
                list1 = input("yes or no: ")
                if list1 == "yes":
                    self.currentmap = "Tower Watch"
            elif self.currentmap == "Traveler's Walk":
                print("Current Area: ", self.currentmap)
                print("Return?")
                list1 = input("yes or no: ")
                if list1 == "yes":
                    self.currentmap = "Tower Watch"
            elif self.currentmap == "Hall of Guardians":
                print("Current Area: ", self.currentmap)
                print("Return?")
                list1 = input("yes or no: ")
                if list1 == "yes":
                    self.currentmap = "Tower Watch"
        elif self.destination == "Earth":
            if self.currentmap == "The Steppes":
                print(self.currentmap)
            elif self.currentmap == "Mothyards":
                print(self.currentmap)
            elif self.currentmap == "Lunar Complex":
                print(self.currentmap)
            elif self.currentmap == "Skywatch":
                print(self.currentmap)
            elif self.currentmap == "Terrestrial Complex":
                print(self.currentmap)
            elif self.currentmap == "Forgotten Shore":
                print(self.currentmap)
            elif self.currentmap == "Bunker RAS-2":
                print(self.currentmap)
            elif self.currentmap == "The Grottos":
                print(self.currentmap)
            elif self.currentmap == "Refinery":
                print(self.currentmap)
            elif self.currentmap == "The Blast":
                print(self.currentmap)
            elif self.currentmap == "Devils' lair":
                print(self.currentmap)
            elif self.currentmap == "Rocket Yard":
                print(self.currentmap)
            elif self.currentmap == "The Divide":
                print(self.currentmap)
            elif self.currentmap == "The Breach":
                print(self.currentmap)
            elif self.currentmap == "The Gateway":
                print(self.currentmap)
            elif self.currentmap == "Dock 13":
                print(self.currentmap)
        elif self.destination == "Moon":
            print("I'm on the Moon!")
        elif self.destination == "Venus":
            print("I'm on Venus?")
        elif self.destination == "Mars":
            print("I've made it to Mars")
        else:
            print("travel to another destination.")

    def shop(self):
        if self.glimmer >= 0:
            print("What would you like?")
            shopping = input("weapons or armor: ")
            if shopping == "weapons":
                print(weaponshop)
                purchase1 = input("Please choose a weapon: ")
                if self.glimmer >= weaponshop[purchase1]:
                    self.glimmer -= weaponshop[purchase1]
                    weaponinv.append(purchase1)
                    print("Thank you for shopping")
                else:
                    print("You do not have enough glimmer for %s" % purchase1)
            elif shopping == "armor":
                list1 = input("head, chest, or legs?")
                if list1 == "head":
                    print(armorhshop)
                    purchase = input("Please choose a armor set: ")
                    if self.glimmer >= armorhshop[purchase]:
                        self.glimmer -= armorhshop[purchase]
                        armorhinv.append(purchase)
                    else:
                        print("You do not have enough glimmer for %s" % purchase)
                elif list1 == "chest":
                    print(armorcshop)
                    purchase = input("Please choose a armor set: ")
                    if self.glimmer >= armorcshop[purchase]:
                        self.glimmer -= armorcshop[purchase]
                        armorcinv.append(purchase)
                    else:
                        print("You do not have enough glimmer for %s" % purchase)
                elif list1 == "legs":
                    print(armorlshop)
                    purchase = input("Please choose a armor set: ")
                    if self.glimmer >= armorlshop[purchase]:
                        self.glimmer -= armorlshop[purchase]
                        armorlinv.append(purchase)
                    else:
                        print("You do not have enough glimmer for %s" % purchase)
                else:
                    print(invalidinput)
            else:
                print(invalidinput)
        else:
            print("You should gather more glimmer")

    def giveglimmer(self):
        print("How much glimmer do you want? ")
        glimmer2 = input()
        if glimmer2.isdecimal():
            self.glimmer += int(glimmer2)
            print("%s glimmer has been added to your account" % glimmer2)
        else:
            print("Not a number")
            print("%s glimmer has been added to your account" % glimmer2)

    def view(self):
        if self.destination == "Tower":
            print("You look at the view from the Tower.")

    def debugcommand(self):
        print("what command do you want to us?")
        list1 = input("Exp, Damage, Glimmer? ")
        if list1 == "Exp":
            self.giveexp()
        elif list1 == "Damage":
            self.takedamage()
        elif list1 == "Glimmer":
            self.giveglimmer()
        else:
            print(invalidinput)

    def giveexp(self):
        print("How much experience?")
        exp = input()
        if exp.isdecimal():
            self.experience += int(exp)
        else:
            print(invalidinput)
        self.levelup()

    def takedamage(self):
        dealdamage = input("How much damage do you want to deal? ")
        if dealdamage.isdecimal():
            self.health -= int(dealdamage)
        else:
            print(invalidinput)

    def newgame(self):
        print("Activision")
        t1 = input()
        print("Bungie")
        t1 = input()
        print("A ship starts to enter the atmosphere of a red planet")
        print("Three explorers disembark from the craft")
        t1 = input()
        print("The Planet Mars")
        print("The explorers check and adjust their gear")
        print("They begin setting out to look for something")
        print("They travel quite a distance before walking up")
        print("a hill to discover a larger floating orb")
        t1 = input()
        print("Destiny")
        t1 = input()
        print("We called it, The Traveler, and its arrival changed us forever.")
        print("Great cities were built on Mars and Venus, Mercury became a garden world, ")
        print("human life-span tripled, it was a time of miracles.")
        print("We stared out at the galaxy and knew that it was our destiny")
        print("to walk the light of other stars, but the Traveler had an enemy.")
        t1 = input()
        print("A Darkness, which had hunted it for eons across the black gulf of space.")
        print("Centuries after our Golden Age began, this Darkness found us ")
        print("and that was the end of everything.")
        print("But it was also a beginning. \n")
        del Cmd['new game']
        Cmd['create character'] = Player.createcharacter
        self.createcharacter()

    def search(self):
        if self.destination != "Space":
            if self.destination != "Tower":
                self.state = "fight"
                if self.state == "fight":
                    self.battle()
            else:
                print("Travel to a destination")
        else:
            print("Travel to a destination")

    def battle(self):
        if self.state == "fight":
            print("An enemy has appeared")
        print("You have engaged the enemy")

    def practice(self):
        monster = Practicemonster(Dreg, 10, 5)
        if monster.health <= 0:
            print("You have destroyed the enemy.")
        else:
            print("Hello")
            print("[1]Primary, [2]Special, [3]Heavy, [4]Status, [5]Reload")
            action = input("What would you like to do? ")
            if int(action) == 1:
                if self.primaryammo >= self.primaryconsumption:
                    print("You fire your weapon at the Enemy")
                    totalattack = randint(self.attack, self.attack + self.level)
                    print("You dealt %d to the Enemy" % totalattack)
                    monster.health -= int(totalattack)
                    self.primaryammo -= 1
                    self.practice()
                else:
                    print("You need to reload")
                    self.practice()
            elif action == "4":
                print("%s has %d health left" % (monster.name, monster.health))
                print("Primary Weapon: %d / %d" % (self.primaryammo, self.primarymaxammo))
                self.practice()
            elif action == "5":
                print("You reload your weapon")
                self.primaryammo = self.primarymaxammo
                self.practice()

        """
        if monster1.status != "dead":
            if self.state != "fight":
                print("What would you like to fight?")
                print(monsterlist)
                monsterselect = input("Select one: ")
                if monsterselect in monsterlist:
                    self.state = "fight"
                    monster = monsterselect
                    print("A %s has appeared" % monster)
                    print("What would you like to do? \n", actions)
                    list1 = input("Select one: ")
                    if list1 == "shoot":
                        print("pewpew")
                        monster1.health -= self.attack
                        if monster1.health < 1:
                            monster1.state = "dead"
                            print("%s has fallen" % monster1.subclass)
                    elif list1 == "grenade":
                        print("Tossing grenade")
                    elif list1 == "super":
                        print("Super coming up")
                    elif list1 == "melee":
                        print("Welcome to earf!")
                    self.practice()
                else:
                    print("Check spelling")
            else:
                print("What would you like to do? \n", actions)
                list1 = input("Select one: ")
                if list1 == "shoot":
                    print("pewpew")
                    monster1.health -= self.attack
                    if monster1.health < 1:
                        monster1.status = "dead"
                        self.state = ""
                        print("%s has fallen" % monster1.subclass)
                        self.practice()
                    else:
                        self.practice()
        elif monster1.status == "dead":
            monster1.status = "Normal"
            monster1.health += monster1.healthmax
            print("The enemy has died")
            print("You gained %d experience" % monster1.exp)
            print("You gained %d glimmer" % monster1.glimmer)
            self.glimmer += monster1.glimmer
            self.experience += monster1.exp
            """

    def inspect(self):
        print(options)
        list1 = input("What would you like to inspect? ")
        if list1 == "weapon":
            print("'primary', 'special', or 'heavy' ")
            list1 = input("Which type of weapon do you want to inspect? ")
            if list1 == "primary":
                print("Currently Equipped: %s" % self.primaryw)
                print("Primary Weapon Inventory")
                print(primarywinv)
                list1 = input("Which would you like to inspect? ")
                if list1 in self.primaryw or primarywinv:
                    for x in list1.values():
                        print("Name: %s" % x('name'))
                        print("Attack: %d" % x('attack'))
                    """
                    print("Attack: %d" % list1.values('Attack'))
                    print("Range: %d" % list1.get('Range'))
                    print("Impact: %d" % list1.get('Impact'))
                    print("Rate of Fire: %d" % list1.get('Rate of Fire'))
                    print("Reload: %d" % list1.get('Reload'))
                    print("Stability: %d" % list1.get('Stability'))
                    print("Max Magazine Size: %d" % list1.get('Max Magazine'))
                    """
                else:
                    print("Please check the spelling")
            elif list1 == "special":
                print()
            elif list1 == "heavy":
                print()
            else:
                print("Make sure you typed correctly")
        elif list1 == "armor":
            print("'head', 'chest' or 'legs' ")
            list1 = input("Which type of armor do you want to inspect? ")
            if list1 == "head":
                print()
            elif list1 == "chest":
                print()
            elif list1 == "legs":
                print()
            else:
                print("Make sure you typed correctly")
        else:
            print("Make sure you typed correctly")

    def menu(self):
        print("Menu Opened")
        print("What would you like to do?")
        list1 = input("'inventory', 'equip', 'status', 'inspect', or 'close'? ")
        if list1 == "inventory":
            self.inventory()
        elif list1 == "equip":
            self.equip()
        elif list1 == "status":
            self.status()
        elif list1 == "close":
            print("Menu closed")
        elif list1 == "inspect":
            self.inspect()
        else:
            print("Make sure you typed correctly")


class Monster():
    def __init__(self):
        self.monsterrace = ""
        self.subclass = ""
        self.health = 1
        self.defense = 1
        self.attack = 1
        self.level = 1
        self.status = "Normal"
        self.loot = []
        self.glimmer = 1


class Dreg(Monster):
    def __init__(self):
        Monster.__init__(self)
        self.monsterrace = "Fallen"
        self.subclass = "Dreg"
        self.level = 1
        self.health = 1
        self.healthmax = (1 * self.level)
        self.defense = (1 + self.level)
        self.attack = (1 + self.level)
        self.status = "Normal"
        self.exp = 100*self.level
        self.glimmer = 25*self.level

class Practicemonster():
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack


class Armor():
    def __int__(self):
        self.name = ""
        self.job = ""
        self.defense = 1
        self.light = 1
        self.discipline = 1
        self.intellect = 1
        self.strength = 1


class Primary():
    def __init__(self):
        self.typew = "Primary"


class Weapon():
    def __init__(self):
        self.name = ""
        self.typew = ""
        self.guntype = ""
        self.attack = 1
        self.ammoclip = 1
        self.maxammo = 1
        self.rof = 1
        self.impact = 1
        self.range = 1
        self.stability = 1
        self.reload = 1

"""
class testweapon(Primary):
    def __init__(self):
        Primary.__init__(self)
        self.name = "Test Weapon"
        self.guntype = "Hand Cannon"
        self.attack = 1
        self.ammoclip = 10
        self.maxammo = 10
        self.rof = 1
        self.impact = 1
        self.range = 1
        self.stability = 1
        self.reload = 1
"""

options = ['weapon', 'armor', 'close']
invalidinput = "Invalid input, please try again"
race = ["Human", "Awoken", "Exo", ]
job = ["Titan", "Hunter", "Warlock", ]
currentmission = []
completedmission = []
inventory2 = []
weaponinv = []
primarywinv = ["test1", "testweapon", ]
specialwinv = ["test1", ]
heavywinv = ["test1", ]
armorhinv = ["test1", ]
armorcinv = ["test1", ]
armorlinv = ["test1", ]
planets = ["tower", "earth", "moon", "venus", "mars", ]
weaponshop = {'Hawkmoon': 2000, }
armorhshop = {'VoG Head': 4000, }
armorcshop = {'VoG Chest': 3000, }
armorlshop = {'VoG Legs': 2000, }

monsterlist = ['Dreg', ]
actions = ['shoot', 'grenade', 'Super', 'melee']
monster1 = Dreg()

testweapon = {
    'name': "Test Weapon",
    'attack': 10,
    'range': 1,
    'impact': 1,
    'rof': 1,
    'reload': 1,
    'stability': 1,
    'Current Magazine': 1,
    'Max Magazine': 1,
    }

p = Player()

print("Welcome to Destiny")
print("Type: help \nfor a list of commands")

Cmd2 = {
    'help': Player.help1,
    'new game': Player.newgame,
    }

Cmd = {
    'status': Player.status,
    'create character': Player.createcharacter,
    'help': Player.help1,
    'travel': Player.travel,
    'inventory': Player.inventory,
    'equip': Player.equip,
    'explore': Player.explore,
    'glimmer': Player.giveglimmer,
    'go to orbit': Player.orbit,
    'xp': Player.giveexp,
    'take damage': Player.takedamage,
    'debug': Player.debugcommand,
    'search': Player.search,
    'new game': Player.newgame,
    'view': Player.view,
    'shop': Player.shop,
    'inspect': Player.inspect,
    'practice': Player.practice,
    }

"""
while p.health > 0:
    line = input("> ")
    arg = line.replace(" ", "")
    if len(arg) > 0:
        commandFound = False
        for c in Cmd.keys():
            if arg[0] == c[:len(arg[0])]:
                print(arg)
                Cmd[c](p)
                commandFound = True
                break
        if not commandFound:
            print("%s doesn't understand the suggestion." % p.name)
"""

while p.health > 0:
    line = input("> ")
    if len(line) > 0:
        commandFound = False
        for c in Cmd.keys():
            if line == c:
                Cmd[c](p)
                commandFound = True
                break
        if not commandFound:
            print(invalidinput)


if p.health <= 0:
    print("You were killed in battle")
    print("Game Over")