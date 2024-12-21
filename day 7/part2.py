from_file = True
equations = {}
if not from_file:
    equations = {
        190     : [10, 19],
        3267    : [81, 40, 27],
        83      : [17, 5],
        156     : [15, 6],
        7290    : [6, 8, 6, 15],
        161011  : [16, 10, 13],
        192     : [17, 8, 14],
        21037   : [9, 7, 18, 13],
        292     : [11, 6, 16, 20]
    }
else:
    with open("day 7/input.txt", "r") as f:
        for line in f:
            line_split = line.split(":")
            num = int(line_split[0])
            operands = line_split[1].strip().split(" ")
            equations[num] = operands

def to_base3(number):
    if number == 0:
        return "0"
    digits = []
    while number:
        digits.append(str(number % 3))
        number //= 3
    return ''.join(reversed(digits))

def evaluate_equation(eq):
    while len(eq) != 1:
        a = eq[0]
        b = eq[2]
        op = eq[1]
        if op == "+":
            eq[0] = str(int(a) + int(b))
        elif op == "*":
            eq[0] = str(int(a) * int(b))
        else:
            eq[0] = a + b
        eq.pop(1)
        eq.pop(1)
    return int(eq[0])

total = 0
for num, operands in equations.items():
    print(num)
    n_operands = len(operands)
    n_operators = n_operands - 1
    for i in range(0, 3**n_operators):
        base3_i = to_base3(i)
        while (len(base3_i) < n_operators):
            base3_i = "0" + base3_i
        arrangement = base3_i.replace("0", "+").replace("1", "*").replace("2", "|")
        equation = [str(item) for pair in zip(operands, arrangement) for item in pair] + [str(operands[n_operators])]
        if (evaluate_equation(equation) == num):
            total += num
            break
print(total)


#part2: 328790210468594 CORRECT