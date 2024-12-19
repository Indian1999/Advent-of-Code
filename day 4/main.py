import numpy as np
from pprint import pprint

from_file = True
if not from_file:
    matrix = [
        ["M","M","M","S","X","X","M","A","S","M"],
        ["M","S","A","M","X","M","S","M","S","A"],
        ["A","M","X","S","X","M","A","A","M","M"],
        ["M","S","A","M","A","S","M","S","M","X"],
        ["X","M","A","S","A","M","X","A","M","M"],
        ["X","X","A","M","M","X","X","A","M","A"],
        ["S","M","S","M","S","A","S","X","S","S"],
        ["S","A","X","A","M","A","S","A","A","A"],
        ["M","A","M","M","M","X","M","M","M","M"],
        ["M","X","M","X","A","X","M","A","S","X"]
    ]
else:
    with open("day 4/input.txt", "r", encoding = "utf-8") as f:
        matrix = []
        for line in f:
            line = line.strip()
            row = []
            for char in line:
                row.append(char)
            matrix.append(row)

matrix = np.array(matrix)
texts = {
    "left_to_right": [],
    "right_to_left": [],
    "up_to_down": [],
    "down_to_up": [],
    "main_diag": [],
    "second_diag": [],
    "main_diag_rev": [],
    "second_diag_rev": []
    }

#rows
for row in matrix:
    texts["left_to_right"].append("".join(row))
    texts["right_to_left"].append("".join(row[::-1]))
matrix = matrix.T

#columns
for col in matrix:
    texts["up_to_down"].append("".join(col))
    texts["down_to_up"].append("".join(col[::-1]))
matrix = matrix.T

#main diagonals
i = len(matrix) - 4
while i >= 0:
    j = 0 
    while j <= len(matrix[0])-4:
        text = matrix[i][j] + matrix[i+1][j+1] + matrix[i+2][j+2] + matrix[i+3][j+3]
        texts["main_diag"].append(text)
        texts["main_diag_rev"].append(text[::-1])
        j += 1
    i -= 1

#secondary diagonals
i = 0
while i <= len(matrix) - 4:
    j = 3
    while j < len(matrix[0]): 
        text = matrix[i][j] + matrix[i+1][j-1] + matrix[i+2][j-2] + matrix[i+3][j-3]
        texts["second_diag"].append(text)
        texts["second_diag"].append(text[::-1])
        j += 1
    i += 1

total = 0
total += texts["main_diag"].count("XMAS")
total += texts["second_diag"].count("XMAS")
total += texts["main_diag_rev"].count("XMAS")
total += texts["second_diag_rev"].count("XMAS")
for text in texts["left_to_right"]:
    total += text.count("XMAS")
for text in texts["right_to_left"]:
    total += text.count("XMAS")
for text in texts["up_to_down"]:
    total += text.count("XMAS")
for text in texts["down_to_up"]:
    total += text.count("XMAS")

print(total)

def check_position(i,j):
    if matrix[i][j] == "A":
        if matrix[i+1][j+1] == "S" and matrix[i-1][j-1] == "M" or matrix[i+1][j+1] == "M" and matrix[i-1][j-1] == "S":
            if matrix[i-1][j+1] == "S" and matrix[i+1][j-1] == "M" or matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S":
                return True
    return False

total = 0
for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[i]) - 1):
        total += check_position(i,j)

print(total)
#part 1: 2578 CORRECT
#part 2: 1972 CORRECT

    
