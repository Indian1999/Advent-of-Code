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
    if pos[0] >= 0 and pos[0] < len(matrix) and pos[1] >= 0 and pos[1] < len(matrix[0]):
        return True
    return False

for type, list in antennas.items():
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            a = list[i]
            b = list[j]
            if a not in antinodes:
                antinodes.append(a)
            if b not in antinodes:
                antinodes.append(b)
            ab = (b[0]-a[0], b[1]-a[1])
            c = (a[0] - ab[0], a[1] - ab[1])
            d = (b[0] + ab[0], b[1] + ab[1])
            while is_valid_pos(c):
                if c not in antinodes:
                    antinodes.append(c)
                c = (c[0] - ab[0], c[1] - ab[1])
            while is_valid_pos(d):
                if d not in antinodes:
                    antinodes.append(d)
                d = (d[0] + ab[0], d[1] + ab[1])
"""for antinode in antinodes:
    if matrix[antinode[0]][antinode[1]] == ".":
        matrix[antinode[0]][antinode[1]] = "#"
for row in matrix:
    print("".join(row))"""
print(len(antinodes))