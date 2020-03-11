###Minecraft Adventure
def intro():
    wake = input("Hello Traveler, did you just wake up?")

    if wake=="yes":
        print("Strange... I don't have time to talk, but take this")
        print("*The Mysterious Man gave you a rusty sword and took off*")
    else:
        print("Oh, ok have a good day then.")

intro()

def Forest():
    print(" After the man leaves you decide to gather resources")
    woodtool = input("you chopped down a tree. What would you like to do with the wood? Would you like to create a sword or a pickaxe?")

    if woodtool == "sword": cave1 = input("you craft a wood sword and realize that its worse than the rusty one you have. So, you get more wood and make a pickaxe. Would you like to go mining?")

    else woodtool:  == input(" You built your pickaxe, and you remember you saw a mine when you were breaking the tree down. Will you go mining? ")

    if cave1 == "yes": deepcave =input("you got some cobble stone and made a better pickaxe, would you like to go further?")

    else: buildhome = input("you decide to not go mining, instead you gather materials and food for later.") 

    if deepcave == "yes": print("You go further and find some iron to mine. its a dead end and you leave the cave")

    buildhome = input(" You finished mining and killed a chicken for some food would you like to build a house and sleep?" )

    if buildhome == "yes": print( "You built a small house and used the wool from a sheep to make a small bed, You decide its time for bed and got to sleep")

    else: print( "Oof, It looks like you got ambushed by a creeper! Better luck next time")
    life1 = input(" respawn or quit? ")
    if life1 == "respawn": print("respawn")
    else: print(" Goodbye")
Forest()

