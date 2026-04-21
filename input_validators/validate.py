import sys
import re

n_line = sys.stdin.readline()
if not re.fullmatch(r"[1-9][0-9]*\n", n_line):
    print("expected single integer n", file=sys.stderr)
    sys.exit(43)

n = int(n_line)
if n < 2:
    print("integer n must be at least 2", file=sys.stderr)
    sys.exit(43)

arr_line = sys.stdin.readline().rstrip("\n")

if not re.fullmatch(r"(0|(-?[1-9][0-9]*))( (0|(-?[1-9][0-9]*)))*", arr_line):
    print("expected integers separated by single spaces", file=sys.stderr)
    sys.exit(43)

arr = arr_line.split(" ")

if len(arr) != n:
    print("array length does not match n", file=sys.stderr)
    sys.exit(43)

extra = sys.stdin.read()
if extra.strip():  # anything left in the file after the two lines?
    print("extra data at end of file", file=sys.stderr)
    sys.exit(43)

sys.exit(42)
