# import random

def generate_path(maze, N, M):
    # This function generates a random path through an NxM maze, represented as a dictionary. The keys are (i, j) tuples representing
    # coordinates of each cell in the maze and the values are integers: 0 for empty, 1 for obstacle, and 2 for path. The path starts 
    # from (0,0) and ends at (N-1,M-1), and the direction (right or down) at each step is chosen randomly.

    # your code here


def add_obstacles(maze, min_obstacles, N, M):
    # This function randomly adds obstacles (represented as 1) to the empty cells (represented as 0) in the given maze until at least
    # min_obstacles have been added. If a KeyError occurs while trying to set an obstacle, it is caught and a message is printed.

    # your code here
    

def set_obstacle(maze, N, M):
    # This function allows a user to manually set an obstacle in the maze. The user is prompted to input the coordinates of the cell
    # where they want to place the obstacle. If the cell is part of the path or an obstacle is already present, an error message is 
    # displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here


def remove_obstacle(maze, N, M):
    # This function allows a user to manually remove an obstacle from the maze. The user is prompted to input the coordinates of the 
    # cell where they want to remove the obstacle. If the cell is part of the path or there's no obstacle at the given cell, an error 
    # message is displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here


def print_maze(maze, N, M):
    # This function prints the current state of the maze in a grid-like format. Each cell is represented by a 3-character string: 
    # '   ' for empty cells, ' X ' for obstacles, and ' O ' for path cells.

    # your code here
    


def main():
    # This function serves as the main driver of the program. It reads the maze dimensions from a file, asks the user for the minimum 
    # number of obstacles to be added, generates the path and adds the obstacles, and then enters a loop where the user can choose to 
    # set or remove obstacles, print the maze, or exit the program. Exceptions for ValueError, IOError, and NameError are handled.

    # your code here
    #load the grids
    while True:
        filename = input("Enter the file name: ")
        try:
            with open(filename, "r") as fr:
                grid = [list(line.strip()) for line in fr if line.strip()]
        except IOError:
            print("IOError occured in main function. File not found Please enter a valid file name")
        else:
            break

    #initialize the maze
    N=0
    M=0
    for i in grid[1]:
        if i =="|":
            N+=1
    N=N-1 #calculate the number of row

    for i in grid():
        if i[0] =="+":
            M+=1
    M=M-1 #num of col

    maze ={}
    col_index = -1
    row_index = -1

    for i in grid:
        if i[0] == "+":
            row_index+=1
            continue

        for char in i:
            if char =="|" and col_index<=M:
                col_index+=1
                maze[(row_index,col_index)] 




main()

