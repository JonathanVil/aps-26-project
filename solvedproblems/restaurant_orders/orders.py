from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
max_order_price = 11

nr_of_items = int(input())
menu = list(map(int, input().split()))
m = int(input())
orders = list(map(int, input().split()))

# -1 = impossible
# 0 = possible
# 1 = ambiguous
# build matrix
possible = [[-1 for _ in range(nr_of_items + 1)] for _ in range(max_order_price + 1)]
possible[0][0] = 0
for price in range(max_order_price + 1):
    for item in range(1, nr_of_items + 1):
        if possible[price][item-1] == 0:
            # all multitudes of item shall be set to 0.
            for i in range (price, max_order_price+1, menu[item-1]):
                possible[i][item] += 1
                if i > max_order_price:
                    break 

def solve(x):
    global possible
    colon = len(menu)
    valid_order = []

    i = colon
    while (i >= 0):
        value = possible[x][i]
        if value > 0:
            print("Ambiguous")
            break
        elif value == 0:
            i -= 1
        elif value < 0:
            if (i+1) < colon and value == 0:
                valid_order.append(menu[i+1])
                x = -menu[i+1]
                i+=1
            else:
                print("Impossible")
                break
    print(valid_order)
                


    




def pretty_print(possible):
    rows = len(possible)
    cols = len(possible[0])

    # Print matrix (y reversed so 0 is at bottom)
    for price in reversed(range(rows)):
        print(f"{price:4} |", end="")  # y-axis labels on the left
        for item in range(cols):
            val = possible[price][item]
            if val == -1:
                print("   .", end="")
            else:
                print(f"{val:4}", end="")
        print()

    # Separator line
    print("      " + "----" * cols)

    # Bottom x-axis labels
    print("      ", end="")
    for item in range(cols):
        print(f"{item:4}", end="")
    print()

pretty_print(possible)

solve(6)