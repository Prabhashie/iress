from libs.log_msgs import *

DIRECTIONS = ["NORTH", "SOUTH", "EAST", "WEST"]
COMMANDS = ["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"]
GRID_X = 5
GRID_Y = 5

def getProcessedInput():
    comm = input("")
    comm = comm.strip().split(" ") # remove leading or trailing whitespaces

    return comm

def validCoords(x, y):
    if x < GRID_X and y < GRID_Y:
        return True
    return False

def getNewCoords(x, y, f):
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

def getNewDirection(f, comm):
    newF = f
    if f == "NORTH":
        if comm == "LEFT":
            newF = "WEST"
        else:
            newF = "EAST"
    elif f == "SOUTH":
        if comm == "LEFT":
            newF = "EAST"
        else:
            newF = "WEST"
    elif f == "EAST":
        if comm == "LEFT":
            newF = "NORTH"
        else:
            newF = "SOUTH"
    else:
        if comm == "LEFT":
            newF = "SOUTH"
        else:
            newF = "NORTH"
    
    return newF

def solution():
    robotPlaced = False
    x, y, f = None, None, None

    while True:
        comm = getProcessedInput() # get processed input

        if len(comm) == 2: # PLACE command expected
            if comm[0].upper() == 'PLACE':
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
                    if directions[2].upper() in DIRECTIONS:
                        f = directions[2].upper()
                    else:
                        print(INVALID_DIRECTION_ERR)
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
            if comm[0].upper() == "QUIT": # loop termination request
                print(EXIT_PROGRAM_INFO)
                break
            if not robotPlaced: # ignore until robot has been placed
                print(ROBOT_NOT_PLACED_ERR)
                continue
            else: # for correct single word commands
                if comm[0].upper() == "MOVE":
                    newX, newY = getNewCoords(x, y, f) # get new coords if moved
                    if validCoords(newX, newY): # validate coordinates within the board
                        x, y = newX, newY
                elif comm[0].upper() == "LEFT" or comm[0].upper() == "RIGHT":
                    f = getNewDirection(f, comm[0].upper()) # get new direction after turning
                elif comm[0].upper() == "REPORT":
                    print(f"Output: {x}, {y}, {f}")
                else:
                    print(INVALID_COMMAND_ERR)
                    continue
        else: # invalid command structure
            print(INVALID_COMMAND_FORMAT_ERR)
            continue

solution()