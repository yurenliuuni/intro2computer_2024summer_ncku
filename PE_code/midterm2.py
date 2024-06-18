3
import random

def generate_path(N, M):
    # Goal: Generate a maze with a clear path from the starting point to the bottom-right cell using a brute-force approach.
    # Detailed Instructions:
    # 1. Create a 2D list of zeros representing the maze map with dimensions N rows by M columns.
    # 2. Start at the top-left cell of the maze map and add it to the path list.
    # 3. While not at the bottom-right cell of the maze map:
    #     a. If at the bottom row of the maze map, move right.
    #     b. If at the rightmost column of the maze map, move down.
    #     c. Otherwise, randomly choose to move right or down.
    #     d. Mark the chosen cell as part of the path and add it to the path list.
    # 4. Mark the bottom-right cell of the maze map as part of the path and add it to the path list.
    # 5. Return the updated maze map with the path.
    
    maze = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(0)
        maze.append(row)

    # # your code here
    path_list=[] #length is n-1 right and m-1 down

    # for i in range(N+M-2):


    path_list.append([0,0])
    start_point = [0,0]
    current_point = start_point
    count_step = 0

    while current_point != [N-1, M-1] :

        choice_right_or_down =random.randint(0,1) 

        if current_point[1] == M-1: #走到最右邊
            current_point[0] +=1 
            path_list.append(list(current_point))
            continue
        if current_point[0] == N-1:  #reach the bottom
            current_point[1] +=1
            path_list.append(list(current_point))
            continue

        if choice_right_or_down == 0:
            current_point[1] = current_point[1] +1
            path_list.append(list(current_point))
        else:
            current_point[0] = current_point[0]+1
            path_list.append(list(current_point))

        print(path_list)




    return maze, path_list

def add_obstacles(maze, num_obstacles, path_list):
    # Goal: Add a number of obstacles randomly to the maze.
    # Detailed Instructions:
    # 1. While the number of obstacles in the maze is less than num_obstacles:
        # a. Choose a random cell in the maze that is not part of the path or already an obstacle.
        # b. Mark the cell as an obstacle.
    # 2. Return the updated maze map with the obstacles.

    # your code here
    #印出障礙物為2, 路徑為1


    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if [i,j] in path_list:
                maze[i][j] = 2

    count_obstacles = 0
    while count_obstacles <num_obstacles:
        i= random.randint(0,len(maze)-1)
        j=random.randint(0,len(maze[0])-1)
        if maze[i][j] ==0:
            maze[i][j] = 1
            count_obstacles+=1

    return maze

def generate_maze(N, M, num_obstacles):
    # Goal: Generate a maze with a clear path from the starting point to the bottom-right cell and a number of obstacles using a brute-force approach.
    # Detailed Instructions:
    # 1. Call the generate_path function with the arguments N and M to generate a maze with a clear path.
    # 2. Call the add_obstacles function with the generated maze map and the argument num_obstacles to add a number of obstacles randomly to the maze.
    # 3. Return the updated maze map.


    # generate a maze with a clear path from the starting point to the bottom-right cell
    maze, path_list = generate_path(N, M)

    # add the number of obstacles randomly to the maze
    maze = add_obstacles(maze, num_obstacles, path_list)

    return maze



def print_maze(maze):
    # Goal: Print the maze map as a grid to the console using boundaries with "-", "|", and "+" symbols.
    # Detailed Instructions:
    # 1. For each row in the maze map:
    #   a. Print a horizontal boundary line with "+" symbols at the intersections and "-" symbols between them.
    #   b. For each cell in the row:
    #       If the cell is an obstacle, print an "X" symbol.
    #       Otherwise, print a space character.
    #   c. Print a vertical boundary line with "|" symbols at the ends.
    # 2. Print a horizontal boundary line with "+" symbols at the intersections and "-" symbols between them at the bottom of the maze map.
    
    print("+" + "---+" * len(maze[0]))
    for i in range(len(maze)):
        row_str = "|"
        for j in range(len(maze[0])):
            if maze[i][j] == 0:
                row_str += "   "
            elif maze[i][j] == 1:
                row_str += " X "
            elif maze[i][j] == 2:
                row_str += "   "
            row_str += "|"
        print(row_str)
        print("+" + "---+" * len(maze[0]))

# prompt the user to input the values of N, M, and num_obstacles
N = int(input("Enter the number of rows (N): "))
M = int(input("Enter the number of columns (M): "))
max_possible_obs = N*M-(N+M-1)
num_obstacles = int(input("Enter the number of obstacles (0-" + str(max_possible_obs) + "): "))
while num_obstacles < 0 or num_obstacles > max_possible_obs:
    num_obstacles = int(input("Re-enter again (0-" + str(max_possible_obs) + "): "))

# generate the maze using the user-specified values
maze = generate_maze(N, M, num_obstacles)

# print the generated maze as a grid to the console
print("Generated Maze Map:")
print_maze(maze)
