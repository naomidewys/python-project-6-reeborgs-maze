# defines right turn because only turn left and move forward are pre-defined in program.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# reeborg moves forward until reaches a wall
while front_is_clear():
    move()
turn_left()

# while loop until goal is reached
while not at_goal():
    # reeborg follows right side of maze
    if right_is_clear():
        turn_right()
        move()
    # if wall on right side but front is clear, move forward    
    elif front_is_clear():
        move()
    # if wall in front and on right, turn left until front is clear again to restart first loop
    else:
        turn_left()
