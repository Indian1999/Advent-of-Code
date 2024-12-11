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

stones = [3935565, 31753, 437818, 7697, 5, 38, 0, 123]

for i in range(25):
    blink()
print(len(stones))


