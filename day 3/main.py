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
        
instruction = ""
with open("day 3/input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        instruction = instruction + line
print(parse_instruction(instruction))
