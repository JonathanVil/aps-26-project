import argparse
from collections import deque
import random
import string
import sys


def random_name(rng, used):
    used = used if used is not None else set()
    alphabet = string.ascii_lowercase + string.digits + "_"
    while True:
        n = rng.randint(3, 10)
        # First char a letter to keep names readable; not required by spec.
        name = rng.choice(string.ascii_lowercase) + "".join(
            rng.choice(alphabet) for _ in range(n - 1)
        )
        if name not in used:
            used.add(name)
            return name

def ensure_path_to_canteen(adj, sources, sinks, rng, max_cap):
    new_edges = []
    nodes = list(adj.keys())

    def reaches_sink(start):
        seen = {start}
        dq = deque([start])
        while dq:
            x = dq.popleft()
            if x in sinks:
                return True
            for y, _ in adj[x]:
                if y not in seen:
                    seen.add(y)
                    dq.append(y)
        return False

    for s in sources:
        if reaches_sink(s):
            continue
        # Build a path from source to a sink with a few intermediate nodes.
        path_len = rng.randint(1, max(1, min(4, len(nodes) // 2)))
        cur = s
        for _ in range(path_len):
            nxt = rng.choice(nodes)
            if nxt == cur or nxt in sources:  # avoid self loop / edges into sources
                continue
            cap = rng.randint(1, max_cap)
            adj[cur].append((nxt, cap))
            new_edges.append((cur, nxt, cap))
            cur = nxt
            if cur in sinks:
                break
        if cur not in sinks:
            t = rng.choice(sinks)
            cap = rng.randint(1, max_cap)
            adj[cur].append((t, cap))
            new_edges.append((cur, t, cap))
    return new_edges

def generate(A, C, D, max_students=100, max_cap=100, extra_rooms=None):
    rng = random.Random()

    extra_rooms = (A + C) // 2
    used = set()

    used = set()
    auditoriums = [random_name(rng, used) for _ in range(A)]
    canteens = [random_name(rng, used) for _ in range(C)]
    intermediate_rooms = [random_name(rng, used) for _ in range(extra_rooms)]

    students = [rng.randint(1, max_students) for _ in range(A)]

    all_nodes = auditoriums + intermediate_rooms + canteens

    adj = {n: [] for n in all_nodes}

    edges = []

    for _ in range(D):
        u, v = rng.sample(all_nodes, 2)
        capacity = rng.randint(1, max_cap)
        adj[u].append((v, capacity))
        edges.append((u, v, capacity))

    edges += ensure_path_to_canteen(adj, auditoriums, canteens, rng, max_cap)

    out = []
    out.append(str(A))
    for a, s in zip(auditoriums, students):
        out.append(f"{a} {s}")
    out.append(str(C))
    out.extend(canteens)
    out.append(str(len(edges)))
    for u, v, c in edges:
        out.append(f"{u} {v} {c}")
    return "\n".join(out) + "\n"


parser = argparse.ArgumentParser()
parser.add_argument("-A", type=int, default=3)
parser.add_argument("-C", type=int, default=2)
parser.add_argument("-D", type=int, default=8)
parser.add_argument("--max-students", type=int, default=100)
parser.add_argument("--max-cap", type=int, default=100)
parser.add_argument("--extra-rooms", type=int, default=None)
args = parser.parse_args()

text = generate(
    A=args.A,
    C=args.C,
    D=args.D,
    max_students=args.max_students,
    max_cap=args.max_cap,
    extra_rooms=args.extra_rooms,
)

sys.stdout.write(text)
