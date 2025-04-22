from collections import deque


with open("Day 16\Day16.txt") as file:
    lines = file.read().strip().split("\n")

valves = {}
tunnels = {}

for line in open("Day 16\Day16.txt"):
    line = line.strip()
    valve = line.split()[1]
    flow = int(line.split(";")[0].split("=")[1])
    targets = line.split("to ")[1].split(" ", 1)[1].split(", ")

    #print(valve, flow, targets)
    #insert in dictionaries

    valves[valve] = flow
    tunnels[valve] = targets

#print(valves)
#print(tunnels)

#compress graph to remove nodes with flow 0

dists = {}
nonempty = []

for valve in valves:

    if valve != "AA" and not valves[valve]:
        continue

    if valve != "AA":
        nonempty.append(valve)

    dists[valve] = {valve: 0, "AA": 0}

    visited = {valve}

    queue = deque([(0, valve)])

    while queue:
        distance, position = queue.popleft()
        for neighbor in tunnels[position]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            if valves[neighbor]:
                dists[valve][neighbor] = distance + 1
            queue.append((distance + 1, neighbor))

    del dists[valve][valve]
    if valve != "AA":
        del dists[valve]["AA"]

#print(dists)

#Brute force, track time, flow and open nodes. DFS 

#Cache the routes

indices = {}

for index, el in enumerate(nonempty):
    indices[el] = index

print(nonempty)
print(indices)

cache = {}

def dfs(time, valve, bitmask):
    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]

    maxval = 0
    for neighbor in dists[valve]:
        print(indices[neighbor])
        bit = 1 << indices[neighbor]
        print(bit)
        print("-----")
        if bitmask & bit:           # these overlay bitmask and bit and see if they overlap for bit position
            continue
        remtime = time - dists[valve][neighbor] - 1
        if remtime <= 0:
            continue
        #print(bitmask, bit)
        #print(maxval)
        maxval = max(maxval, dfs(time, neighbor, bitmask | bit) + valves[neighbor] * remtime)


    cache[(time, valve, bitmask)] = maxval
    return maxval

print(dfs(30, "AA", 0))
