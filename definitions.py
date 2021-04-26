'''
This file contains the Robot class definition and input file parsing logic
'''

import typing as t

# The following dictionary contains direction updates

DIRECTION_UPDATES = {("N", "R"): "E",
                     ("N", "L"): "W",
                     ("E", "R"): "S",
                     ("E", "L"): "N",
                     ("S", "R"): "W",
                     ("S", "L"): "E",
                     ("W", "R"): "N",
                     ("W", "L"): "S",
                    }

# The Robot class defines the state of the robot together
# with a process commands function which updates the states
# according to given commands

class Robot:
    
    def __init__(self, x: int, y: int, direction: str):
        
        self.x = x
        self.y = y
        self.direction = direction
    
    def process_commands(self, commands: str, floor: list):
        
        for command in commands:
            
            # If the command is of turning type, i.e. L or R direction is updates
            
            if command in "LR":
                self.direction = DIRECTION_UPDATES[(self.direction, command)]
                
            # When the command is forward (F) the position of the robot is updated
            elif command == "F":
                current_position = [self.x, self.y]
                
                if self.direction == "N":
                    self.y -= 1                        
                elif self.direction == "S":
                    self.y += 1
                elif self.direction == "E":
                    self.x += 1
                elif self.direction == "W":
                    self.x -= 1
                    
                # This check is to verify if the forward step is feasible considering the size of the floor
                    
                if (self.x < 0) or (self.y < 0) or (self.x > floor[0]) or (self.y > floor[1]):
                    print(f"{command} is not feasible at {current_position[0]}, {current_position[1]}, {self.direction}")
                    break
            else:
                print("Command not recognized:", command)
                break
            
        print(f"Report: {self.x} {self.y} {self.direction}")
        
        return(self.x, self.y, self.direction)
        

def parse_input(file_name: str):
        
    robot_file = open(file_name, 'r')
    lines = robot_file.readlines()
    
    # From the input file the floor dimension, initial robot state and list of commands are parsed

    floor = list(map(int, lines[0][:-1].split(" ")))
    print(floor[0], floor[1])

    start_state = lines[1][:-1].split(" ")
    x, y = list(map(int, start_state[:2]))
    
    direction = start_state[2]
    print(x, y, direction)

    commands = lines[2]
    print(commands)
    
    return(floor, x, y, direction, commands)

