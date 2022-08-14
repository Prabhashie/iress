"""
file name:      play_robot2.py
author:         Sachinthana Pathiranage
date created:   14/08/2022
purpose:        Contains the raw functionality for the requirement. 
                This implimentation follows OOP concepts.
version:        1.0
"""

# imports
from classes.grid import Grid
from classes.robot import Robot
from utils.log_msgs import *

# constants
DIRECTIONS = ["NORTH", "SOUTH", "EAST", "WEST"]
SINGULAR_COMMANDS = ["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"]

# global variables
grid = Grid()
robot = Robot(grid)

def redefine_grid():
    """Change the default grid dimensions.
    """
    while True: # get the new x dimension
        newX = input(f"Please enter new x dimension (current is {grid.xDim}): ")
        try:
            newX = int(newX)
            break
        except:
            if newX.upper() == "QUIT" or newX.upper() == "Q":
                print(EXIT_PROGRAM_INFO)
                break
            print(INVALID_DIMENSION_ERR)
            continue
    
    while True: # get the new y dimension
        newY = input(f"Please enter new y dimension (current is {grid.yDim}): ")
        try:
            newY = int(newY)
            break
        except:
            if newY.upper() == "QUIT" or newX.upper() == "Q":
                print(EXIT_PROGRAM_INFO)
                break
            print(INVALID_DIMENSION_ERR)
            continue
    
    grid.change_dims(newX, newY)
    print(NEW_GRID_DIMENSIONS_SET_INFO)

def get_processed_input():
    """Processes the initial input command.

    :return: List of constituents of the command.
    :rtype: list
    """
    comm = input("")
    comm = comm.strip().split(" ", 1) # split on first occurence to avoid spaces in args of "PLACE" command
    comm = [c.strip() for c in comm if c != ""] # remove leading or trailing whitespaces

    return comm

def get_processed_args(args):
    """Processes the arguments for PLACE command.

    :param args: Args for the PLACE command.
    :type args: str
    :return: List of constituent args.
    :rtype: list
    """
    newArgs = args.strip().split(',')
    newArgs = [a.strip() for a in newArgs if a != "" and not a.isspace()] # remove leading or trailing whitespaces and empty args

    return newArgs

def validate_args(args):
    """Validate args of the PLACE command.

    :param args: Args for the PLACE command.
    :type args: list
    :return: If arguments are valid, error string, x coordinate, y coordinate, direction. For invalid args, last three args will be of None type.
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

def play_game():
    """Driver functionality for the toy robot.
    """
    robotPlaced = False

    while True:
        comm = get_processed_input() # get processed input
        if len(comm) == 2: # PLACE command expected
            if comm[0].upper() == 'PLACE':
                args = get_processed_args(comm[1])
                if len(args) == 3: # if there are 3 args in the later part of the command
                    # validate arguments
                    validArgs, errStr, newX, newY, newF = validate_args(args)
                    if not validArgs:
                        print(errStr)
                        continue
                    
                    validPlacement, errStr = robot.place(newX, newY, newF)
                    # validate coordinates within the board
                    if not validPlacement:
                        print(errStr)
                        continue
                    robotPlaced = True
                else:
                    print(INVALID_ATTR_COUNT_ERR)
                    continue
            else:
                print(INVALID_COMMAND_ERR)
                continue
        elif len(comm) == 1: # check for other commands
            if comm[0].upper() == "QUIT" or  comm[0].upper() == "Q": # loop termination request
                print(EXIT_PROGRAM_INFO)
                break
            if comm[0].upper() not in SINGULAR_COMMANDS: # invalid command
                print(INVALID_COMMAND_ERR)
                continue
            if not robotPlaced: # ignore until robot has been placed
                print(ROBOT_NOT_PLACED_ERR)
                continue
            else: # for correct single word commands
                if comm[0].upper() == "MOVE":
                    validCoords, errStr = robot.move() # get new coords if moved
                    if not validCoords:
                        print(errStr)
                        continue
                elif comm[0].upper() == "LEFT" or comm[0].upper() == "RIGHT":
                    robot.turn(comm[0].upper()) # get new direction after turning
                else:
                    robot.report()
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
            redefine_grid()
        elif choice == 2:
            play_game()
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