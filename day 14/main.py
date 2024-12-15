from_file = True
robots = [
    ((0,4), (3,-3)),
    ((6,3), (-1,-3)),
    ((10,3), (-1,2)),
    ((2,0), (2,-1)),
    ((0,0), (1,3)),
    ((3,0), (-2,-2)),
    ((7,6), (-1,-3)),
    ((3,0), (-1,-2)),
    ((9,3), (2,3)),
    ((7,3), (-1,2)),
    ((2,4), (2,-3)),
    ((9,5), (-3,-3))
]
width = 11
height = 7
if from_file:
    width = 101
    height = 103
    robots = []
    with open("day 14/input.txt", "r", encoding="utf-8") as f:
        # Sample line: p=35,60 v=-8,52
        for line in f:
            line_split = line.split(" v=")
            pos_str = line_split[0][2:]
            vel_str = line_split[1]
            pos_str_split = pos_str.split(",")
            vel_str_split = vel_str.split(",")
            robots.append(
                (
                    (int(pos_str_split[0]), int(pos_str_split[1])),
                    (int(vel_str_split[0]), int(vel_str_split[1]))
                )
            )


def calculate_positions(robots, seconds):
    # Sample robot  (pos, vel) = ((0,4), (3,-3))
    new_positions = []
    for robot in robots:
        new_pos = (robot[0][0] + robot[1][0] * seconds, robot[0][1] + robot[1][1] * seconds)
        new_pos = (new_pos[0] % width, new_pos[1] % height)
        new_positions.append(new_pos)
    return new_positions

def count_robots(robots):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        if robot[0] < width // 2 and robot[1] < height // 2:
            q1 += 1
        if robot[0] > width // 2 and robot[1] < height // 2:
            q2 += 1
        if robot[0] > width // 2 and robot[1] > height // 2:
            q3 += 1
        if robot[0] < width // 2 and robot[1] > height // 2:
            q4 += 1
    print(q1,q2,q3,q4)
    return q1*q2*q3*q4

def robot_matrix(robots):
    robot_matrix = [[0 for i in range(width)] for j in range(height)]
    for pos in robots:
        robot_matrix[pos[1]][pos[0]] += 1
    for row in robot_matrix:
        row[width//2] = " "
    robot_matrix[height//2] = [" " for i in range(int(width*0.7))]
    for row in robot_matrix:
        print(row)
    
new_positions = calculate_positions(robots, 100)
#robot_matrix(new_positions)
print(count_robots(new_positions))

#part 1: 63011520 INCORRECT
#part 1: 221604840 INCORRECT (too low)
#part 1: 225810288 CORRECT
