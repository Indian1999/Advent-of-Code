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
            #print_cost_matrix()
            f((x, y-1), ">")
        elif cost_matrix[x][y-1] > cost_matrix[x][y]:
            cost_matrix[x][y-1] = cost_matrix[x][y]
            #print_cost_matrix()
            f((x, y-1), dire)
    if maze[x][y+1] == ".":
        if dire != "<" and cost_matrix[x][y+1] > cost_matrix[x][y] + 1:
            cost_matrix[x][y+1] = cost_matrix[x][y] + 1
            #print_cost_matrix()
            f((x, y+1), "<")
        elif cost_matrix[x][y+1] > cost_matrix[x][y]:
            cost_matrix[x][y+1] = cost_matrix[x][y]
            #print_cost_matrix()
            f((x, y+1), dire)
    if maze[x+1][y] == ".":
        if dire != "^" and cost_matrix[x+1][y] > cost_matrix[x][y] + 1:
            cost_matrix[x+1][y] = cost_matrix[x][y] + 1
            #print_cost_matrix()
            f((x+1, y), "^")
        elif cost_matrix[x+1][y] > cost_matrix[x][y]:
            cost_matrix[x+1][y] = cost_matrix[x][y]
            #print_cost_matrix()
            f((x+1, y), dire)
    if maze[x-1][y] == ".":
        if dire != "v" and cost_matrix[x-1][y] > cost_matrix[x][y] + 1:
            cost_matrix[x-1][y] = cost_matrix[x][y] + 1
            #print_cost_matrix()
            f((x-1, y), "v")
        elif cost_matrix[x-1][y] > cost_matrix[x][y]:
            cost_matrix[x-1][y] = cost_matrix[x][y]
            #print_cost_matrix()
            f((x-1, y), dire)



def make_turn_cost_matrix():
    finish = get_finish_pos()
    start = get_start_pos()
    cost_matrix[finish[0]][finish[1]] = 0
    #print_cost_matrix()
    f(finish, "^")
    f(finish, ">")

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
    #input()

make_turn_cost_matrix()
print_cost_matrix()
