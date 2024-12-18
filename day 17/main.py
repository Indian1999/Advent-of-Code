from math import floor

pointer = 0
output = []

a = 18427963
b = 0
c = 0
instructions = [2,4,1,1,7,5,0,3,4,3,1,6,5,5,3,0]
#               #   #   #   #   #   #   #   #
"""
a = 729
b = 0
c = 0
instructions = [0, 1, 5, 4, 3, 0]
"""

def get_combo_operand(num):
    if num <= 3:
        return num
    if num == 4:
        return a
    if num == 5:
        return b
    if num == 6:
        return c

def f0(num):
    global a, b, c, pointer
    a = floor(a / 2**get_combo_operand(num))
    pointer += 2

def f1(num):
    global a, b, c, pointer
    b = b ^ num
    pointer += 2

def f2(num):
    global a, b, c, pointer
    b = get_combo_operand(num) % 8
    pointer += 2

def f3(num):
    global a, b, c, pointer
    if a != 0:
        pointer = num
    else:
        pointer += 2

def f4(num):
    global a, b, c, pointer
    b = b^c
    pointer += 2

def f5(num):
    global a, b, c, pointer, output
    output.append(get_combo_operand(num) % 8)
    pointer += 2

def f6(num):
    global a, b, c, pointer
    b = floor(a / 2**get_combo_operand(num))
    pointer += 2

def f7(num):
    global a, b, c, pointer
    c = floor(a / 2**get_combo_operand(num))
    pointer += 2

while pointer < len(instructions):
    break
    instruction = instructions[pointer]
    operand = instructions[pointer + 1]
    if instruction == 0:
        f0(operand)
    if instruction == 1:
        f1(operand)
    if instruction == 2:
        f2(operand)
    if instruction == 3:
        f3(operand)
    if instruction == 4:
        f4(operand)
    if instruction == 5:
        f5(operand)
    if instruction == 6:
        f6(operand)
    if instruction == 7:
        f7(operand)
#print(output)

def loop():
    global a,b,c, output
    output = []
    while a != 0:
        b = a % 8
        b = b ^ 1
        c = a >> b
        a = a >> 3
        b = b ^ c
        b = b ^ 6
        output.append(b%8)

#From doodling on paper I deduced that the goal number is 48 bit long and the first 4 bits are 1110
# First bits: 1110000


for i in range(200000, 800000000):
    a = i
    loop()
    if len(output) >= 5 and output[-5:] == instructions[-5:]:
        print(f"a = {i} ({bin(i)[2:]}):", output)

"""
Nice try, the value of our searched value looks to be a 46-48 bit number
i = 0
while output != instructions:
    i += 1
    a = i
    if i % 100000 == 0:
        print(i)
    loop()
print(output)
"""


#part 1: 2,0,7,3,0,3,1,3,7 CORRECT