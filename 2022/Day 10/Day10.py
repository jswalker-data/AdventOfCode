
with open("Day10.txt") as file:
    lines = file.read().strip().split("\n")

#print(lines)

x = 1
loop = 0
ans = 0

int_loops = [20, 60, 100, 140, 180, 220]

for line in lines:
    parts = line.split(" ")
    #print(parts)
    
    if parts[0] == "noop":
        loop += 1

        if loop in int_loops:
            ans += loop * x

    elif parts[0] =="addx":
        add = int(parts[1])
        x += add

        loop += 1

        if loop in int_loops:
            ans += loop * (x-add)

        loop += 1

        if loop in int_loops:
            ans += loop * (x-add)




