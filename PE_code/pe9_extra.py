import random
def generate_path(maze, N, M):
    # This function generates a random path through an NxM maze, represented as a dictionary. The keys are (i, j) tuples representing
    # coordinates of each cell in the maze and the values are integers: 0 for empty, 1 for obstacle, and 2 for path. The path starts 
    # from (0,0) and ends at (N-1,M-1), and the direction (right or down) at each step is chosen randomly.
    # your code here
    #start
    current_point = (0,0)
    maze[(0,0)] = 2
    down_step =0
    right_step = 0
    while (right_step+down_step)<(N+M-2):
        choice = random.randint(0,1)
        if choice ==1 and right_step<M-1:
            #turn right
            if  maze[(current_point[0], current_point[1]+1)] == 0: #make sure there is no key error
                current_point = (current_point[0], current_point[1]+1)
                maze[current_point] = 2
                right_step +=1

        if choice ==0  and down_step<N-1:
            if maze[(current_point[0]+1, current_point[1])] == 0:
                current_point = (current_point[0]+1, current_point[1])            
                maze[current_point] = 2
                down_step +=1
def add_obstacles(maze, min_obstacles, N, M):
    # This function randomly adds obstacles (represented as 1) to the empty cells (represented as 0) in the given maze until at least
    # min_obstacles have been added. If a KeyError occurs while trying to set an obstacle, it is caught and a message is printed.
    # your code here

    #check the input value of minimum_obstacles
    try:
        min_obstacles = int(min_obstacles)
        if not (0<=min_obstacles<=55):
            return False
    except:
        print("ValueError occurred in main function. Invalid number of obstacles.")
        return False
    else:
        i=0
        while i <(min_obstacles):
            row = random.randint(0,N-1)
            col = random.randint(0,M-1)
            if maze[row,col]==0:
                maze[row,col] = 1
                i+=1
        return True
def set_obstacle(maze, N, M):
    # This function allows a user to manually set an obstacle in the maze. The user is prompted to input the coordinates of the cell
    # where they want to place the obstacle. If the cell is part of the path or an obstacle is already present, an error message is 
    # displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.
    # your code here
    while True:
        ui = input("Enter the coordinates to set an obstacle, e.g. i,j: ")
        ui_ls = ui.split(",")
        try: 
            tuple_keys = int(ui_ls[0]), int(ui_ls[1])
            #might be index error, typeerror
            if maze[tuple_keys] == 0:
                maze[tuple_keys] = 1
                print("Obstacle placed at (%d, %d)"%tuple_keys)
                break
            elif maze[tuple_keys] == 2:
                print("Obstacle cannot be placed on the path.")
            else:
                print("Obstacle already exist at this location.")
        except ValueError:
            print("ValueError in set_obstacle function. Need to be coordinate")
        except KeyError:
            print("KeyError in set_obstacle function. \'Invalid coordinates. Please input coordinates within the range.\'")
        except:
            print("ValueError in set_obstacle function. Need to be coordinate.")


def remove_obstacle(maze, N, M):
    # This function allows a user to manually remove an obstacle from the maze. The user is prompted to input the coordinates of the 
    # cell where they want to remove the obstacle. If the cell is part of the path or there's no obstacle at the given cell, an error 
    # message is displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here
    while True:
        ui = input("Enter the coordinates to remove obstacle, e.g. i,j: ")
        ui_ls = ui.split(",")
        try: 
            tuple_keys = int(ui_ls[0]), int(ui_ls[1])
            #might be index error, typeerror
            if maze[tuple_keys] == 1:
                maze[tuple_keys] = 0
                print("Obstacle removed at (%d, %d)"%tuple_keys)
                break
            elif maze[tuple_keys] == 2:
                print("Obstacle does not exist on the path.")
            else:
                print("Obstacle does not exist at this location.")
        except ValueError:
            print("ValueError in reomove obstacle function. Need to be coordinate")
        except KeyError:
            print("KeyError in remove obstacle function. \'Invalid coordinates. Please input coordinates within the range.\'")
        except:
            print("ValueError in reomove obstacle function. Need to be coordinate.")
def print_maze(maze, N, M):
    # This function prints the current state of the maze in a grid-like format. Each cell is represented by a 3-character string: 
    # '   ' for empty cells, ' X ' for obstacles, and ' O ' for path cells.
    # your code here

    for i in range(N):
        print("+---"*M+"+")
        for j in range(M):
            if maze[(i,j)] == 0:
                print("|   ", end="")
            elif maze[(i,j)] == 1:
                print("| X ", end="")
            else:
                print("| O ", end="")
        print("|")
    print("+---"*M+"+")
def main():
    # This function serves as the main driver of the program. It reads the maze dimensions from a file, asks the user for the minimum 
    # number of obstacles to be added, generates the path and adds the obstacles, and then enters a loop where the user can choose to 
    # set or remove obstacles, print the maze, or exit the program. Exceptions for ValueError, IOError, and NameError are handled.
    # your code here

    #load the grid file
    while True:
        ui_filename = input("Enter file name: ") 
        try:
            fr = open(ui_filename, "r")
            grids_rows = fr.readlines()
            fr.close()
            break
        except:
            print("IOError occurred in main function. File not found Plaese enter a valid file name")

    #initialize the maze, N, M
    i = 1 #start from the first line, i,j are the indices for the strings
    maze = {}
    N = 0
    while i<len(grids_rows):
        M=0
        j=2 #the first entry index of grid
        while j <len(grids_rows[1]):
            if grids_rows[i][j] ==" ":
                maze[N,M] = 0
            else:
                maze[N,M] = 1
            j+=4
            M+=1
        N+=1
        i+=2
    print_maze(maze,N,M) #show the initial grids
    generate_path(maze,N,M)

    while True:
        ui = input("Enter the minimum number of obstacles (0-55): ")
        if add_obstacles(maze, ui, M,N):
            break
    print_maze(maze,N,M) #print the new maze with new added obstacles

    while True:
        print("Options:\n1. Set obstacle\n2. Remove obstacle\n3. Exit")
        ui = input("Enter your option: ")
        if ui not in ["1","2","3"]:
            print("Invalid option. Please choose a valid option.")
        elif ui == "3":
            break
        elif ui =="1":
            set_obstacle(maze, N, M)
            print_maze(maze, N, M)
        elif ui =="2":
            remove_obstacle(maze, N,M)
            print_maze(maze, N,M)



main()
