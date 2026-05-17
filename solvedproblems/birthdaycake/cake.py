# n candles, m cuts, r radius
n, m, r = map(int, input().split())
cakesquare = [(r,r),(r,-r),(-r,-r),(-r,r)]

candles = []
for _ in range(n):
    x, y = map(int, input().split())
    candles.append((x,y))

cuts = []
for _ in range(m):
    a, b, c = map(int, input().split())
    cuts.append((a,b,c))

success = True

# check if candle pairs are separated by a cut
for i in range(n):
    candle = candles[i]
    print(f"checking for candle {candle}")
    for j in range(i + 1, n):
        separated = False
        comparecandle = candles[j]
        print(f"comparing to candle {comparecandle}")
        for a,b,c in cuts:
            if separated:
                break
            candle_i = a*candle[0] + b*candle[1] + c
            candle_j = a*comparecandle[0] + b*comparecandle[1] + c

            print(f"candle: {candle_i} and comparecandle: {candle_j}")

            if (candle_i > 0 and candle_j < 0) or (candle_i < 0 and candle_j > 0):
                print("they are separated!")
                # they are separated! yay!
                separated = True 
            else:
                print("they are not separated :(")

        if not separated:
            success = False
            break

# check how many slices there are, if it equals the amount of candles.
slices = 2
#how the heck count slices??



if success:
    print("yes")
else:
    print("no")

