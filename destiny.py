class character():
    def __init__(self):
        self.name = ""
        self.race = ""
        self.job = ""
        self.subjob = ""
        
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
    def status(self):
        print("Name: %s" % self.name)
        print("Class: %s" % self.job)
        print("Subclass: %s" % self.subjob)
    def menu(self):
        return
    def createcharacter(self):
        self.name = input("Character Name: ")
        self.job = 

        
p = player()

print("Welcome to Destiny")
print("Login Please")
username = input("Login: ")
usrpass = input("Password: ")
print("Connecting to Destiny servers...")
print("Connection Sucessful")
print("Downloading Character data")

Commands = { 
    'status': player.status, 
    'create character': player.createcharacter(self),
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
