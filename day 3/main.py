import re


def parse_instruction(instruction: str):
    start = instruction.find("mul(")
    instruction = instruction[start+4:]
    end = instruction.find(")")
    sub_instruction = instruction[:end]
    sub_instruction_split = sub_instruction.split(",")
    if len(sub_instruction_split) == 2 and sub_instruction_split[0].isdigit() and sub_instruction_split[1].isdigit():
        return int(sub_instruction_split[0])*int(sub_instruction_split[1]) + parse_instruction(instruction)
    else:
        if instruction != "":
            return 0 + parse_instruction(instruction)
        else:
            return 0
        
def handle_dos_and_donts(instruction: str) -> str:
    dont_index = instruction.find("don't()")
    do_index = instruction[dont_index:].find("do()") + dont_index
    if dont_index == -1:
        return instruction
    if do_index == -1:
        return instruction[:dont_index]
    return instruction[:dont_index] + handle_dos_and_donts(instruction[do_index+4:])

def handle_dos_and_donts_2(instruction:str)->str:
    handled_instruction = ""
    enabled = True
    for i in range(len(instruction)):
        if instruction[i] == "d":
            if i + 1 < len(instruction) and instruction[i+1] == "o":
                if i + 2 < len(instruction) and instruction[i+2] == "(":
                    if i + 3 < len(instruction) and instruction[i+3] == ")":
                        enabled = True
                        continue
        if instruction[i] == "d":
            if i + 1 < len(instruction) and instruction[i+1] == "o":
                if i + 2 < len(instruction) and instruction[i+2] == "n":
                    if i + 3 < len(instruction) and instruction[i+3] == "'":
                        if i + 4 < len(instruction) and instruction[i+4] == "t":
                            if i + 5 < len(instruction) and instruction[i+5] == "(":
                                if i + 6 < len(instruction) and instruction[i+6] == ")":
                                    enabled = False
                                    continue
        if enabled:
            handled_instruction += instruction[i]
    return handled_instruction

def string_clean_up(instruction:str)->str:
    """Abandon this, it changes the result"""
    valid_chars = "mul(),don't0123456789"
    cleaned_string = ""
    for char in instruction:
        if char in valid_chars:
            cleaned_string += char
    return cleaned_string
    
def handle_dos_and_donts_3(instruction:str)->str:
    ins_split = instruction.split("don't")
    handled_instruction = ""
    handled_instruction += ins_split[0]
    for i in range(1, len(ins_split)):
        if "do()" in ins_split[i]:
            do_index = ins_split[i].find("do()")
            handled_instruction += ins_split[i][do_index+4:]
    return handled_instruction

def regex_parse(instruction):
    matches = re.findall(r"mul\(\d+,\d+\)", instruction)
    total = 0
    for match in matches:
        nums = match[4:-1]
        nums = nums.split(",")
        a = int(nums[0])
        b = int(nums[1])
        total += a*b
    return total

def regex_dos_and_donts(instruction):
    regex = r"don't\(\).*?do\(\)"
    instruction_split = re.split(regex, instruction)
    new_instruction = ""
    for item in instruction_split:
        new_instruction += item
    return new_instruction

def regex_cleanup(instruction):
    return "".join(re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", instruction))



instruction = ""
with open("day 3/input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        instruction = instruction + line.strip()

#instruction = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undon't()do()()?mul(8,5))"

#print(instruction)
#instruction = handle_dos_and_donts_3(instruction)
#print(instruction)
#print(parse_instruction(instruction))
instruction += "do()"
instruction = regex_cleanup(instruction)
print(instruction)
instruction = regex_dos_and_donts(instruction)
print()
print(instruction)
print(regex_parse(instruction))

#part2: (with handle_dos_and_donts)               83276487 INCORRECT (too high)
#part2: (with handle_dos_and_donts_2)             82733731 INCORRECT (too high)
#part2: (with handle_dos_and_donts_2 and cleanup) 82911076 INCORRECT (too high)
#part2: (with handle_dos_and_donts and cleanup)   83453832 INCORRECT (too high)
#part2: (handle_dos_and_donts_3 results the same as the 2)

#82733683


"""
Idea for tomorrow:
insert a do() at the start and a don't() at the end
maybe something comes of it
"""