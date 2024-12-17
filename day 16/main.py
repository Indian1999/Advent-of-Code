from math import inf

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
        if dire != ">" and cost_matrix[x][y-1] > cost_matrix[x][y] + 1:
            cost_matrix[x][y-1] = cost_matrix[x][y] + 1
            f((x, y-1), ">")
        if dire == ">" and cost_matrix[x][y-1] > cost_matrix[x][y]:
            cost_matrix[x][y-1] = cost_matrix[x][y]
            f((x, y-1), dire)
    if maze[x][y+1] == ".":
        if dire != "<" and cost_matrix[x][y+1] > cost_matrix[x][y] + 1:
            cost_matrix[x][y+1] = cost_matrix[x][y] + 1
            f((x, y+1), "<")
        if dire == "<" and cost_matrix[x][y+1] > cost_matrix[x][y]:
            cost_matrix[x][y+1] = cost_matrix[x][y]
            f((x, y+1), dire)
    if maze[x+1][y] == ".":
        if dire != "^" and cost_matrix[x+1][y] > cost_matrix[x][y] + 1:
            cost_matrix[x+1][y] = cost_matrix[x][y] + 1
            f((x+1, y), "^")
        if dire == "^" and cost_matrix[x+1][y] > cost_matrix[x][y]:
            cost_matrix[x+1][y] = cost_matrix[x][y]
            f((x+1, y), dire)
    if maze[x-1][y] == ".":
        if dire != "v" and cost_matrix[x-1][y] > cost_matrix[x][y] + 1:
            cost_matrix[x-1][y] = cost_matrix[x][y] + 1
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

def fd(pos):
    global maze, distance_cost_matrix
    x, y = pos
    if maze[x][y-1] == ".":
        if distance_cost_matrix[x][y-1] > distance_cost_matrix[x][y] + 1 + 1000*cost_matrix[x][y]:
            distance_cost_matrix[x][y-1] = distance_cost_matrix[x][y] + 1 + 1000*cost_matrix[x][y]
            fd((x,y-1))
    if maze[x][y+1] == ".":
        if distance_cost_matrix[x][y+1] > distance_cost_matrix[x][y] + 1 + 1000*cost_matrix[x][y]:
            distance_cost_matrix[x][y+1] = distance_cost_matrix[x][y] + 1 + 1000*cost_matrix[x][y]
            fd((x,y+1))
    if maze[x-1][y] == ".":
        if distance_cost_matrix[x-1][y] > distance_cost_matrix[x][y] + 1 + 1000*cost_matrix[x][y]:
            distance_cost_matrix[x-1][y] = distance_cost_matrix[x][y] + 1 + 1000*cost_matrix[x][y]
            fd((x-1,y))
    if maze[x+1][y] == ".":
        if distance_cost_matrix[x+1][y] > distance_cost_matrix[x][y] + 1 + 1000*cost_matrix[x][y]:
            distance_cost_matrix[x+1][y] = distance_cost_matrix[x][y] + 1 + 1000*cost_matrix[x][y]
            fd((x+1,y))


def make_distance_cost_matrix():
    global distance_cost_matrix
    finish = get_finish_pos()
    distance_cost_matrix[finish[0]][finish[1]] = 0
    fd(finish)

def print_cost_matrix():
    for row in cost_matrix:
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

def go_horsey_go():
    global maze, cost_matrix
    x,y = get_start_pos()
    #right = (cost_matrix[x][y+1] + 0) * 1000 + distance_cost_matrix[x][y+1]
    #left  = (cost_matrix[x][y-1] + 1) * 1000 + distance_cost_matrix[x][y-1]
    #up    = (cost_matrix[x-1][y] + 1) * 1000 + distance_cost_matrix[x-1][y]
    #down  = (cost_matrix[x+1][y] + 1) * 1000 + distance_cost_matrix[x+1][y]
    right = distance_cost_matrix[x][y+1]
    left  = distance_cost_matrix[x][y-1]
    up    = distance_cost_matrix[x-1][y]
    down  = distance_cost_matrix[x+1][y]
    dire = ">"
    if left <= up and left <= down and left < right:
        dire = "<"
    elif down <= up and down <= left and down < right:
        dire = "v"
    elif up <= down and up <= left and up < right:
        dire = "^"

    if dire == ">":
        print(right)
    elif dire == "<":
        print(left)
    elif dire == "^":
        print(up)
    else:
        print(down)


make_turn_cost_matrix()
#print_cost_matrix()
make_distance_cost_matrix()
#print_distance_cost_matrix()
go_horsey_go()
