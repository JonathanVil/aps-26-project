from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

n = int(input())
menu = list(map(int, input().split()))
m = int(input())
orders = list(map(int, input().split()))

valid_order = []
ambiguous = False

itemnumber = defaultdict(int)

for i in range(len(menu)):
    itemnumber[menu[i]] = i+1

solved = defaultdict(str)
result = defaultdict(list)

def solve(x: int, path : list):
    global ambiguous
    global valid_order

    if ambiguous: return 
    if x < 0:  return
    elif x == 0: 
        if valid_order == []:
            valid_order = path.copy()
        elif valid_order != path:
            ambiguous = True
    elif solved[x] != "":
        if solved[x] == "Impossible":
            return
        if solved[x] == "Ambiguous":
            ambiguous = True
        if solved[x] == "Possible":
            valid_order = sorted(path + result[x])
    elif x > 0: 
        for item in menu: 
            next_path = path.copy()
            next_path.append(item)
            next_path.sort()
            solve(x - item, next_path)
    

res = []

for i in range(m):
    valid_order = []
    ambiguous = False
    order = orders[i]
    solve(order, [])
    if ambiguous: print("Ambiguous")
    elif valid_order == []: print("Impossible")
    else:
        for item in valid_order:
            res.append(str(itemnumber[item]))

        print(" ".join(res))

