def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Can also be while at_goal() == False:
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
