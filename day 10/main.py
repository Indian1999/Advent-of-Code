def possible_moves(i,j):
    moves = []
    if i > 0 and map[i-1][j] == map[i][j] - 1:
        moves.append("up")
    if i < len(map)-1 and map[i+1][j] == map[i][j] - 1:
        moves.append("down")
    if j < len(map[0])-1 and map[i][j+1] == map[i][j] - 1:
        moves.append("right")
    if j > 0 and map[i][j-1] == map[i][j] - 1:
        moves.append("left")
    return moves

def increment_scores(a,b):
    visited = []
    def f(i,j):
        if (i,j) not in visited:
            score_map[i][j] += 1
            visited.append((i,j))
            moves = possible_moves(i,j)
            if "up" in moves:
                f(i-1,j)
            if "down" in moves:
                f(i+1,j)
            if "left" in moves:
                f(i,j-1)
            if "right" in moves:
                f(i,j+1)
    f(a,b)

def read_file(filename:str) -> list[list[int]]:
    map = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            row = []
            for char in line.strip():
                row.append(int(char))
            map.append(row)
    return map

"""
map = [
    [0,1,2,9,8],
    [2,2,3,3,7],
    [3,5,4,5,6],
    [3,6,7,4,4],
    [4,5,8,3,0],
    [5,1,9,2,1]
] # output: 2 + 1 = 3
"""

map = read_file("day 10/input.txt")
score_map = [[0 for a in range(len(map[0]))] for b in range(len(map))]

for i in range(len(map)):
    for j in range(len(map[i])):
        if (map[i][j] == 9):
            increment_scores(i,j)

total = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if (map[i][j] == 0):
            total += score_map[i][j]
print(total)
