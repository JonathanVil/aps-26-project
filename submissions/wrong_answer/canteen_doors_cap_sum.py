from collections import defaultdict
import sys


graph = defaultdict(lambda: defaultdict(int))
A = int(input())

for _ in range(A):
    name, p = input().split()
    capacity = int(p)
    graph["supersource"][name] = capacity

C = int(input())
canteens = []
for _ in range(C):
    name = input()
    graph[name]["supersink"] = sys.maxsize
    canteens.append(name)

D = int(input())
for _ in range(D):
    src, dst, p= input().split()
    capacity = int(p)
    graph[src][dst] = capacity

sum = 0
for room in graph.keys():
    for canteen in canteens:
        sum += graph[room][canteen]

print(sum)
