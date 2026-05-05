N = int(input())
heights = list(map(int, input().split()))

twiceAsLarge = [0] * N

total_messy = 0
for i, h in enumerate(heights):
    # check if there exists a, b in heights such that a >= b*2 >= h*2
    # to enable this, we could store for each index, how many values before it are at least twice as large

    count = 0
    messy = 0
    for x in range(0, i):
        if heights[x] >= h * 2:
            count += 1
            messy += twiceAsLarge[x]

    twiceAsLarge[i] = count
    total_messy += messy

print(total_messy)
