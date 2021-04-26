"""
This program is to solve a robotic challenge. From given floor size,
position, the direction of the robot and a set of commands it returns
the position and direction of the robot that was following the commands.
"""

import sys
from definitions import Robot, parse_input

        
if __name__ == "__main__":

    file_name = sys.argv[1]
        
    floor, x, y, direction, commands = parse_input(file_name)
    
    # Instantiating the Robot class and process the commands

    R = Robot(x, y, direction)
    R.process_commands(commands, floor)
         