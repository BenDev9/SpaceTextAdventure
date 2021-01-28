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
discoverDialogue = "You haven't been in this room yet, maybe you should [lookAround]?"

class Data:
    class Rooms:
        class ViewingDome:
            Name = "The Viewing Dome"
            position = (0,0)
            discovered = False

        class Lab1:
            Name = "Lab 1"
            position = (-1,0)
            discovered = False

        class Lab2:
            Name = "Lab 2"
            position = (0,0)
            discovered = False

        class LeftEngine:
            Name = "Left Engine"
            position = (-1,-1)
            discovered = False

        class Electrical:
            Name = "Electrical"
            position = (0,-1)
            discovered = False

        class RightEngine:
            Name = "Right Engine"
            position = (1,-1)
            discovered = False

        class MedBay:
            Name = "Med Bay"
            position = (0,1)
            discovered = False

        class Barracks2:
            Name = "Barracks 2"
            position = (-1,1)
            discovered = False

        class Barracks1:
            Name = "Barracks 1"
            position = (1,1)
            discovered = False

    x = 0
    y = 0
    currentPos = (x,y)
    hintNum = 0

roomsArray = [Data.Rooms.ViewingDome, Data.Rooms.Lab1, Data.Rooms.Lab2, Data.Rooms.Electrical, Data.Rooms.Barracks1, Data.Rooms.Barracks2, Data.Rooms.RightEngine, Data.Rooms.LeftEngine, Data.Rooms.MedBay]

class Functions:
    inText = str("")
    global Data

    def Debug():
        for room in roomsArray:
            print(room.Name)

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

            Syntax:
                ·In the hints, I use square brackets around commands [Like this]
                ·Game announcements will be in XML tags <Game> Like this </Game>
            
        ''')

    def GetHint():
        global hints
        global Data
        try:
            print("Hint: " + hints[Data.hintNum])
        except:
            print("You have run out of hints")

        Data.hintNum +=1

    def GetDiscovery():
        for room in Data:
            print(room)

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
        elif "debugcommand" in inText:
            Functions.Debug()
        else:
            print("Unknown command")

    def FindCurrentRoom():
        global Data
        if Data.currentPos == Data.ViewingDome.position:
            return "The Viewing Dome"
        elif Data.currentPos == Data.MedBay.position:
            return "Med Bay"
        elif Data.currentPos == Data.Electrical.position:
            return "Electrical"
        elif Data.currentPos == Data.Barracks1.position:
            return "Barracks 1"
        elif Data.currentPos == Data.Barracks2.position:
            return "Barracks 2"
        elif Data.currentPos == Data.Lab1.position:
            return "Lab 1"
        elif Data.currentPos == Data.Lab2.position:
            return "Lab 2"
        elif Data.currentPos == Data.LeftEngine.position:
            return "Left Engine"
        elif Data.currentPos == Data.RightEngine.position:
            return "Right Engine"

    def GetRoomInfo():
        global Data
        if Data.currentPos == Data.Rooms.ViewingDome.position:
            #The Viewing Dome
            print("The room has large, thick, plate glass windows, offering a beatiful view.")
        elif Data.currentPos == Data.Rooms.MedBay.position:
            #Med Bay
            print()
        elif Data.currentPos == Data.Rooms.Electrical.position:
            #Electrical
            print()
        elif Data.currentPos == Data.Rooms.Barracks1.position:
            #Barracks 1
            print()
        elif Data.currentPos == Data.Rooms.Barracks2.position:
            #Barracks 2
            print()
        elif Data.currentPos == Data.Rooms.LeftEngine.position:
            #Left Engine
            print()
        elif Data.currentPos == Data.Rooms.RightEngine.position:
            #RightEngine
            print()
        elif Data.currentPos == Data.Rooms.Lab1.position:
            #Lab1
            print()
        elif Data.currentPos == Data.Rooms.Lab2.position:
            #Lab2
            print()
        
    def GetRoomDiscoveryInfo():
        global Data
        if Data.currentPos == Data.Rooms.ViewingDome.position:
            #The Viewing Dome
            print("The room has large, thick, plate glass windows, offering a beatiful view.")
        elif Data.currentPos == Data.Rooms.MedBay.position:
            #Med Bay
            print()
        elif Data.currentPos == Data.Rooms.Electrical.position:
            #Electrical
            print()
        elif Data.currentPos == Data.Rooms.Barracks1.position:
            #Barracks 1
            print()
        elif Data.currentPos == Data.Rooms.Barracks2.position:
            #Barracks 2
            print()
        elif Data.currentPos == Data.Rooms.LeftEngine.position:
            #Left Engine
            print()
        elif Data.currentPos == Data.Rooms.RightEngine.position:
            #RightEngine
            print()
        elif Data.currentPos == Data.Rooms.Lab1.position:
            #Lab1
            print()
        elif Data.currentPos == Data.Rooms.Lab2.position:
            #Lab2
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
        for room in roomsArray:
            if room.Name.lower() == Functions.FindCurrentRoom().lower():
                if room.Discovered == False: print()


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