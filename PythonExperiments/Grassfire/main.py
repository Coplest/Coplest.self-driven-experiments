from find import paths

world_rows = 7
world_cols = 6

# creating 2D world
#     create an array of "world_cols" cols, for each of the "world_rows" rows
#        all elements are initialized to "-" character

world = [["-" for j in range(0, world_cols)] for i in range(0, world_rows)]

# setting start point
world_start_x = 0
world_start_y = 1
world[world_start_x][world_start_y] = "+"

# setting end point
world_end_x = 5
world_end_y = 4
world[world_end_x][world_end_y] = 0

# setting an obstacles
world_obstacle_x = 2
world_obstacle_y = 3
world[world_obstacle_x][world_obstacle_y] = "."

world_obstacle_x = 3
world_obstacle_y = 3
world[world_obstacle_x][world_obstacle_y] = "."

world_obstacle_x = 4
world_obstacle_y = 3
world[world_obstacle_x][world_obstacle_y] = "."

distance = 0
twoWays = False

while True:
    
    # Loop into array
    for x in range(0, world_rows):
        for y in range(0, world_cols):
            # If actual position is initial point verify if has two ways to complete path
            if(world[x][y] == "+"):
                try:
                    if(world[x + 1][y] != "-" and world[x][y + 1] != "-"):
                        twoWays = True
                except IndexError:
                    pass
                try:
                    if(world[x - 1][y] != "-" and world[x][y + 1] != "-"):
                        twoWays = True
                except IndexError:
                    pass
                try:
                    if(world[x + 1][y] != "-" and world[x][y - 1] != "-"):
                        twoWays = True
                except IndexError:
                    pass
                try:
                    if(world[x - 1][y] != "-" and world[x][y - 1] != "-"):
                        twoWays = True
                except IndexError:
                    pass
            # If actual position is same as distance            
            elif(world[x][y] == distance):
                # try to set distance with siblings
                try:
                    if(world[x + 1][y] == "-"):
                        world[x + 1][y] = distance + 1
                    if(world[x - 1][y] == "-"):
                        world[x - 1][y] = distance + 1

                    if(world[x][y + 1] == "-"):
                        world[x][y + 1] = distance + 1
                    if(world[x][y - 1] == "-"):
                        world[x][y - 1] = distance + 1
                except IndexError:
                    pass
        
    distance = distance + 1

    if(twoWays == True):
        break

# printing world
for x in range(0, world_rows):
    for y in range(0, world_cols):
        print(world[x][y], end="  ")
    print("\n")

# Now we know max_distance with distance value
max_distance = distance
print("max_distance: ", max_distance)

#print(world)