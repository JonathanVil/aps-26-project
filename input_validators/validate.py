import sys
import re
from collections import defaultdict

# We are building the input validator based on the constraints in the input, 
# and also under the constraint that at least one path between an auditorium and a canteen exists.

#Check A
A_line = sys.stdin.readline()
if not re.fullmatch(r"[1-9][0-9]*\n", A_line):
    print("expected single integer A", file=sys.stderr)
    sys.exit(43)

A = int(A_line)
if A < 1:
    print("integer A must be at least 1", file=sys.stderr)
    sys.exit(43)
# remember to also check upper bound

for _ in range(A):
    audit_line = sys.stdin.readline().rstrip("\n")
    # Check auditorium names
    if not re.fullmatch(r"^[a-z0-9_]+( ([1-9][0-9]*))", audit_line):
        print("expected a string and an integer separated by single spaces", file=sys.stderr)
        sys.exit(43)

#Check C
C_line = sys.stdin.readline()
if not re.fullmatch(r"[1-9][0-9]*\n", C_line):
    print("expected single integer C", file=sys.stderr)
    sys.exit(43)

C = int(C_line)
if C < 1:
    print("integer C must be at least 1", file=sys.stderr)
    sys.exit(43)
# remember to also check upper bound

for _ in range(C):
    audit_line = sys.stdin.readline().rstrip("\n")
    # Check canteen names
    if not re.fullmatch(r"^[a-z0-9_]+", audit_line):
        print("expected a lowercase string ", file=sys.stderr)
        sys.exit(43)

#Check D
D_line = sys.stdin.readline().rstrip("\n")
if not re.fullmatch(r"[1-9][0-9]*", D_line):
    print("expected single integer D", file=sys.stderr)
    sys.exit(43)


D = int(D_line)
if D < 1:
    print("integer D must be at least one", file=sys.stderr)
    sys.exit(43)
# remember to also check upper bound

graph = defaultdict(list)
for _ in range(D):
    edges_line = sys.stdin.readline().rstrip("\n")
    if not re.fullmatch(r"^[a-z0-9_]+( ([a-z0-9_])+)( ([1-9][0-9]*))", edges_line):
        print("Expected 2 string followed by 1 integer, separated by single spaces", file=sys.stderr)
        sys.exit(43)
    
    spl = edges_line.split()
    graph[spl[0]].append(spl[1])
    

#we have graph - find one path from an auditorium to a canteen
if sys.stdin.readline() != "":
    sys.exit(43)

sys.exit(42)
