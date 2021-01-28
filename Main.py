#   __________            __________            __________
#  |          |          |          |          |          |
#  | Barracks2|----------|  Med Bay |----------| Barracks1|
#  |          |          |          |          |          |
#  |__________|          |__________|          |__________|
#       |                     |                     |
#       |                     |                     |
#   ____|_____            ____|_____            ____|_____
#  |          |          |          |          |          |
#  |   Lab1   |----------|ViewingDome|---------|   Lab2   |
#  |          |          |          |          |          |
#  |__________|          |__________|          |__________|
#       |                     |                     |
#       |                     |                     |
#   ____|_____            ____|_____            ____|_____
#  |          |          |          |          |          |
#  |LeftEngine|----------|Electrical|----------|RightEngine|
#  |          |          |          |          |          |
#  |__________|          |__________|          |__________|

isRunning = True
import time

hints = ["Explore the spaceship by using the [move] command", "There might be some tools in the engine bays", "Have you checked the Med Bay for supplies?", "One of your fellow astronauts might have brought some digital photos with them", "The technicians might have left some stuff lying around when they were working in Electrical", "The scientists used a lot of dangerous gases in the labs"]

class Data:
    class ViewingDome:
        position = (0,0)
        discovered = False

    class Lab1:
        position = (-1,0)
        discovered = False

    class Lab2:
        position = (0,0)
        discovered = False

    class LeftEngine:
        position = (-1,-1)
        discovered = False

    class Electrical:
        position = (0,-1)
        discovered = False

    class RightEngine:
        position = (1,-1)
        discovered = False

    class MedBay:
        position = (0,1)
        discovered = False

    class Barracks2:
        position = (-1,1)
        discovered = False

    class Barracks1:
        position = (1,1)
        discovered = False

    x = 0
    y = 0
    currentPos = (x,y)
    hintNum = 0


class Functions:
    inText = str("")

    def PrintHelp():
        print('''
            
            Commands:
            ***NOTICE: These commands aren't case sensitive***
            ·Move <north/east/sout/west>: This is the command you use to move around the map
            ·ExitGame: This command exits the game (Duh)
            ·Where: This command tells you which room you are in
            ·LookAround: This command describes the room that you are in
            ·Help: This command brings up the help dialogue
            ·Hint: This command gives you a (potentially) helpful hint
            
        ''')

    def GetHint():
        global hints
        global Data
        try:
            print("Hint: " + hints[Data.hintNum])
        except:
            print("You have run out of hints")

        Data.hintNum +=1


    def Analyze(inText=""):
        if "move" in inText:
            inText = str(inText).replace("move ", "")
            Actions.Move(inText)
        elif "exitgame" in inText:
            global isRunning
            isRunning = False
        elif "where" in inText:
            print(Functions.FindCurrentRoom())
        elif "lookAround" in inText:
            Functions.GetRoomInfo()
        elif "help" in inText:
            Functions.PrintHelp()
        elif "hint" in inText:
            Functions.GetHint()
        else:
            print("Unknown command")

    def FindCurrentRoom():
        global Data
        if Data.currentPos == (0,0):
            return "The Viewing Dome"
        elif Data.currentPos == (0,1):
            return "Med Bay"
        elif Data.currentPos == (0,-1):
            return "Electrical"
        elif Data.currentPos == (1,1):
            return "Barracks 1"
        elif Data.currentPos == (-1,1):
            return "Barracks 2"
        elif Data.currentPos == (-1,0):
            return "Lab 1"
        elif Data.currentPos == (1,0):
            return "Lab 2"
        elif Data.currentPos == (-1,-1):
            return "Left Engine"
        elif Data.currentPos == (1,-1):
            return "Right Engine"

    def GetRoomInfo():
        global Data
        if Data.currentPos == (0,0):
            #The Viewing Dome
            print()
        elif Data.currentPos == (0,1):
            #Med Bay
            print()
        elif Data.currentPos == (0,-1):
            #Electrical
            print()
        elif Data.currentPos == (1,1):
            #Barracks 1
            print()
        elif Data.currentPos == (-1,1):
            #Barracks 2
            print()


class Actions:
    global Data

    def Move(dir):
        lastPos = Data.currentPos

        if dir == "north":
            Data.y += 1
            Data.currentPos = (Data.x, Data.y)
        elif dir == "south":
            Data.y -= 1
            Data.currentPos = (Data.x, Data.y)
        elif dir == "east":
            Data.x += 1
            Data.currentPos = (Data.x, Data.y)
        elif dir == "west":
            Data.x -= 1
            Data.currentPos = (Data.x, Data.y)
        else:
            print("That's not a possible direction")

        if Data.currentPos != lastPos: print("You are now in " + Functions.FindCurrentRoom())

print("Welcome, the game will begin shortly......")

print("You wake up, your body floating in the air. As you twist around, you catch a glimps outside of the window. A blue orb floats silently outside. Earth.")
time.sleep(10)
print("")
print("You shout out, looking for your crewmates, but you get no reply. As you examine the docking ports, realization washes over you.")
print("")
time.sleep(8)
print("They left")
time.sleep(3)
print("")
print("You have an idea! The other landing pod is still there! Unfortunately, it needs some repairs.")
time.sleep(5)
print("<Game> You need to gather these materials: Spanner, Tape, Cables, Thumb Drive, Oxygen Mask, Oxygen Tank </Game>")
time.sleep(5)

Functions.PrintHelp()

while isRunning:
    print("")
    inputText = input("What would you like to do? > ")
    inputText = inputText.lower()
    Functions.Analyze(inputText)