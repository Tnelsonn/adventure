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
Forest()
