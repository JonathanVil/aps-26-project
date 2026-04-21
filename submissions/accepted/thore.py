#!/usr/bin/python3

n = int(input())
arr = list(map(int, input().split()))

visited = [False] * n

current = 0
while True:
    if current == n - 1:
        print("Valid")
        break

    if current < 0 or current >= n:
        print("Impossible")
        break

    if visited[current]:
        print("Endless")
        break
    visited[current] = True

    current = arr[current]
