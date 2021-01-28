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

class Data:
    class Room:
        name = ""
        position = (0,0)

    x = 0
    y = 0
    currentPos = (x,y)


class Functions:
    inText = str("")

    def Analyze(inText=""):
        if "move" in inText:
            inText = str(inText).replace("move ", "")
            Actions.Move(inText)
        elif "exitgame" in inText:
            global isRunning
            isRunning = False
        elif "where" in inText:
            Functions.FindCurrentRoom()
        elif "where" in inText:
            Functions.GetRoomInfo()
        elif "help" in inText:
            print('''
            
                Commands:
                ***NOTICE: These commands aren't case sensitive***
                ·Move <north/east/sout/west>: This is the command you use to move around the map
                ·ExitGame: This command exits the game (Duh)
            
            ''')
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
        if dir != "north" or dir != "south" or dir != "east" or dir != "west": print("Not a possible direction")
        else:
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

        print("You are now in " + Functions.FindCurrentRoom())

while isRunning:
    inputText = input("what would you like to do> ")
    inputText = inputText.lower()
    Functions.Analyze(inputText)