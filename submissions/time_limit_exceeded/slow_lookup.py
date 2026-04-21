#!/usr/bin/python3

n = int(input())
arr = list(map(int, input().split()))

visited = {}

for i in range(n):
    visited[i] = False

l = ""
for _ in range(n * n):
    l += "a"

current = 0
while True:
    if current == n - 1:
        print("Valid")
        break

    if current < 0 or current >= n:
        print("Impossible")
        break

    for key, val in visited.items():
        if val:
            if key == current:
                print("Endless")
                break

    visited[current] = True

    current = arr[current]
