from math import inf
import sys
sys.setrecursionlimit(30000)

maze = []
cost_matrix = []
distance_cost_matrix = []
def read_maze(from_file):
    global maze, cost_matrix, distance_cost_matrix
    if not from_file:
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
    x,y = pos
    right = cost_matrix[x][y+1]
    left  = cost_matrix[x][y-1]
    up    = cost_matrix[x-1][y]
    down  = cost_matrix[x+1][y]
    dire = ">"
    if left <= up and left <= down and left < right and left != inf:
        dire = "<"
    elif down <= up and down <= left and down < right and down != inf:
        dire = "v"
    elif up <= down and up <= left and up < right and up != inf:
        dire = "^"
    elif right != inf:
        dire = ">"
    else:
        raise Exception("DeadEndError")
    return dire

def ghg(pos):
    global finish_pos, cost_matrix
    print(pos)
    print(cost_matrix[pos[0]][pos[1]])
    input()
    if pos == finish_pos:
        return 0
    else:
        dire = find_cheapest_neighbour(pos)
        x,y = pos
        cost_matrix[x][y] = inf
        if dire == "<":
            return 1 + ghg((x,y-1))
        elif dire == ">":
            return 1 + ghg((x,y+1))
        elif dire == "^":
            return 1 + ghg((x-1,y))
        elif dire == "v":
            return 1 + ghg((x+1,y))


def go_horsey_go():
    global maze, cost_matrix
    x,y = get_start_pos()
    turn_cost = cost_matrix[x][y]
    distance = ghg((x,y))
    print(distance + turn_cost)

read_maze(True)
finish_pos = get_finish_pos()

make_turn_cost_matrix()
#print_cost_matrix()
make_distance_cost_matrix()
#print_distance_cost_matrix()
go_horsey_go()
