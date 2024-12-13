import numpy as np
import pulp

with open("day 13/input.txt", "r", encoding="utf-8") as f:
    file = f.readlines()

machines = []
for i in range(0, len(file), 4):
    equation = []

    data = file[i].split("X+")[1]
    data = data.split(", Y+")
    equation.append((int(data[0]), int(data[1])))
    
    data = file[i+1].split("X+")[1]
    data = data.split(", Y+")
    equation.append((int(data[0]), int(data[1])))

    data = file[i+2].split("X=")[1]
    data = data.split(", Y=")
    equation.append((int(data[0]), int(data[1])))

    machines.append(equation)

solutions = []
for item in machines:
    lp = pulp.LpProblem("KeyPresses", pulp.LpMinimize)

    x1 = pulp.LpVariable("x1", lowBound=0, cat="Integer")
    x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")

    lp += x1 + 3*x2
    lp += item[0][0]*x1 + item[1][0]*x2 == item[2][0] + 10000000000000 # + for part2
    lp += item[0][1]*x1 + item[1][1]*x2 == item[2][1] + 10000000000000 # + for aprt2

    solver = pulp.PULP_CBC_CMD(msg=False)
    status = lp.solve(solver)
    if status == 1:
        print("Optimal solution:")
        print(f"x1 = {pulp.value(x1)}")
        print(f"x2 = {pulp.value(x2)}")
        solutions.append((int(pulp.value(x1)), int(pulp.value(x2))))
    else:
        solutions.append("NaN")

def calculate_tokens(lista):
    total = 0
    for item in lista:
        if item != "NaN":
            total += 3*item[0] + item[1]
    return total

print(solutions)
print(calculate_tokens(solutions))


#part 1: 29201 CORRECT
#part 2: 2769724810000 INCORRECT (too low)