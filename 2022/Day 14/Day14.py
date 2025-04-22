
with open("Day 14\Day14.txt") as file:
    lines = file.read().strip().split("\n")

#print(lines)

sand_source = 500, 0

#arrows are corners in each line

#create a set of filled coordinates
filled = set()

for line in lines:

    #initialise corrod variable
    coords = []

    #split and map all the coordinates
    for str in line.split(" -> "):
        x, y = map(int, str.split(","))
        coords.append((x, y))

    #every consecutive pair share 1 coordinate
    for i in range(1, len(coords)):
        ax, ay = coords[i]
        bx, by = coords[i - 1]

        if ay != by:
            assert ax == bx
            for y in range(min(ay, by), max(ay,by) + 1):
                filled.add((ax, y))

        if ax != bx:
            assert ay == by
            for x in range(min(ax, bx), max(ax,bx) + 1):
                filled.add((x, ay))

max_y = max([coord[1] for coord in filled])

#print(filled)
#print(max_y)

def simulate_sand():
    global filled 
    x, y = 500, 0

    while y <= max_y:
        if (x, y + 1) not in filled:
            y += 1
            continue

        if (x - 1, y + 1) not in filled:
            x -= 1
            y += 1
            continue

        if (x+1, y+ 1) not in filled:
            x += 1
            y += 1
            continue

        #everything is filled so come to rest 
        filled.add((x,y))
        return True

    return False

ans = 0

while True:
    simulation = simulate_sand()

    if not simulation:
        break

    ans += 1

print(ans)


# === Part 2 ===

filled = set()

for line in lines:

    #initialise corrod variable
    coords = []

    #split and map all the coordinates
    for str in line.split(" -> "):
        x, y = map(int, str.split(","))
        coords.append((x, y))

    #every consecutive pair share 1 coordinate
    for i in range(1, len(coords)):
        ax, ay = coords[i]
        bx, by = coords[i - 1]

        if ay != by:
            assert ax == bx
            for y in range(min(ay, by), max(ay,by) + 1):
                filled.add((ax, y))

        if ax != bx:
            assert ay == by
            for x in range(min(ax, bx), max(ax,bx) + 1):
                filled.add((x, ay))




def simulate_sand2():
    global filled 
    x, y = 500, 0

    if (x, y) in filled:
        return (x,y)

    while y <= max_y:
        if (x, y + 1) not in filled:
            y += 1
            continue

        if (x - 1, y + 1) not in filled:
            x -= 1
            y += 1
            continue

        if (x + 1, y + 1) not in filled:
            x += 1
            y += 1
            continue

        #everything is filled so come to rest 
        break

    return (x, y)


ans2 = 0

while True:

    x, y = simulate_sand2()
    filled.add((x,y))
    ans2 += 1
    
    if (x, y) == (500,0):
        break

#print(ans2)
        









