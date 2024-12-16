from_file = True
input = 2
print_steps = False
robot_pos = (0,0)
warehouse = []
moves = ""
if not from_file:
    if input == 1:
        warehouse = [
            ["#","#","#","#","#","#","#","#"],
            ["#",".",".","O",".","O",".","#"],
            ["#","#","@",".","O",".",".","#"],
            ["#",".",".",".","O",".",".","#"],
            ["#",".","#",".","O",".",".","#"],
            ["#",".",".",".","O",".",".","#"],
            ["#",".",".",".",".",".",".","#"],
            ["#","#","#","#","#","#","#","#"]
        ]
        moves = "<^^>>>vv<v>>v<<"
    if input == 2:
        warehouse = [
            ["#","#","#","#","#","#","#","#","#","#"],
            ["#",".",".","O",".",".","O",".","O","#"],
            ["#",".",".",".",".",".",".","O",".","#"],
            ["#",".","O","O",".",".","O",".","O","#"],
            ["#",".",".","O","@",".",".","O",".","#"],
            ["#","O","#",".",".","O",".",".",".","#"],
            ["#","O",".",".","O",".",".","O",".","#"],
            ["#",".","O","O",".","O",".","O","O","#"],
            ["#",".",".",".",".","O",".",".",".","#"],
            ["#","#","#","#","#","#","#","#","#","#"]
        ]
        moves = "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"
else:
    with open("day 15/input.txt", "r", encoding="utf-8") as f:
        reading_map = True
        for line in f:
            if line == "\n":
                reading_map = False
                continue
            if reading_map:
                line = line.strip()
                map_row = []
                for char in line:
                    map_row.append(char)
                warehouse.append(map_row)
            else:
                line = line.strip()
                moves += line

def find_robot() -> tuple:
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == "@":
                return (i, j)
            
def move_boxes(dire) -> bool:
    global robot_pos
    x,y = robot_pos
    if dire == "<":
        col = y - 1
        while warehouse[x][col] == "O":
            col -= 1
        if warehouse[x][col] == ".":
            warehouse[x][col] = "O"
            return True
        return False
    if dire == ">":
        col = y + 1
        while warehouse[x][col] == "O":
            col += 1
        if warehouse[x][col] == ".":
            warehouse[x][col] = "O"
            return True
        return False
    if dire == "v":
        row = x + 1
        while warehouse[row][y] == "O":
            row += 1
        if warehouse[row][y] == ".":
            warehouse[row][y] = "O"
            return True
        return False
    if dire == "^":
        row = x - 1
        while warehouse[row][y] == "O":
            row -= 1
        if warehouse[row][y] == ".":
            warehouse[row][y] = "O"
            return True
        return False
    
def move_robot(dire):
    global robot_pos
    x,y = robot_pos
    if dire == "<":
        if warehouse[x][y-1] == ".":
            robot_pos = (x, y-1)
            warehouse[x][y-1] = "@"
            warehouse[x][y] = "."
        if warehouse[x][y-1] == "O":
            pushable = move_boxes(dire)
            if pushable:
                robot_pos = (x, y-1)
                warehouse[x][y-1] = "@"
                warehouse[x][y] = "."
    if dire == ">":
        if warehouse[x][y+1] == ".":
            robot_pos = (x, y+1)
            warehouse[x][y+1] = "@"
            warehouse[x][y] = "."
        if warehouse[x][y+1] == "O":
            pushable = move_boxes(dire)
            if pushable:
                robot_pos = (x, y+1)
                warehouse[x][y+1] = "@"
                warehouse[x][y] = "."
    if dire == "^":
        if warehouse[x-1][y] == ".":
            robot_pos = (x-1, y)
            warehouse[x-1][y] = "@"
            warehouse[x][y] = "."
        if warehouse[x-1][y] == "O":
            pushable = move_boxes(dire)
            if pushable:
                robot_pos = (x-1, y)
                warehouse[x-1][y] = "@"
                warehouse[x][y] = "."
    if dire == "v":
        if warehouse[x+1][y] == ".":
            robot_pos = (x+1, y)
            warehouse[x+1][y] = "@"
            warehouse[x][y] = "."
        if warehouse[x+1][y] == "O":
            pushable = move_boxes(dire)
            if pushable:
                robot_pos = (x+1, y)
                warehouse[x+1][y] = "@"
                warehouse[x][y] = "."

def print_warehouse():
    for row in warehouse:
        output = ""
        for char in row:
            output += char
        print(output)
    print()

def sum_of_boxes():
    total = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == "O":
                total += 100*i + j
    return total

def run():
    global robot_pos
    robot_pos = find_robot()
    for dire in moves:
        move_robot(dire)
        if print_steps:
            print("Move " + dire + ":\nRobot position: " + str(robot_pos))
            print_warehouse()
    print(sum_of_boxes())

run()


#part 1: 1538871 CORRECT
    


