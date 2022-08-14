# iress

IRESS Toy Robot Coding Challenge
--------------------------------

Content:
    This file contains the implementation and testing for the IRESS Toy Robot Coding Challenge.

Folder and file structure (iress/submission/):
    classes: Contains the class files for the OOP implementation.
    utils: Contains the utilities required to execute the program. At the moment, provides logging and testing capability.
    src: Source codes for the implementation. Contains a non-OOP approach and a OOP approach.
    tests: Test files for the functionality. Contains unit and integrations tests.
    setup.py: Setup file for package imports.

Requirements:
    Python Version: Python 3.10 and above.

Application type: Console Application. 

How to run:
    1. Download the iress folder.
    2. Inside the iress/submission/ directory, run the command 'python setup.py install' to install the package import setup.
    3. Inside the iress/submission/src directory, run play_robot1.py as 'python play_robot1.py'.
    P.S. Whenever changes are done to the modules imported from other packages, the setup file should be reinstalled in order for the changes to be reflected in other files.

Input types:
    Currently implemented for standard input. 

Program commands:
    PLACE X,Y,F:
        PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. 
        The origin (0,0) can be considered to be the SOUTH WEST most corner. 
        It is required that the first command to the robot is a PLACE command.
        After that, any sequence of commands may be issued, in any order, including another PLACE command.
    
    MOVE:
        MOVE will move the toy robot one unit forward in the direction it is currently facing.

    LEFT/ RIGHT:
        LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot.

    REPORT:
        REPORT will announce the X,Y and F of the robot.

Notes:
    According to the initial requirement, the robot will move on a table with a 5X5 grid. However, capability is provided to modify the range of the grid.
    A robot that is not on the table ignores the MOVE, LEFT, RIGHT and REPORT commands.

TODO:
    Implement capability to accept commands from a file input.