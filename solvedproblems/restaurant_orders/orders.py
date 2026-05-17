max_order_price = 30000

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

for item in range(1, nr_of_items + 1):
    for price in range(max_order_price + 1):
        left = possible[price][item-1]

        # we see if we've already used this item once. -1 for no and >= 0 for yeap.
        alreadyused = -1
        if price >= menu[item-1]:
            alreadyused = possible[price-menu[item-1]][item] 
        if left == -1 and alreadyused == -1: #
            continue
        elif left >= 0 and alreadyused >= 0: 
            possible[price][item] = 1 # its ambiguous - we can both get here from previous item and with current item
        else:
            possible[price][item] = 0  # there is exactly one way

def solve(x):
    global possible
    leftmostitem = len(menu)
    valid_order = []

    item = leftmostitem
    price = x 

    while True:
        value = possible[price][item]
        
        left_item = possible[price][item-1]
        if value > 0:
            print("Ambiguous")
            break
        if left_item >= 0:   
            item -= 1
        elif price - menu[item-1] >= 0 and possible[price - menu[item-1]][item] >= 0:
            price = price - menu[item-1]
            valid_order.append(item)
            if price == 0:
                valid_order.sort()
                res = map(str, valid_order)
                print(" ".join(res))
                break
        else:
            print("Impossible")
            break

for order in orders:
    solve(order)