from_file = True
print_steps = False
maze = 1
robot_pos = (0,0)
warehouse = []
moves = ""
if not from_file:
    if maze == 1:
        warehouse = [
            ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
            ["#","#",".",".",".",".","[","]",".",".",".",".","[","]",".",".","[","]","#","#"],
            ["#","#",".",".",".",".",".",".",".",".",".",".",".",".","[","]",".",".","#","#"],
            ["#","#",".",".","[","]","[","]",".",".",".",".","[","]",".",".","[","]","#","#"],
            ["#","#",".",".",".",".","[","]","@",".",".",".",".",".","[","]",".",".","#","#"],
            ["#","#","[","]","#","#",".",".",".",".","[","]",".",".",".",".",".",".","#","#"],
            ["#","#","[","]",".",".",".",".","[","]",".",".",".",".","[","]",".",".","#","#"],
            ["#","#",".",".","[","]","[","]",".",".","[","]",".",".","[","]","[","]","#","#"],
            ["#","#",".",".",".",".",".",".",".",".","[","]",".",".",".",".",".",".","#","#"],
            ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
        ]
    if maze == 2:
        warehouse = [
            ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
            ["#","#","[","]",".",".",".",".",".",".",".","[","]",".","[","]","[","]","#","#"],
            ["#","#","[","]",".",".",".",".",".",".",".",".",".",".",".","[","]",".","#","#"],
            ["#","#","[","]",".",".",".",".",".",".",".",".","[","]","[","]","[","]","#","#"],
            ["#","#","[","]",".",".",".",".",".",".","[","]",".",".",".",".","[","]","#","#"],
            ["#","#",".",".","#","#",".",".",".",".",".",".","[","]",".",".",".",".","#","#"],
            ["#","#",".",".","[","]",".",".",".",".",".",".",".",".",".",".",".",".","#","#"],
            ["#","#",".",".","@",".",".",".",".",".",".","[","]",".","[","]","[","]","#","#"],
            ["#","#",".",".",".",".",".",".","[","]","[","]",".",".","[","]",".",".","#","#"],
            ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
        ]
    if maze == 3:
        warehouse = [
            ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
            ["#","#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#","#"],
            ["#","#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#","#"],
            ["#","#",".",".",".",".",".","[","]","[","]","[","]",".",".",".",".",".","#","#"],
            ["#","#",".",".",".",".",".",".","[","]","[","]",".",".",".",".",".",".","#","#"],
            ["#","#",".",".","#","#",".",".",".","[","]","@",".",".",".",".",".",".","#","#"],
            ["#","#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#","#"],
            ["#","#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#","#"],
            ["#","#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#","#"],
            ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
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

def convert_warehouse():
    global warehouse
    new_warehouse = []
    for i in range(len(warehouse)):
        new_warehouse_row = []
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == "#":
                new_warehouse_row.append("#")
                new_warehouse_row.append("#")
            elif warehouse[i][j] == "O":
                new_warehouse_row.append("[")
                new_warehouse_row.append("]")
            elif warehouse[i][j] == ".":
                new_warehouse_row.append(".")
                new_warehouse_row.append(".")
            else:
                new_warehouse_row.append("@")
                new_warehouse_row.append(".")
        new_warehouse.append(new_warehouse_row)
    warehouse = new_warehouse.copy()

def find_robot() -> tuple:
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == "@":
                return (i, j)
            
def can_move_box(pos, dire):
    x1, y1 = pos
    x2, y2 = pos[0], pos[1] + 1   
    if dire == "^":
        if warehouse[x1-1][y1] == "." and warehouse[x2-1][y2] == ".":
            return True
        elif warehouse[x1-1][y1] == "#" or warehouse[x2-1][y2] == "#":
            return False
        elif warehouse[x1-1][y1] == "[":
            return True and can_move_box((x1-1,y1), dire)
        elif warehouse[x1-1][y1] == "]" and warehouse[x1-1][y2] == "[":
            return True and can_move_box((x1-1,y1-1), dire) and can_move_box((x1-1,y2), dire)
        elif warehouse[x1-1][y1] == "]":
            return True and can_move_box((x1-1,y1-1), dire)
        elif warehouse[x1-1][y2] == "[":
            return True and can_move_box((x1-1,y2),dire)
    if dire == "v":
        if warehouse[x1+1][y1] == "." and warehouse[x2+1][y2] == ".":
            return True
        elif warehouse[x1+1][y1] == "#" or warehouse[x2+1][y2] == "#":
            return False
        elif warehouse[x1+1][y1] == "[":
            return True and can_move_box((x1+1,y1), dire)
        elif warehouse[x1+1][y1] == "]" and warehouse[x1+1][y2] == "[":
            return True and can_move_box((x1+1,y1-1), dire) and can_move_box((x1+1,y2), dire)
        elif warehouse[x1+1][y1] == "]":
            return True and can_move_box((x1+1,y1-1), dire)
        elif warehouse[x1+1][y2] == "[":
            return True and can_move_box((x1+1,y2),dire)
    if dire == "<":
        if warehouse[x1][y1-1] == ".":
            return True
        elif warehouse[x1][y1-1] == "#":
            return False
        elif warehouse[x1][y1-1] == "]":
            return True and can_move_box((x1, y1-2), dire)
    if dire == ">":
        if warehouse[x1][y1+2] == ".":
            return True
        elif warehouse[x1][y1+2] == "#":
            return False
        elif warehouse[x1][y1+2] == "[":
            return True and can_move_box((x1, y1+2), dire)

def move_box(pos, dire):
    x,y = pos
    if dire == "^":
        if warehouse[x-1][y] == "[":
            move_box((x-1,y), dire)
            warehouse[x-1][y] = "["
            warehouse[x-1][y+1] = "]"
            warehouse[x][y] = "."
            warehouse[x][y+1] = "."
        elif warehouse[x-1][y] == "]" and warehouse[x-1][y+1] == "[":
            move_box((x-1, y-1), dire)
            move_box((x-1, y+1), dire)
            warehouse[x-1][y] = "["
            warehouse[x-1][y+1] = "]"
            warehouse[x][y] = "."
            warehouse[x][y+1] = "."
        elif warehouse[x-1][y] == "]":
            move_box((x-1, y-1), dire)
            warehouse[x-1][y] = "["
            warehouse[x-1][y+1] = "]"
            warehouse[x][y] = "."
            warehouse[x][y+1] = "."
        elif warehouse[x-1][y+1] == "[":
            move_box((x-1, y+1), dire)
            warehouse[x-1][y] = "["
            warehouse[x-1][y+1] = "]"
            warehouse[x][y] = "."
            warehouse[x][y+1] = "."
        elif warehouse[x-1][y] == "." and warehouse[x-1][y+1] == ".":
            warehouse[x-1][y] = "["
            warehouse[x-1][y+1] = "]"
            warehouse[x][y] = "."
            warehouse[x][y+1] = "."
    if dire == "v":
        if warehouse[x+1][y] == "[":
            move_box((x+1,y), dire)
            warehouse[x+1][y] = "["
            warehouse[x+1][y+1] = "]"
            warehouse[x][y] = "."
            warehouse[x][y+1] = "."
        elif warehouse[x+1][y] == "]" and warehouse[x+1][y+1] == "[":
            move_box((x+1, y-1), dire)
            move_box((x+1, y+1), dire)
            warehouse[x+1][y] = "["
            warehouse[x+1][y+1] = "]"
            warehouse[x][y] = "."
            warehouse[x][y+1] = "."
        elif warehouse[x+1][y] == "]":
            move_box((x+1, y-1), dire)
            warehouse[x+1][y] = "["
            warehouse[x+1][y+1] = "]"
            warehouse[x][y] = "."
            warehouse[x][y+1] = "."
        elif warehouse[x+1][y+1] == "[":
            move_box((x+1, y+1), dire)
            warehouse[x+1][y] = "["
            warehouse[x+1][y+1] = "]"
            warehouse[x][y] = "."
            warehouse[x][y+1] = "."
        elif warehouse[x+1][y] == "." and warehouse[x+1][y+1] == ".":
            warehouse[x+1][y] = "["
            warehouse[x+1][y+1] = "]"
            warehouse[x][y] = "."
            warehouse[x][y+1] = "."
    if dire == ">":
        if warehouse[x][y+2] == "[":
            move_box((x, y+2), dire)
            warehouse[x][y] = "."
            warehouse[x][y+1] = "["
            warehouse[x][y+2] = "]"
        else:
            warehouse[x][y] = "."
            warehouse[x][y+1] = "["
            warehouse[x][y+2] = "]"
    if dire == "<":
        if warehouse[x][y-1] == "]":
            move_box((x, y-2), dire)
            warehouse[x][y] = "]"
            warehouse[x][y+1] = "."
            warehouse[x][y-1] = "["
        else:
            warehouse[x][y] = "]"
            warehouse[x][y+1] = "."
            warehouse[x][y-1] = "["
    
def move_robot(dire):
    global robot_pos
    x,y = robot_pos
    if dire == "<":
        if warehouse[x][y-1] == ".":
            robot_pos = (x, y-1)
            warehouse[x][y-1] = "@"
            warehouse[x][y] = "."
        if warehouse[x][y-1] == "]":
            pushable = can_move_box((x,y-2), dire)
            if pushable:
                move_box((x,y-2), dire)
                robot_pos = (x,y-1)
                warehouse[x][y-1] = "@"
                warehouse[x][y] = "."
    if dire == ">":
        if warehouse[x][y+1] == ".":
            robot_pos = (x, y+1)
            warehouse[x][y+1] = "@"
            warehouse[x][y] = "."
        if warehouse[x][y+1] == "[":
            pushable = can_move_box((x,y+1), dire)
            if pushable:
                move_box((x,y+1), dire)
                robot_pos = (x,y+1)
                warehouse[x][y+1] = "@"
                warehouse[x][y] = "."
    if dire == "^":
        if warehouse[x-1][y] == ".":
            robot_pos = (x-1, y)
            warehouse[x-1][y] = "@"
            warehouse[x][y] = "."
        if warehouse[x-1][y] == "]":
            pushable = can_move_box((x-1,y-1), dire)
            if pushable:
                move_box((x-1,y-1), dire)
                robot_pos = (x-1,y)
                warehouse[x-1][y] = "@"
                warehouse[x][y] = "."
        if warehouse[x-1][y] == "[":
            pushable = can_move_box((x-1,y), dire)
            if pushable:
                move_box((x-1,y), dire)
                robot_pos = (x-1,y)
                warehouse[x-1][y] = "@"
                warehouse[x][y] = "."
    if dire == "v":
        if warehouse[x+1][y] == ".":
            robot_pos = (x+1, y)
            warehouse[x+1][y] = "@"
            warehouse[x][y] = "."
        if warehouse[x+1][y] == "]":
            pushable = can_move_box((x+1,y-1), dire)
            if pushable:
                move_box((x+1,y-1), dire)
                robot_pos = (x+1,y)
                warehouse[x+1][y] = "@"
                warehouse[x][y] = "."
        if warehouse[x+1][y] == "[":
            pushable = can_move_box((x+1,y), dire)
            if pushable:
                move_box((x+1,y), dire)
                robot_pos = (x+1,y)
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
            if warehouse[i][j] == "[":
                total += 100*i + j
    return total

def run():
    convert_warehouse()
    print_warehouse()
    global robot_pos
    robot_pos = find_robot()
    for dire in moves:
        move_robot(dire)
        if print_steps:
            print("Move " + dire + ":\nRobot position: " + str(robot_pos))
            print_warehouse()
            input()

    print(sum_of_boxes())

run()

#part 2: 1543338 CORRECT