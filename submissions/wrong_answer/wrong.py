# wrong answer where we just take the max incoming capacity to the canteens

#throw away auditoriums
totalpeople = 0
for _ in range(int(input())): 
    
    _, p = input().split()
    totalpeople += int(p)

max_cap = 0
#save the canteens!
canteens = [input().strip() for _ in range(int(input()))]
D = int(input())
for _ in range(D):
    src, dst, p = input().split()
    if dst in canteens:
        max_cap += int(p)

if totalpeople < max_cap:
    max_cap = totalpeople
print(max_cap)