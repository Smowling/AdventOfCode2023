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

def lookup(s, m):
    # begin, end, delta
    for b, e, d in m:
        if   s > e: continue
        elif s < b: return s
        else: return s + d
    return s

locations  = [reduce(lookup, maps, s) for s in seeds]

print(f"Result: {min(locations)}")