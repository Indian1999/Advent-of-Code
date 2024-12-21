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


total = 0
for num, operands in equations.items():
    n_operands = len(operands)
    n_operators = n_operands - 1
    for i in range(0, 2**n_operators):
        bin_i = bin(i)[2:]
        while (len(bin_i) < n_operators):
            bin_i = "0" + bin_i
        arrangement = bin_i.replace("0", "+").replace("1", "*")
        equation = [str(item) for pair in zip(operands, arrangement) for item in (pair[0], ")", pair[1])] + [str(operands[n_operators])]
        equation = "".join(equation)
        equation += ")"
        equation = n_operands*"(" + equation
        if eval(equation) == num:
            total += num
            break
print(total)


#part1: 5512534574980 CORRECT