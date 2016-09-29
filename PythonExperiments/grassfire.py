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

distance = 0
while (distance < 1):
   distance = distance + 1
   
   world[world_end_x + distance][world_end_y] = distance
   world[world_end_x - distance][world_end_y] = distance

   world[world_end_x][world_end_y + distance] = distance
   world[world_end_x][world_end_y - distance] = distance

# printing world
for x in range(0, world_rows):
    for y in range(0, world_cols):
        print(world[x][y], end="  ")
    print("\n")

#print(world)