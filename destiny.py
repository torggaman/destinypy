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
        self.status = ""
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
        self.armor = ""

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
        if self.made == 1:
            print("Name: %s" % self.name)
            print("Race: %s" % self.race)
            print("Class: %s" % self.job)
            print("Subclass: %s" % self.subjob)
            print("Level: %s" % self.explevel)
            print("Primary: %s" % self.primaryw)
        else:
            print("Please make a character.")

    def createcharacter(self):
        if self.made == 0:
            self.name = input("Character Name: ")
            self.chooserace()
        else:
            print("You already have a character.")

    def chooserace(self):
        print(race)
        self.race = input("Choose a Race: ")
        self.choosejob()

    def choosejob(self):
        print(job)
        self.job = input("Choose a Class: ")
        self.choosesubjob()

    def choosesubjob(self):
        if self.job == "Titan":
            self.subjob = input("Choose a Subclass 'Defender' or 'Striker': ")
        elif self.job == "Warlock":
            self.subjob = input("Choose a Subclass 'Sunsinger' or 'Voidwalker': ")
        elif self.job == "Hunter":
            self.subjob = input("Choose a Subclass 'Gunslinger' or 'Bladedancer': ")
        self.made += 1
        self.destination = "Earth"
        del Cmd['new game']
        Cmd['go to orbit'] = player.orbit
        Cmd['travel'] = player.travel


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
        print(inventory2)
        print("%s glimmer" % self.glimmer)
        print("%s vanguard marks" % self.vanguardmarks)
        print("%s Motes of light" % self.moteoflight)

    def equip(self):
        if self.made != 1:
            print("Create a character first.")
        else:
            print("What would you like to equip?")
            liste = input("Weapon or Armor: ")
            if liste == "Weapon":
                print("Choose a weapon from below")
                print(weaponinv)
                equipweapon = input("Select One: ")
                if self.primaryw == "":
                    self.primaryw = equipweapon
                    weaponinv.remove(equipweapon)
                else:
                    weaponinv.append(self.primaryw)
                    self.primaryw = equipweapon
                    weaponinv.remove(equipweapon)
            elif liste == "Armor":
                print("Choose which armor you want to equip")
                print(armorinv)
                equiparmor = input("Select one: ")
                if self.armor == "":
                    self.armor = equiparmor
                    armorinv.remove(equiparmor)
                else:
                    armorinv.append(self.armor)
                    self.armor = equiparmor
                    armorinv.remove(equiparmor)
            else:
                print(invalidinput)

    def explore(self):
        if self.made == 0:
            print("Make a character first.")
        else:
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
                print(armorshop)
                purchase = input("Please choose a armor set: ")
                if self.glimmer >= armorshop[purchase]:
                    self.glimmer -= armorshop[purchase]
                    armorinv.append(purchase)
                else:
                    print("You do not have enough glimmer for %s" % purchase)
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
        print("They travel quite a distance before walking up /na hill to discover a larger floating orb")
        t1 = input()
        print("Destiny")
        print("We called it, The Traveler, and its arrival changed us forever.")
        print("Great cities were built on Mars and Venus, Mercury became a garden world, human life-span tripled,")
        print("it was a time of mirecles.")
        print("We stared out at the galaxy and knew that it was our destiny to walk the light of other stars,")
        print("but the Traveler had an enemy.")
        t1 = input()
        print("A Darkness, which had hunted it for eons across the black gulf of space.")
        print("Centuries after our Golden Age began, this Darkness found us and that was the end of everything.")
        print("But it was also a beginning./n")
        self.createcharacter()

invalidinput = "Invalid input, please try again"
race = ["Human", "Awoken", "Exo", ]
job = ["Titan", "Hunter", "Warlock", ]
inventory2 = []
weaponinv = []
armorinv = []
planets = ["tower", "earth", "moon", "venus", "mars", ]
weaponshop = {'Hawkmoon': 2000, }
armorshop = {'VoG set': 4000, }

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