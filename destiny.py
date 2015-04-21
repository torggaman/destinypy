

class character():
    def __init__(self):
        self.name = ""
        self.race = ""
        self.job = ""
        self.subjob = ""
        self.destination = ""
        self.currentmap = ""


class player(character):
    def __init__(self):
        character.__init__(self)
        self.state = ""
        self.health = 1
        self.defense = 1
        self.light = 1
        self.level = 1
        self.explevel = 1
        self.experience = 1
        self.attack = 1
        self.glimmer = 1
        self.moteoflight = 1
        self.vanguardmarks = 1
        self.commendations = 1
        self.made = 0
        self.primaryw = ""
        self.specialw = ""
        self.heavyw = ""
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
            self.status()
        elif status1 == "armor":
            print("Helmet: %s" % self.armorh)
            print("Chest: %s" % self.armorc)
            print("Legs: %s" % self.armorl)
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
            print(self.race)
            self.chooserace()
        elif selectrace == "Human":
            self.race = selectrace
        elif selectrace == "Awoken":
            self.race = selectrace
        elif selectrace == "Exo":
            self.race = selectrace
        else:
            self.chooserace()
        self.choosejob()

    def choosejob(self):
        print(job)
        selectjob = input("Choose a Class: ")
        if selectjob == "":
            self.choosejob()
        elif selectjob == "Titan":
            self.job = selectjob
        elif selectjob == "Hunter":
            self.job = selectjob
        elif selectjob == "Warlock":
            self.job = selectjob
        else:
            self.choosejob()
        self.choosesubjob()

    def choosesubjob(self):
        if self.job == "Titan":
            selectsubjob = input("Choose a Subclass 'Defender' or 'Striker': ")
            if selectsubjob == "Defender":
                self.subjob = selectsubjob
            elif selectsubjob == "Striker":
                self.subjob = selectsubjob
            else:
                self.choosesubjob()
        elif self.job == "Warlock":
            selectsubjob = input("Choose a Subclass 'Sunsinger' or 'Voidwalker': ")
            if selectsubjob == "Sunsinger":
                self.subjob = selectsubjob
            elif selectsubjob == "Voidwalker":
                self.subjob = selectsubjob
            else:
                self.choosesubjob()
        elif self.job == "Hunter":
            selectsubjob = input("Choose a Subclass 'Gunslinger' or 'Bladedancer': ")
            if selectsubjob == "Gunslinger":
                self.subjob = selectsubjob
            elif selectsubjob == "Bladedancer":
                self.subjob = selectsubjob
            else:
                self.choosesubjob()
        else:
            self.choosesubjob()
        self.charactercomplete()

    def charactercomplete(self):
        self.made += 1
        self.destination = "Earth"
        del Cmd['new game']
        Cmd['status'] = player.status
        Cmd['orbit'] = player.orbit
        Cmd['travel'] = player.travel
        Cmd['equip'] = player.equip
        Cmd['inventory'] = player.inventory

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
            else:
                print("You are already in orbit")
        else:
            print("Make a character first.")

    def travel(self):
        if self.made == 1:
            if self.destination == "Space":
                answer = input("Where would you like to go? \n %s: " % planets)
                if answer == "earth":
                    self.destination = "Earth"
                    self.currentmap = ""
                    print("Initiating Warp Drive")
                    print("Welcome to Earth")
                elif answer == "tower":
                    self.destination = "Tower"
                    self.currentmap = ""
                    Cmd['shop'] = player.shop
                    print("Initiating Warp Drive")
                    print("Welcome to the Tower")
                elif answer == "moon":
                    self.destination = "Moon"
                    self.currentmap = ""
                    print("Initiating Warp Drive")
                    print("Welcome to the Moon")
                elif answer == "venus":
                    self.destination = "Venus"
                    self.currentmap = ""
                    print("Initiating Warp Drive")
                    print("Welcome to Venus")
                elif answer == "mars":
                    self.destination = "Mars"
                    self.currentmap = ""
                    print("Initiating Warp Drive")
                    print("Welcome to Mars")
                else:
                    print(invalidinput)
            else:
                print("Go to Orbit first")
        else:
            print("Make a character first.")

    def inventory(self):
        print("%s glimmer" % self.glimmer)
        print("%s vanguard marks" % self.vanguardmarks)
        print("%s Motes of light" % self.moteoflight)
        print("Primary WeaponsL \n", primarywinv)
        print("Special Weapons: \n", specialwinv)
        print("Heavy Weapons: \n", heavywinv)
        print("Headgear: \n", armorhinv)
        print("Chest: \n", armorcinv)
        print("Legs: \n", armorlinv)

    def equip(self):
        print("What would you like to equip?")
        liste = input("weapon or armor: ")
        if liste == "weapon":
            liste = input("primary, special, or heavy? ")
            if liste == "primary":
                print("Choose a Primary weapon from below")
                print(primarywinv)
                equipweapon = input("Select One: ")
                if equipweapon == primarywinv:
                    if self.primaryw == "":
                        self.primaryw = equipweapon
                        primarywinv.remove(equipweapon)
                        print("Equipped: %s" % equipweapon)
                    else:
                        primarywinv.append(self.primaryw)
                        self.primaryw = equipweapon
                        primarywinv.remove(equipweapon)
                        print("Equipped: %s" % equipweapon)
                else:
                    print(invalidinput)
            elif liste == "special":
                print("Choose a Special weapon from below")
                print(specialwinv)
                equipweapon = input("Select One: ")
                if equipweapon == specialwinv:
                    if self.specialw == "":
                        self.specialw = equipweapon
                        specialwinv.remove(equipweapon)
                        print("Equipped: %s" % equipweapon)
                    else:
                        specialwinv.append(self.specialw)
                        self.specialw = equipweapon
                        specialwinv.remove(equipweapon)
                        print("Equipped: %s" % equipweapon)
                else:
                    print(invalidinput)
            elif liste == "heavy":
                print("Choose a Special weapon from below")
                print(heavywinv)
                equipweapon = input("Select One: ")
                if equipweapon == heavywinv:
                    if self.heavyw == "":
                        self.heavyw = equipweapon
                        heavywinv.remove(equipweapon)
                        print("Equipped: %s" % equipweapon)
                    else:
                        heavywinv.append(self.heavyw)
                        self.heavyw = equipweapon
                        heavywinv.remove(equipweapon)
                        print("Equipped: %s" % equipweapon)
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
                if armorhinv == equiparmor:
                    if self.armorh == "":
                        self.armorh = equiparmor
                        armorhinv.remove(equiparmor)
                    else:
                        armorhinv.append(self.armorh)
                        self.armorh = equiparmor
                        armorhinv.remove(equiparmor)
                else:
                    print(invalidinput)
            elif list1 == "chest":
                print("Choose which armor you want to equip")
                print(armorcinv)
                equiparmor = input("Select one: ")
                if armorcinv == equiparmor:
                    if self.armorc == "":
                        self.armorc = equiparmor
                        armorcinv.remove(equiparmor)
                    else:
                        armorcinv.append(self.armorc)
                        self.armorc = equiparmor
                        armorcinv.remove(equiparmor)
                else:
                    print(invalidinput)
            elif list1 == "legs":
                print("Choose which armor you want to equip")
                print(armorlinv)
                equiparmor = input("Select one: ")
                if armorlinv == equiparmor:
                    if self.armorl == "":
                        self.armorl = equiparmor
                        armorlinv.remove(equiparmor)
                    else:
                        armorlinv.append(self.armorl)
                        self.armorl = equiparmor
                        armorlinv.remove(equiparmor)
                else:
                    print(invalidinput)
            else:
                print(invalidinput)
        else:
            print(invalidinput)

    def explore(self):
        if self.destination == "Tower":
            print("Looks like there are some shops to visit")
        elif self.destination == "Earth":
            print("Lets explore Earth!")
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
        self.createcharacter()


class monster():
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


class armor():
    def __int__(self):
        self.name = ""
        self.job = ""
        self.defense = 1
        self.light = 1
        self.discipline = 1
        self.intellect = 1
        self.strength = 1


class weapon():
    def __init__(self):
        self.name = ""
        self.typew = ""
        self.guntype = ""
        self.attack = ""
        self.ammoclip = 1
        self.maxammo = 1
        self.rof = 1
        self.impact = 1
        self.range = 1
        self.stability = 1
        self.reload = 1


invalidinput = "Invalid input, please try again"
race = ["Human", "Awoken", "Exo", ]
job = ["Titan", "Hunter", "Warlock", ]
inventory2 = []
weaponinv = []
primarywinv = ['test1', ]
specialwinv = ['test1', ]
heavywinv = ['test1', ]
armorhinv = ['test1', ]
armorcinv = ['test1', ]
armorlinv = ['test1', ]
planets = ["tower", "earth", "moon", "venus", "mars", ]
weaponshop = {'Hawkmoon': 2000, }
armorhshop = {'VoG Head': 4000, }
armorcshop = {'VoG Chest': 3000, }
armorlshop = {'VoG Legs': 2000, }


p = player()

print("Welcome to Destiny")
print("Type: help \nfor a list of commands")

Cmd = {
    'help': player.help1,
    'new game': player.newgame,
    }
Cmd2 = {
    'status': player.status,
    'create character': player.createcharacter,
    'help': player.help1,
    'travel': player.travel,
    'inventory': player.inventory,
    'equip': player.equip,
    'explore': player.explore,
    'glimmer': player.giveglimmer,
    'go to orbit': player.orbit,
    'xp': player.giveexp,
    'take damage': player.takedamage,
    }
while p.health > 0:
    line = input("> ")
    args = line.split()
    if len(args) > 0:
        commandFound = False
        for c in Cmd.keys():
            if args[0] == c[:len(args[0])]:
                Cmd[c](p)
                commandFound = True
                break
        if not commandFound:
            print("%s doesn't understand the suggestion." % p.name)

if p.health <= 0:
    print("You were killed in battle")
    print("Game Over")