
with open("Day 10\Day10.txt") as file:
    lines = file.read().strip().split("\n")

#print(lines)

cur_x = 1
loop = 0
ans = 0

row = 0
col = 0

#value at every cycle
screen = [1] * 241

for line in lines:
    parts = line.split(" ")

    if parts[0] == "noop":
        loop += 1
        screen[loop] = cur_x

    elif parts[0] == "addx":

        #add cur_x in loop 1
        screen[loop + 1] = cur_x

        #ammend cur_x and add in loop 2
        add = int(parts[1])
        cur_x += add
        loop += 2
        screen[loop] = cur_x

# ranges from 1 -> 39
#initialise array
ans = [[None]*40 for _ in range(6)]

#print(screen)

for col in range(40):
    for row in range(6):
        counter = row * 40 + col
        if abs(screen[counter]-(col)) <= 1:
            ans[row][col] = "##"
        else:
            ans[row][col] = "  "


for row in ans:
    print("".join(row))

