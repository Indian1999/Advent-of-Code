"""
reports = [
    [7, 6, 4, 2, 1], #safe
    [1, 2, 7, 8, 9], #unsafe
    [9, 7, 6, 2, 1], #unsafe
    [1, 3, 2, 4, 5], #unsafe
    [8, 6, 4, 4, 1], #unsafe
    [1, 3, 6, 7, 9]  #safe
]
A report is safe if all numbers are increasing or decreasing
the increase/decrease has to be 1, 2, 3, so two 4s can't be next to each other
"""

def is_safe(report:list[int], joker:bool = True) -> bool:
    def error(i):
        if joker:
            safe_without_first = is_safe(report[1:], False)
            return safe_without_first or is_safe(report[:i] + report[i+1:], False)
        return False
    increasing = False
    if report[0] < report[1]:
        increasing = True
    for i in range(1, len(report)):
        if increasing and report[i] <= report[i-1]:
            return error(i)
        if increasing and report[i] - 3 > report[i-1]:
            return error(i)
        if not increasing and report[i] >= report[i-1]:
            return error(i)
        if not increasing and report[i] + 3 < report[i-1]:
            return error(i)
    return True

reports = []
with open("day 2/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        split_line = line.split()
        report = [int(item) for item in split_line]
        reports.append(report)

"""
reports = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9], 
    [9, 7, 6, 2, 1], 
    [1, 3, 2, 4, 5], 
    [8, 6, 4, 4, 1], 
    [1, 3, 6, 7, 9]
]"""
counter = 0
for report in reports:
    if is_safe(report):
        counter += 1

#part1: 220
#part2: INCORRECT 295
print(counter)