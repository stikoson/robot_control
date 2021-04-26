# Robot control

This snippet is to solve a simple robot control problem. 
Usage:

`python robot.py input.txt`

`input.txt` contains the following information:
- size of the floor on which the robot can move, format `W L`, i.e. width and length, both are positive integers
- state of the robot `X Y DIRECTION`, where `X` and `Y` are the staring coordinates of the robot `DIRECTION` can be 
`N`orth, `E`ast, `W`est, `S`outh
- string with commands `L`eft, `R`ight, `F`orward, example: `LFFRFLFR`

The program initialize the robot at the starting point and moves it around according to the commands.
The output is the end-state of the robot.

Limited testing is available in `test.py`.

