#!/usr/bin/env python3
from functools import reduce

almanac = open("input.txt").read().rstrip()
entries = almanac.split("\n\n")
seeds = list(map(int, entries[0].split(':')[1].split()))

maps = []

for mp in entries[1:]:
    m = []
    for line in mp.split("\n")[1:]:
        e, b, d = map(int, line.split())
        m.append([b, b + d - 1, e - b])
    maps.append(sorted(m))


def lookup(s, t, m):
    rs = []
    # begin, end, delta
    for b, e, d in m:
        #                          b.........e  [s-t]
        if s>e or t<b: # or: [s-t] b.........e
            continue
        if s < b: #            [s--b-----?t].e  ?t]
            rs += [(s, b - 1), (b + d, min(e, t) + d)]
        else: #                    b.[s--?t].e  ?t]
            rs += [(s + d, min(e, t) + d)]

        if e > t: return rs #      b.[s--t]..e  
        s = e
    if not rs: rs = [(s, t)]
    return rs

def process(p):
    r = [(p[0], p[0] + p[1])]
    for m in maps:
        rs = []
        for s, t in r:
            rs += lookup(s, t, m)
        r = rs
    return min(rs)[0]

locations = [process((seeds[i:i + 2])) for i in range(0, len(seeds), 2)]

print(f"result: {min(locations)}")

# todo, its fucked