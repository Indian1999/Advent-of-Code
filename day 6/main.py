from_file = False
map = []
if not from_file:
    map = [
        [".",".",".",".","#",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","#"],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".","#",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","#",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".","#",".",".","^",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","#","."],
        ["#",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".","#",".",".","."]
    ]
else:
    with open("day 6/input.txt", "r") as f:
        for line in f:
            map.append(list(line.strip()))

def find_guard(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "^" or map[i][j] == ">" or map[i][j] == "<" or map[i][j] == "v":
                return (i,j)
            
def move_guard():
    global guard_pos, map
    x, y = guard_pos
    dire = map[x][y]
    if dire == "^":
        if x == 0:
            map[x][y] = "X"
            return False
        else:
            if map[x-1][y] == "#":
                map[x][y] = ">"
                return True
            else:
                map[x-1][y] = "^"
                map[x][y] = "X"
                guard_pos = (x-1, y)
                return True
    elif dire == "v":
        if x == len(map)-1:
            map[x][y] = "X"
            return False
        else:
            if map[x+1][y] == "#":
                map[x][y] = "<"
                return True
            else:
                map[x+1][y] = "v"
                map[x][y] = "X"
                guard_pos = (x+1, y)
                return True
    elif dire == "<":
        if y == 0:
            map[x][y] = "X"
            return False
        else:
            if map[x][y-1] == "#":
                map[x][y] = "^"
                return True
            else:
                map[x][y-1] = "<"
                map[x][y] = "X"
                guard_pos = (x, y-1)
                return True
    elif dire == ">":
        if y == len(map[0]) - 1:
            map[x][y] = "X"
            return False
        else:
            if map[x][y+1] == "#":
                map[x][y] = "v"
                return True
            else:
                map[x][y+1] = ">"
                map[x][y] = "X"
                guard_pos = (x, y+1)
                return True

def print_map():
    global map
    for row in map:
        print("".join(row))

guard_pos = find_guard(map)
while move_guard():
    pass
    #print_map()
    #input()

total = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "X":
            total += 1


print_map()
print(total)

#part 1: 4647 CORRECT
