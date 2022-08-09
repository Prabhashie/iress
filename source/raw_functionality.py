DIRECTIONS = ["NORTH", "SOUTH", "EAST", "WEST"]
COMMANDS = ["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"]
GRID_X = 5
GRID_Y = 5

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
        comm = input("")
        comm = comm.strinp().split(" ") # remove leading or trailing whitespaces

        if len(comm) == 2: # PLACE command expected
            if comm[0].capitalize() == 'PLACE':
                directions = comm[1].strip().split(',')
                if len(directions) == 3: # if there are 3 parts in the later part of the command
                    # validate x is number
                    try:
                        x = int(directions[0])
                    except:
                        continue

                    # vallidate y is number
                    try:
                        y = int(directions[1])
                    except:
                        continue

                    # validate face
                    if directions[2] in DIRECTIONS:
                        f = directions[2]
                    else:
                        continue
                    
                    if validCoords(x,y):
                        robotPlaced = True
                    else:
                        continue
                else:
                    continue
            else:
                continue
        elif len(comm) == 1: # check for other commands
            if not robotPlaced: # ignore until robot has been placed
                continue 
            else:
                pass
        else: # invalid command structure
            continue
