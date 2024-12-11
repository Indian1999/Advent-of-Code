list_1 = []
list_2 = []

with open("day 1/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        list_1.append(int(line.split()[0]))
        list_2.append(int(line.split()[1]))
        
list_1.sort()
list_2.sort()

total = 0
for i in range(len(list_1)):
    total += abs(list_1[i]-list_2[i])
    
print("Total difference:", total)