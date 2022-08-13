"""
file name:      raw_functionality.py
author:         Sachinthana Pathiranage
date created:   09/08/2022
purpose:        Contains the raw functionality for the requirement. 
                This implimentation doesn't follow OOP concepts.
version:        1.0
"""

# imports
from libs.log_msgs import *

# constants
DIRECTIONS = ["NORTH", "SOUTH", "EAST", "WEST"]
COMMANDS = ["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"]
GRID_X = 5
GRID_Y = 5

def defineGrid():
    """Change the default grid dimensions.
    """
    while True: # get the new x dimension
        newX = input(f"Please enter new x dimension (current is {GRID_X}): ")
        try:
            GRID_X = int(newX)
            break
        except:
            if newX.upper() == "QUIT" or choice.upper() == "Q":
                print(EXIT_PROGRAM_INFO)
                break
            print(INVALID_DIMENSION_ERR)
            continue
    
    while True: # get the new y dimension
        newY = input(f"Please enter new y dimension (current is {GRID_Y}): ")
        try:
            GRID_Y = int(newY)
            break
        except:
            if newY.upper() == "QUIT" or choice.upper() == "Q":
                print(EXIT_PROGRAM_INFO)
                break
            print(INVALID_DIMENSION_ERR)
            continue

    print(NEW_GRID_DIMENSIONS_SET_INFO)

def getProcessedInput():
    """Processes the initial input command.

    :return: List of constituents of the command.
    :rtype: list
    """
    comm = input("")
    comm = comm.strip().split(" ", 1) # split on first occurence to avoid spaces in args of "PLACE" command
    comm = [c.strip() for c in comm if c != ""] # remove leading or trailing whitespaces

    return comm

def getProcessedArgs(args):
    """Processes the arguments for PLACE command.

    :param args: Args for the PLACE command.
    :type args: str
    :return: List of constituent args.
    :rtype: list
    """
    newArgs = args.strip().split(',')
    newArgs = [a.strip() for a in newArgs if a != "" and not a.isspace()] # remove leading or trailing whitespaces and empty args
    print(newArgs)

    return newArgs

def validateArgs(args):
    """Validate args of the PLACE command.

    :param args: Args for the PLACE command.
    :type args: list
    :return: ifValidArgs, errorString, x coordinate, y coordinate, direction. For invalid args, last three args will be of None type.
    :rtype: bool, str, int, int, str
    """
    errStr = ""
    x, y, f = None, None, None

    try:
        x = int(args[0])
    except:
        errStr = UNEXPECTED_TYPE_ERR + " x coordinate should be an integer."
        return False, errStr, x, y, f

    # vallidate y is number
    try:
        y = int(args[1])
    except:
        errStr = UNEXPECTED_TYPE_ERR + " y coordinate should be an integer."
        return False, errStr, x, y, f

    # validate face
    if args[2].upper() in DIRECTIONS:
        f = args[2].upper()
    else:
        errStr = INVALID_DIRECTION_ERR + " Valid directions are [NORTH, SOUTH, EAST, WEST]."
        return False, errStr, x, y, f
    
    return True, errStr, x, y, f

def validCoords(x, y):
    """Validate x, y coordinate range.

    :param x: y coordinate.
    :type x: int
    :param y: y coordinate.
    :type y: int
    :return: If coordinates are valid.
    :rtype: bool
    """
    if x < GRID_X and y < GRID_Y:
        return True
    return False

def move(x, y, f):
    """Move the robot.

    :param x: y coordinate.
    :type x: int
    :param y: y coordinate.
    :type y: int
    :param f: Facing direction.
    :type f: str
    :return: New x and y coordinates.
    :rtype: int, int
    """
    newX, newY = x, y
    if f == "NORTH":
        newY = y + 1
    elif f == "SOUTH":
        newY = y - 1
    elif f == "EAST":
        newX = x + 1
    else:
        newX = x - 1
    
    return newX, newY

def turn(f, direction):
    """Turn the robot.

    :param f: Current facing direction.
    :type f: str
    :param direction: Turning direction.
    :type direction: str
    :return: New direction.
    :rtype: str
    """
    newF = f
    if f == "NORTH":
        if direction == "LEFT":
            newF = "WEST"
        else:
            newF = "EAST"
    elif f == "SOUTH":
        if direction == "LEFT":
            newF = "EAST"
        else:
            newF = "WEST"
    elif f == "EAST":
        if direction == "LEFT":
            newF = "NORTH"
        else:
            newF = "SOUTH"
    else:
        if direction == "LEFT":
            newF = "SOUTH"
        else:
            newF = "NORTH"
    
    return newF

def playGame():
    """Driver functionality for the toy robot.
    """
    robotPlaced = False
    x, y, f = None, None, None

    while True:
        comm = getProcessedInput() # get processed input

        if len(comm) == 2: # PLACE command expected
            if comm[0].upper() == 'PLACE':
                args = getProcessedArgs(comm[1])
                if len(args) == 3: # if there are 3 args in the later part of the command
                    # validate x is number
                    validArgs, errStr, x, y, f = validateArgs(args)
                    if not validArgs:
                        print(errStr)
                        continue
                    # validate coordinates within the board
                    if validCoords(x,y):
                        robotPlaced = True
                    else:
                        print(INVALID_COORD_RANEG_ERR)
                        continue
                else:
                    print(INVALID_ATTR_COUNT_ERR)
                    continue
            else:
                print(INVALID_COMMAND_ERR)
                continue
        elif len(comm) == 1: # check for other commands
            if comm[0].upper() == "QUIT" or choice.upper() == "Q": # loop termination request
                print(EXIT_PROGRAM_INFO)
                break
            if not robotPlaced: # ignore until robot has been placed
                print(ROBOT_NOT_PLACED_ERR)
                continue
            else: # for correct single word commands
                if comm[0].upper() == "MOVE":
                    newX, newY = move(x, y, f) # get new coords if moved
                    if validCoords(newX, newY): # validate coordinates within the board
                        x, y = newX, newY
                elif comm[0].upper() == "LEFT" or comm[0].upper() == "RIGHT":
                    f = turn(f, comm[0].upper()) # get new direction after turning
                elif comm[0].upper() == "REPORT":
                    print(f"Output: {x}, {y}, {f}")
                else:
                    print(INVALID_COMMAND_ERR)
                    continue
        else: # invalid command structure
            print(INVALID_COMMAND_FORMAT_ERR)
            continue

# driver code
print("Toy Robot Code Challenge")

while True:
    print("1. Setup grid dimesions.")
    print("2. Play the game.")
    choice = input("Select an option: ")
    try:
        choice = int(choice)
        if choice == 1:
            defineGrid()
        elif choice == 2:
            playGame()
        else:
            print(INVALID_CHOICE_ERR)
            continue
    except:
        if choice.upper() == "QUIT" or choice.upper() == "Q":
            print(EXIT_PROGRAM_INFO)
            break
        else:
            print(INVALID_CHOICE_ERR)
            continue
