antennas = {}
matrix = []
from_file = True
if not from_file:
    matrix = [
        [".",".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","0",".",".","."],
        [".",".",".",".",".","0",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","0",".",".",".","."],
        [".",".",".",".","0",".",".",".",".",".",".","."],
        [".",".",".",".",".",".","A",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","A",".",".","."],
        [".",".",".",".",".",".",".",".",".","A",".","."],
        [".",".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".",".",".","."]
    ]
else:
    with open("day 8/input.txt", "r", encoding="utf-8") as f:
        for line in f:
            matrix.append(list(line.strip()))

antinodes = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != ".":
            if matrix[i][j] in antennas:
                antennas[matrix[i][j]].append((i,j))
            else:
                antennas[matrix[i][j]] = [(i,j)]

def is_valid_pos(pos):
    if pos[0] >= 0 and pos[0] < len(matrix[0]) and pos[1] >= 0 and pos[1] < len(matrix):
        return True
    return False

for type, list in antennas.items():
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            a = list[i]
            b = list[j]
            ab = (b[0]-a[0], b[1]-a[1])
            c = (a[0] - ab[0], a[1] - ab[1])
            d = (b[0] + ab[0], b[1] + ab[1])
            #print(f"a = {a}, b = {b}, ab = {ab}, c = {c}, d = {d}")
            if c not in antinodes and is_valid_pos(c):
                antinodes.append(c)
            if d not in antinodes and is_valid_pos(d):
                antinodes.append(d)
print(len(antinodes))

#part 1: 351 CORRECT