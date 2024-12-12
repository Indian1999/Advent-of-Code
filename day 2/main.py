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

def is_safe(report:list[int]) -> bool:
    increasing = False
    if report[0] < report[1]:
        increasing = True
    for i in range(1, len(report)):
        if increasing and report[i] <= report[i-1]:
            return False
        if increasing and report[i] - 3 > report[i-1]:
            return False
        if not increasing and report[i] >= report[i-1]:
            return False
        if not increasing and report[i] + 3 < report[i-1]:
            return False
    return True

reports = []
with open("day 2/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        split_line = line.split()
        report = [int(item) for item in split_line]
        reports.append(report)

counter = 0
for report in reports:
    if is_safe(report):
        counter += 1

print(counter)