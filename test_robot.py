'''
This module is to test the correctness of the process_commands function of robot.py.
'''

import sys
from definitions import Robot, parse_input

def test_correct_input():
    
    x_start, y_start = 1, 2
    direction_start = "N"
    floor = [5, 5]
    commands = "RFRFFRFRF"
    
    R = Robot(x_start, y_start, direction_start)
    x_end, y_end, direction_end = R.process_commands(commands, floor)
    
    print(x_end, y_end, direction_end)
    
    assert (x_end == 1), "x end coordinate is incorrect."
    assert y_end == 3, "y end coordinate is incorrect."
    assert direction_end == "N", "End direction is incorrect."

    print("End state is correct")
    
def test_correct_input_2():
    
    x_start, y_start = 0, 0
    direction_start = "E"
    floor = [5, 5]
    commands = "RFLFFLRF"
    
    R = Robot(x_start, y_start, direction_start)
    x_end, y_end, direction_end = R.process_commands(commands, floor)
    
    print(x_end, y_end, direction_end)
    
    assert (x_end == 3), "x end coordinate is incorrect."
    assert y_end == 1, "y end coordinate is incorrect."
    assert direction_end == "E", "End direction is incorrect."

    print("End state is correct")
