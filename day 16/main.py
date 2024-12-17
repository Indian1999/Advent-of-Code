from math import inf
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.setrecursionlimit(30000)

maze = []
cost_matrix = []
distance_cost_matrix = []
def read_maze(from_file, maze_num = 1):
    global maze, cost_matrix, distance_cost_matrix
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
    cost_matrix = [[inf for i in range(len(maze[0]))] for j in range(len(maze))]
    distance_cost_matrix = [[inf for i in range(len(maze[0]))] for j in range(len(maze))]


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

def f(pos, dire):
    global maze, cost_matrix
    x, y = pos
    if maze[x][y-1] == ".":
        if dire != ">" and cost_matrix[x][y-1] > cost_matrix[x][y] + 1000:
            cost_matrix[x][y-1] = cost_matrix[x][y] + 1000
            f((x, y-1), ">")
        if dire == ">" and cost_matrix[x][y-1] > cost_matrix[x][y]:
            cost_matrix[x][y-1] = cost_matrix[x][y]
            f((x, y-1), dire)
    if maze[x][y+1] == ".":
        if dire != "<" and cost_matrix[x][y+1] > cost_matrix[x][y] + 1000:
            cost_matrix[x][y+1] = cost_matrix[x][y] + 1000
            f((x, y+1), "<")
        if dire == "<" and cost_matrix[x][y+1] > cost_matrix[x][y]:
            cost_matrix[x][y+1] = cost_matrix[x][y]
            f((x, y+1), dire)
    if maze[x+1][y] == ".":
        if dire != "^" and cost_matrix[x+1][y] > cost_matrix[x][y] + 1000:
            cost_matrix[x+1][y] = cost_matrix[x][y] + 1000
            f((x+1, y), "^")
        if dire == "^" and cost_matrix[x+1][y] > cost_matrix[x][y]:
            cost_matrix[x+1][y] = cost_matrix[x][y]
            f((x+1, y), dire)
    if maze[x-1][y] == ".":
        if dire != "v" and cost_matrix[x-1][y] > cost_matrix[x][y] + 1000:
            cost_matrix[x-1][y] = cost_matrix[x][y] + 1000
            f((x-1, y), "v")
        if dire == "v" and cost_matrix[x-1][y] > cost_matrix[x][y]:
            cost_matrix[x-1][y] = cost_matrix[x][y]
            f((x-1, y), dire)

def make_turn_cost_matrix():
    finish = get_finish_pos()
    cost_matrix[finish[0]][finish[1]] = 0
    f(finish, "^")
    f(finish, ">")
    f(finish, "<")
    f(finish, "v")
    x,y = get_start_pos()
    dire = find_cheapest_neighbour((x,y))
    if dire == ">":
        cost_matrix[x][y] = cost_matrix[x][y+1]
    if dire == "<":
        cost_matrix[x][y] = cost_matrix[x][y-1] + 1000
    if dire == "v":
        cost_matrix[x][y] = cost_matrix[x+1][y] + 1000
    if dire == "^":
        cost_matrix[x][y] = cost_matrix[x-1][y] + 1000

def fd(pos):
    global maze, distance_cost_matrix
    x, y = pos
    if maze[x][y-1] == ".":
        if distance_cost_matrix[x][y-1] > distance_cost_matrix[x][y] + 1:
            distance_cost_matrix[x][y-1] = distance_cost_matrix[x][y] + 1
            fd((x,y-1))
    if maze[x][y+1] == ".":
        if distance_cost_matrix[x][y+1] > distance_cost_matrix[x][y] + 1:
            distance_cost_matrix[x][y+1] = distance_cost_matrix[x][y] + 1
            fd((x,y+1))
    if maze[x-1][y] == ".":
        if distance_cost_matrix[x-1][y] > distance_cost_matrix[x][y] + 1:
            distance_cost_matrix[x-1][y] = distance_cost_matrix[x][y] + 1
            fd((x-1,y))
    if maze[x+1][y] == ".":
        if distance_cost_matrix[x+1][y] > distance_cost_matrix[x][y] + 1:
            distance_cost_matrix[x+1][y] = distance_cost_matrix[x][y] + 1
            fd((x+1,y))


def make_distance_cost_matrix():
    global distance_cost_matrix, cost_matrix
    finish = get_finish_pos()
    distance_cost_matrix[finish[0]][finish[1]] = 0
    fd(finish)

def print_cost_matrix():
    for row in cost_matrix:
        for item in row:
            if item == inf:
                print("####",end=" ")
            else:
                if item < 1000:
                    print(f"   {item}", end=" ")
                else:
                    print(item,end=" ")
        print()
    print()

def print_distance_cost_matrix():
    for row in distance_cost_matrix:
        for item in row:
            if item == inf:
                print("##",end=" ")
            else:
                if item < 10:
                    print(f" {item}", end=" ")
                else:
                    print(item,end=" ")
        print()
    print()

def find_cheapest_neighbour(pos):
    global distance_cost_matrix
    x,y = pos
    right = cost_matrix[x][y+1]
    left  = cost_matrix[x][y-1]
    up    = cost_matrix[x-1][y]
    down  = cost_matrix[x+1][y]
    right_distance = distance_cost_matrix[x][y+1]
    left_distance  = distance_cost_matrix[x][y-1]
    up_distance    = distance_cost_matrix[x-1][y]
    down_distance  = distance_cost_matrix[x+1][y]
    if right_distance != inf:
        right += right_distance
    if left_distance != inf:
        left += left_distance
    if up_distance != inf:
        up += up_distance
    if down_distance != inf:
        down += down_distance
    dire = ">"
    if left <= up and left <= down and left < right and left != inf:
        dire = "<"
    elif up <= down and up <= left and up < right and up != inf:
        dire = "^"
    elif down <= up and down <= left and down < right and down != inf:
        dire = "v"
    elif right != inf:
        dire = ">"
    else:
        raise Exception("DeadEndError")
    return dire

def ghg(pos, stack):
    global finish_pos, cost_matrix, distance_cost_matrix, path_matrix
    stack.append(pos)
    if pos == finish_pos:
        plot_stack(stack)
        return 0
    else:
        x,y = pos
        cost_matrix[x][y] = inf
        try:
            dire = find_cheapest_neighbour(pos)
        except Exception:
            stack.pop()
            return -1 + ghg(stack.pop(), stack)
        if dire == "<":
            return 1 + ghg((x,y-1), stack)
        elif dire == ">":
            return 1 + ghg((x,y+1), stack)
        elif dire == "^":
            return 1 + ghg((x-1,y), stack)
        elif dire == "v":
            return 1 + ghg((x+1,y), stack)


def go_horsey_go():
    global maze, cost_matrix, distance_cost_matrix
    x,y = get_start_pos()
    turn_cost = cost_matrix[x][y]
    stack = [(x,y)]
    distance = ghg((x,y), stack)
    print(distance + turn_cost)

def plot_stack(stack):
    x,y = zip(*stack)
    plt.scatter(y,x)
    plt.gca().invert_yaxis()
    plt.savefig("day 16/my-maze-output.png")

read_maze(True, 3)
finish_pos = get_finish_pos()

make_turn_cost_matrix()
#print_cost_matrix()
make_distance_cost_matrix()
#print_distance_cost_matrix()
go_horsey_go()

#part1: 130816 INCORRECT (too high)
#part1: 130608 INCORRECT (too high)
#part1: 130556 INCORRECT (too high)
