import random

A = 5       # auditoriums
max_p = 50  # max people in an auditorium - also max flow per connection maybe?
R = random.randint(1,10)      # amount of rooms
C = 5       # canteens

# generate the auditoriums with [1 - max_p] people in it
auditoriums = [(f"a{i}", random.randint(1, max_p)) for i in range(A)]
#print (auditoriums)

# generate ?? rooms with a capacity of [1 - max_p]
rooms = [(f"r{i}", random.randint(1, max_p)) for i in range(R)]
#print(rooms)

# generate C canteens
canteens = [f"c{i}"for i in range(C)]

# Time to connect 
