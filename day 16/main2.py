from math import inf
from functools import cache
import matplotlib.pyplot as plt
import numpy as np

#global variables
maze = []
stack = []
cost_matrix = None
start_pos = None
finish_pos = None

def read_maze(from_file, maze_num = 1):
    global maze
    if not from_file:
        if maze_num == 1:
            maze = [
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                ["#",".",".",".",".",".",".",".","#",".",".",".",".","E","#"],
                ["#",".","#",".","#","#","#",".","#",".","#","#","#",".","#"],
                ["#",".",".",".",".",".","#",".","#",".",".",".","#",".","#"],
                ["#",".","#","#","#",".","#","#","#","#","#",".","#",".","#"],
                ["#",".","#",".","#",".",".",".",".",".",".",".","#",".","#"],
                ["#",".","#",".","#","#","#","#","#",".","#","#","#",".","#"],
                ["#",".",".",".",".",".",".",".",".",".",".",".","#",".","#"],
                ["#","#","#",".","#",".","#","#","#","#","#",".","#",".","#"],
                ["#",".",".",".","#",".",".",".",".",".","#",".","#",".","#"],
                ["#",".","#",".","#",".","#","#","#",".","#",".","#",".","#"],
                ["#",".",".",".",".",".","#",".",".",".","#",".","#",".","#"],
                ["#",".","#","#","#",".","#",".","#",".","#",".","#",".","#"],
                ["#","S",".",".","#",".",".",".",".",".","#",".",".",".","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
            ]
        elif maze_num == 2:
            maze = [
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                ["#",".",".",".","#",".",".",".","#",".",".",".","#",".",".","E","#"],
                ["#",".","#",".","#",".","#",".","#",".","#",".","#",".","#",".","#"],
                ["#",".","#",".","#",".","#",".",".",".","#",".",".",".","#",".","#"],
                ["#",".","#",".","#",".","#",".","#","#","#",".","#",".","#",".","#"],
                ["#",".",".",".","#",".","#",".","#",".",".",".",".",".","#",".","#"],
                ["#",".","#",".","#",".","#",".","#",".","#","#","#","#","#",".","#"],
                ["#",".","#",".",".",".","#",".","#",".","#",".",".",".",".",".","#"],
                ["#",".","#",".","#","#","#","#","#",".","#",".","#","#","#",".","#"],
                ["#",".","#",".","#",".",".",".",".",".",".",".","#",".",".",".","#"],
                ["#",".","#",".","#","#","#",".","#","#","#","#","#",".","#","#","#"],
                ["#",".","#",".","#",".",".",".","#",".",".",".",".",".","#",".","#"],
                ["#",".","#",".","#",".","#","#","#","#","#",".","#","#","#",".","#"],
                ["#",".","#",".","#",".",".",".",".",".",".",".",".",".","#",".","#"],
                ["#",".","#",".","#",".","#","#","#","#","#","#","#","#","#",".","#"],
                ["#","S","#",".",".",".",".",".",".",".",".",".",".",".",".",".","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
            ]
        elif maze_num == 3:
            maze = [
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",".",".","E","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",".",".","#",".","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",".",".","#","#",".","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",".",".","#","#","#",".","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",".",".","#","#",".",".",".","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",".",".","#","#","#",".","#","#","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",".",".","#","#","#","#",".",".",".","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",".",".","#","#","#","#","#","#","#",".","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",".",".","#","#",".",".",".",".",".",".",".","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#",".",".","#","#","#",".","#","#","#","#","#","#","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#",".",".","#","#","#","#",".",".",".",".",".",".",".","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#",".",".","#","#","#","#","#","#","#","#","#","#","#",".","#"],
                ["#","#","#","#","#","#","#","#","#","#","#",".",".","#","#",".",".",".",".",".",".",".",".",".",".",".","#"],
                ["#","#","#","#","#","#","#","#","#","#",".",".","#","#","#",".","#","#","#","#","#","#","#","#","#","#","#"],
                ["#","#","#","#","#","#","#","#","#",".",".","#","#","#","#",".",".",".",".",".",".",".",".",".",".",".","#"],
                ["#","#","#","#","#","#","#","#",".",".","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",".","#"],
                ["#","#","#","#","#","#","#",".",".","#","#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#"],
                ["#","#","#","#","#","#",".",".","#","#","#",".","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                ["#","#","#","#","#",".",".","#","#","#","#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#"],
                ["#","#","#","#",".",".","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",".","#"],
                ["#","#","#",".",".","#","#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#"],
                ["#","#",".",".","#","#","#",".","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                ["#",".",".","#","#","#","#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#"],
                ["#",".","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",".","#"],
                ["#","S",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
            ]
    else:
        with open("day 16/input.txt", "r", encoding="utf-8") as f:
            for line in f:
                row = []
                for char in line.strip():
                    row.append(char)
                maze.append(row)

def get_finish_pos():
    global maze
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "E":
                return (i,j)
    raise Exception("Finish point not found ERROR")

def get_start_pos():
    global maze
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                return (i,j)
    raise Exception("Start point not found ERROR")

def print_cost_matrix():
    for row in cost_matrix:
        for item in row:
            if item == inf:
                print("#####",end=" ")
            else:
                if item < 10:
                    print(f"    {item}", end=" ")
                elif item < 100:
                    print(f"   {item}", end=" ")
                elif item < 1000:
                    print(f"  {item}", end=" ")
                elif item < 10000:
                    print(f" {item}", end=" ")
                else:
                    print(item,end=" ")
        print()
    print()

@cache
def is_corner(pos1, pos2, pos3):
    if (pos1[0] == pos2[0] and pos2[0] == pos3[0]):
        return False
    if (pos1[1] == pos2[1] and pos2[1] == pos3[1]):
        return False
    return True

def find_path():
    stack.extend([(start_pos[0],start_pos[1] - 1), start_pos])
    cost_matrix[start_pos[0]][start_pos[1]] = 0
    while len(stack) > 1:
        current_pos = stack[-1]
        prev_pos = stack[-2]
        cx, cy = current_pos
        if (maze[cx][cy + 1] == "." or maze[cx][cy + 1] == "E") and cost_matrix[cx][cy + 1] > cost_matrix[cx][cy] + 1 + 1000 * is_corner(prev_pos, current_pos, (cx, cy + 1)):
            stack.append((cx, cy + 1))
            cost_matrix[cx][cy + 1] = cost_matrix[cx][cy] + 1 + 1000 * is_corner(prev_pos, current_pos, (cx, cy + 1))
        elif (maze[cx][cy - 1] == "." or maze[cx][cy - 1] == "E") and cost_matrix[cx][cy - 1] > cost_matrix[cx][cy] + 1 + 1000 * is_corner(prev_pos, current_pos, (cx, cy - 1)):
            stack.append((cx, cy - 1))
            cost_matrix[cx][cy - 1] = cost_matrix[cx][cy] + 1 + 1000 * is_corner(prev_pos, current_pos, (cx, cy - 1))
        elif (maze[cx + 1][cy] == "." or maze[cx + 1][cy] == "E") and cost_matrix[cx + 1][cy] > cost_matrix[cx][cy] + 1 + 1000 * is_corner(prev_pos, current_pos, (cx + 1, cy)):
            stack.append((cx + 1, cy))
            cost_matrix[cx + 1][cy] = cost_matrix[cx][cy] + 1 + 1000 * is_corner(prev_pos, current_pos, (cx + 1, cy))
        elif (maze[cx - 1][cy] == "." or maze[cx - 1][cy] == "E") and cost_matrix[cx - 1][cy] > cost_matrix[cx][cy] + 1 + 1000 * is_corner(prev_pos, current_pos, (cx - 1, cy)):
            stack.append((cx - 1, cy))
            cost_matrix[cx - 1][cy] = cost_matrix[cx][cy] + 1 + 1000 * is_corner(prev_pos, current_pos, (cx - 1, cy))
        else:
            stack.pop()

read_maze(True, 3)
cost_matrix = [[inf for j in range(len(maze[0]))] for i in range(len(maze))]
start_pos = get_start_pos()
finish_pos = get_finish_pos()
find_path()
print(cost_matrix[finish_pos[0]][finish_pos[1]])

#part 1: 130536 CORRECT

        



