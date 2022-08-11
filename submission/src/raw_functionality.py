import sys
import os

sys.path.append(os.getcwd() + "\submission")

from libs.log_msgs import *

DIRECTIONS = ["NORTH", "SOUTH", "EAST", "WEST"]
COMMANDS = ["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"]
GRID_X = 5
GRID_Y = 5

def getProcessedInput():
    comm = input("")
    comm = comm.strinp().split(" ") # remove leading or trailing whitespaces

    return comm

def validCoords(x, y):
    if x < GRID_X and y < GRID_Y:
        return True
    return False

def solution():
    robotPlaced = False
    x = None
    y = None
    f = None

    while True:
        comm = getProcessedInput() # get processed input

        if len(comm) == 2: # PLACE command expected
            if comm[0].capitalize() == 'PLACE':
                directions = comm[1].strip().split(',')
                if len(directions) == 3: # if there are 3 parts in the later part of the command
                    # validate x is number
                    try:
                        x = int(directions[0])
                    except:
                        print(UNEXPECTED_TYPE_ERR)
                        continue

                    # vallidate y is number
                    try:
                        y = int(directions[1])
                    except:
                        print(UNEXPECTED_TYPE_ERR)
                        continue

                    # validate face
                    if directions[2] in DIRECTIONS:
                        f = directions[2]
                    else:
                        print(INVALID_DIRECTION_ERR)
                        continue
                    
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
            if comm.capitalize() == "QUIT":
                print(EXIT_PROGRAM_INFO)
                break
            if not robotPlaced: # ignore until robot has been placed
                print(ROBOT_NOT_PLACED_ERR)
                continue
            else:
                pass
        else: # invalid command structure
            print(INVALID_COMMAND_FORMAT_ERR)
            continue
