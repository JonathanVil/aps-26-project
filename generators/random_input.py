import random

n = int(input())

print(n)

indexes = random.sample(range(-1, int(n * 1.02)), n)
for i, x in enumerate(indexes):
    if i == len(indexes) - 1:
        print(x, end="")
    else:
        print(i, end=" ")

print("\n", end="")
