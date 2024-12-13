class MyTuple(tuple):
    def __add__(self, other):
        if isinstance(other, tuple):
            return MyTuple(a + b for a, b in zip(self, other))
        return "Oopsie"


def determine_areas(matrix):
    areas = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] != "-"):
                areas.append(collapse_section(matrix, i, j, matrix[i][j]))
    return areas

def collapse_section(matrix, i,j, value):
    if i >= len(matrix) or i < 0 or j >= len(matrix[i]) or j < 0:
        return (0,0)
    if matrix[i][j] != value:
        return (0,0)
    matrix[i][j] = "-"
    return MyTuple((1,cell_perimeter(i,j))) + collapse_section(matrix, i, j-1, value) + collapse_section(matrix, i, j + 1, value) + collapse_section(matrix, i-1, j, value) + collapse_section(matrix, i+1, j, value)

def cell_perimeter(i, j):
    global mtx
    def check_cell_value(i,j, value):
        if i >= len(mtx) or i < 0 or j >= len(mtx[i]) or j < 0:
            return 1
        if mtx[i][j] != value:
            return 1
        else:
            return 0
    perim = check_cell_value(i-1,j,mtx[i][j]) + check_cell_value(i+1,j,mtx[i][j]) + check_cell_value(i,j+1,mtx[i][j]) + check_cell_value(i,j-1,mtx[i][j])
    return perim

def calculate_price(areas):
    total = 0
    for pair in areas:
        total += pair[0] * pair[1]
    return total

mtx = [
    ["R","R","R","R","I","I","C","C","F","F"],
    ["R","R","R","R","I","I","C","C","C","F"],
    ["V","V","R","R","R","C","C","F","F","F"],
    ["V","V","R","C","C","C","J","F","F","F"],
    ["V","V","V","V","C","J","J","C","F","E"],
    ["V","V","I","V","C","C","J","J","E","E"],
    ["V","V","I","I","I","C","J","J","E","E"],
    ["M","I","I","I","I","I","J","J","E","E"],
    ["M","I","I","I","S","I","J","E","E","E"],
    ["M","M","M","I","S","S","J","E","E","E"]
]
from_file = True
if from_file:
    mtx = []
    with open("day 12/input.txt", "r", encoding="utf-8") as f:
        for line in f:
            charlist = list(line)
            charlist.pop()
            mtx.append(charlist)

import copy
mtx_copy = copy.deepcopy(mtx)
print(calculate_price(determine_areas(mtx_copy)))

#part 1: 1490296 INCORRECT (too high) (There was a \n at the end of lines) + 140 * 282 (\n area and perim)
#part 1: 1450816 CORRECT