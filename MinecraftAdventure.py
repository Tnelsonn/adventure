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
    collection = input("What will you do now that the man is gone? Will you explore or gather resources?")

    if collection == "explore":
        print("you find a village but you are tired and hungry from all the running")
        ###add class for villagers and allow person to choose who to talk to###
    else: woodtool = input("you chopped down a tree. What would you like to do with the wood? Would you like to create a sword or a pickaxe?")
    if woodtool == "sword":
        print(" You make a crafting table and make a wood sword, but you remember you have a rusted one already " )
    else: cave1 = input(" You built your pickaxe, and you remember you saw a mine when you were breaking the tree down. Will you go mining? ")
    if cave1 == "yes": deepcave =input("you got some cobble stone and made a better pickaxe, would you like to go further?")
    if deepcave1 == "yes": print("You go further and find some iron to mine. its a dead end and you leave the cave")
    buildhome = input(" You finished mining and killed a chicken for some food would you like to build a house and sleep?" )
Forest()

