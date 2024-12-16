#type: ignore
def moveTo(x_or_tuple = None, y = None):
    if x_or_tuple == None and y == None:
        x = 0
        y = 0
    elif y == None:
        x, y = x_or_tuple
    else:
        x = x_or_tuple
    
    while get_pos_x() != x:
        if ((get_pos_x()-x) % get_world_size() >= (x-get_pos_x()) % get_world_size()):
            move(East)
        else:
            move(West)

    while get_pos_y() != y:
        if ((get_pos_y()-y) % get_world_size() >= (y-get_pos_y()) % get_world_size()):
            move(North)
        else:
            move(South)