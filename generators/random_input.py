import random

A = 5                       # auditoriums
max_p = 50                  # max people in an auditorium - also max flow per connection maybe?
D = random.randint(1,10)    # amount of rooms
C = 5                       # canteens

print(A)
# generate the auditoriums with [1 - max_p] people in it
auditoriums = [(f"a{i}", random.randint(1, max_p)) for i in range(A)]
for i in range(A):
    name = auditoriums[i][0]
    c = auditoriums[i][1]
    print(f"{name} {c}")

print(C)
# generate C canteens
canteens = [f"c{i}"for i in range(C)]
print("\n".join(canteens))

# generate ?? rooms with a capacity of [1 - max_p]
rooms = [(f"r{i}", random.randint(1, max_p)) for i in range(D)]
for i in range(D):
    name = rooms[i][0]
    c = rooms[i][1]
    print(f"{name} {c}")

# Make sure there are connections from auditoriums to canteens

