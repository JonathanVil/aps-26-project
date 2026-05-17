import math
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
    #print(f"checking for candle {candle}")
    for j in range(i + 1, n):
        separated = False
        comparecandle = candles[j]
        #print(f"comparing to candle {comparecandle}")
        for a,b,c in cuts:
            if separated:
                break
            candle_i = a*candle[0] + b*candle[1] + c
            candle_j = a*comparecandle[0] + b*comparecandle[1] + c

            #print(f"candle: {candle_i} and comparecandle: {candle_j}")

            if (candle_i > 0 and candle_j < 0) or (candle_i < 0 and candle_j > 0):
                #print("they are separated!")
                # they are separated! yay!
                separated = True 
           

        if not separated:
            success = False
            break

slices = 0
# check how many slices there are, if it equals the amount of candles.
# base case : one cut = 2 slices. Then for each added cut - +1 and +1 for each intersecting line
for i in range(m):
    if i == 0:
        slices = 2
        continue 
    a1,b1,c1 = cuts[i]
    slices += 1
    for j in range(i):
        a2,b2,c2 = cuts[j]
        intersection = a1*b2 - a2*b1  # formula to get a value that != 0 if the lines intersect
        if intersection != 0: # they intersect! find the intersection coordinate using cool formulas!
            x = ((b1*c2)- (b2*c1))/((a1*b2) - (a2*b1)) 
            y = ((a2*c1)- (a1*c2))/((a1*b2) - (a2*b1))

            # check if its inside the circle :3 using a cool formula
            d = math.sqrt(math.pow(x,2)+math.pow(y,2))
            if d < r: # its inside the circle!
                slices +=1

if slices > n:
    success = False
if success:
    print("yes")
else:
    print("no")

