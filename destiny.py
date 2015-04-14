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
        if self.experience >= 1000 & self.explevel:
            self.explevel += 1
            self.experience -= 1000
        self.attack = 1
        self.glimmer = 1
        self.vanguardmarks = 1
        self.commendations = 1
        self.made = 0

    def status(self):
        if self.made == 1:
            print("Name: %s" % self.name)
            print("Race: %s" % self.race)
            print("Class: %s" % self.job)
            print("Subclass: %s" % self.subjob)
            print("Level: %s" % self.level)
        else:
            print("Please make a character.")

    def createcharacter(self):
        if self.made == 0:
            self.name = input("Character Name: ")
            self.race = input("Choose a Race 'Human', 'Awoken', or 'Exo': ")
            self.job = input("Choose a Class 'Titan', 'Hunter', or 'Warlock': ")
            if self.job == "Titan":
                self.subjob = input("Choose a Subclass 'Defender' or 'Striker': ")
            elif self.job == "Warlock":
                self.subjob = input("Choose a Subclass 'Sunsinger' or 'Voidwalker': ")
            elif self.job == "Hunter":
                self.subjob = input("Choose a Subclass 'Gunslinger' or 'Bladedancer': ")
            self.made += 1
        else:
            print("You already have a character.")

    def help(self):
        print(Commands.keys())

    def travel(self):
        if self.made == 1:
            if self.destination != "Space":
                answer = input("Would you like to go to space? \n 'yes' or 'no': ")
                if answer == "yes":
                    print("Your ship gracefully swoops down and picks you up.")
                    self.destination = "Space"
                else:
                    print("invalid selection")
            elif self.destination == "Space":
                answer = input("Where would you like to go? \n %s: " % planets)
                if answer == "Earth":
                    self.destination = "Earth"
                    self.currentmap = ""
                    print("Initiating Warp Drive")
                    print("Welcome to Earth")
                elif answer == "Tower":
                    self.destination = "Tower"
                    self.currentmap = ""
                    print("Initiating Warp Drive")
                    print("Welcome to the Tower")
                elif answer == "Moon":
                    self.destination = "Moon"
                    self.currentmap = ""
                    print("Initiating Warp Drive")
                    print("Welcome to the Moon")
                elif answer == "Venus":
                    self.destination = "Venus"
                    self.currentmap = ""
                    print("Initiating Warp Drive")
                    print("Welcome to Venus")
                elif answer == "Mars":
                    self.destination = "Mars"
                    self.currentmap = ""
                    print("Initiating Warp Drive")
                    print("Welcome to Mars")
        else:
            print("Make a character first.")

planets = ["Tower", "Earth", "Moon", "Venus", "Mars"]
p = player()

print("Welcome to Destiny")
print("Login Please")
username = input("Login: ")
usrpass = input("Password: ")
print("Connecting to Destiny servers...")
print("Connection Successful")
print("Downloading Character data")
print("Type: help \n for a list of commands")

Commands = {
    'status': player.status,
    'create character': player.createcharacter,
    'help': player.help,
    'travel': player.travel,

    }


while(p.health > 0):
  line = input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print("%s doesn't understand the suggestion." % p.name)
