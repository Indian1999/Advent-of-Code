from functools import cache
def blink():
    global stones
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) & 1 == 0:
            new_stones.append(int(str(stone)[:len(str(stone))//2]))
            new_stones.append(int(str(stone)[len(str(stone))//2:]))
        else:
            new_stones.append(stone*2024)
    stones = new_stones[:]
"""
@cache
def stone_split(num:int, n:int)->int:
    start_stones = [num]
    new_stones = []
    for i in range(n):
        for stone in start_stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) & 1 == 0:
                new_stones.append(int(str(stone)[:len(str(stone))//2]))
                new_stones.append(int(str(stone)[len(str(stone))//2:]))
            else:
                new_stones.append(stone*2024)
        start_stones = new_stones[:]
    return start_stones
"""
@cache
def stone_split(num:int, n:int) -> int:
    new_stones = []
    if num == 0:
        new_stones.append(1)
    elif len(str(num)) & 1 == 0:
        new_stones.append(int(str(num)[:len(str(num))//2]))
        new_stones.append(int(str(num)[len(str(num))//2:]))
    else:
        new_stones.append(num*2024)
    return len(new_stones)

def blink2():
    global stones
    new_stones = []
    for stone in stones:
        new_stones.extend(stone_split(stone))
    stones = new_stones[:]

stones = [3935565, 31753, 437818, 7697, 5, 38, 0, 123]
#stones = [0, 1, 10, 99, 999]
#Blink 25 times: result - 207683
for i in range(25):
    blink()
    print(i)
print(len(stones))


