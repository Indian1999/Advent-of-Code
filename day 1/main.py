list_1 = []
list_2 = []

with open("day 1/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        list_1.append(int(line.split()[0]))
        list_2.append(int(line.split()[1]))
        
#list_1 = [3,4,2,1,3,3]
#list_2 = [4,3,5,3,9,3]
def part1():
    list_1.sort()
    list_2.sort()

    total = 0
    for i in range(len(list_1)):
        total += abs(list_1[i]-list_2[i])

    print("Total difference:", total)

def part2():
    total = 0
    for item in list_1:
        total += item * list_2.count(item)
    print(total)

#part1()
part2()