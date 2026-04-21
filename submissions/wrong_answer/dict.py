#!/usr/bin/python3

n = int(input())
arr = list(map(int, input().split()))

visited = {}

for i in range(n):
    visited[i] = False

current = 0
while True:
    if current == n - 1:
        print("done done")
        break

    if current < 0 or current >= n:
        print("out out")
        break

    if visited[current]:
        print("cyclic cyclic")
        break
    visited[current] = True

    current = arr[current]
