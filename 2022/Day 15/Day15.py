# Just go through regio and look at what intersects with line 2000 and discard
# from list

from tqdm import tqdm
from sympy import *

with open("Day 15\Day15.txt") as file:
    lines = file.read().strip().split("\n")

sensors = []
beacons = []

for line in lines:
    split = line.split(" ")

    sx = int(split[2][2:-1])
    sy = int(split[3][2:-1])
    bx = int(split[8][2:-1])
    by = int(split[9][2:])

    sensors.append((sx, sy))
    beacons.append((bx, by))

N = len(sensors)

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1] - b[1])

dists = []

for i in range(N):
    dists.append(dist(sensors[i], beacons[i]))

Y = 2000000
intervals = []

for i, s in enumerate(sensors):

    dx = dists[i] - abs(s[1] - Y)

    if dx <= 0:
        continue

    intervals.append((s[0] - dx, s[0] + dx))

#Interval overlap

allowed_x = []
for bx, by in beacons:
    if by == Y:
        allowed_x.append(bx)


min_x = min([i[0] for i in intervals])
max_x = max([i[1] for i in intervals])

ans = 0

for x in range(min_x, max_x + 1):
    if x in allowed_x:
        continue
        
    for l, r in intervals:
        if l <= x <= r:
            ans += 1
            break

print(ans)

# === plot them all ===

 #   x, y, z, t = symbols('x y z t')
 #   inequalities = []


 #   for i in range(N):
 #       x, y, z, t = symbols('x y z t')
 #       plot = abs(x - sensors[i][0]) + abs(y - sensors[i][1]) <= dists[i]
 #       inequalities.append(plot)

 #   p1 = plot_implicit(Abs(x - 1) + Abs(y - 1) <= 1581440)

 #   print(inequalities[0])

#=== part 2 ===

pos_lines = []
neg_lines = []

for i,s in enumerate(sensors):
    d = dists[i]
    neg_lines.extend([s[0] + s[1] - d, s[0] + s[1] + d])
    pos_lines.extend([s[0] - s[1] - d, s[0] - s[1] + d])


pos = None
neg = None

for i in range(2 * N):
    for j in range(i + 2, 2 * N):
        a, b = pos_lines[i], pos_lines[j]

        if abs(a - b) == 2:
            pos = min(a, b) + 1

        a, b = neg_lines[i], neg_lines[j]

        if abs(a - b) == 2:
            neg = min(a, b) + 1        


x, y = (pos + neg) // 2, (neg - pos) //2 
ans = x * 4000000 + y
print(ans)



