
#Get data 
with open("Day9.txt") as file:
    lines = file.read().strip().split("\n")

#print(lines)

hx, hy = 0, 0
tx, ty = 0, 0

knots = [[0,0] for _ in range(10)]


# Function to check if touching 

def touching(x1, y1, x2, y2):
    return abs(x1-x2)<=1 and abs(y1 - y2)<=1

#move by 1, can multiply when needed

def move(dx, dy):
    global knots

    knots[0][0] += dx
    knots[0][1] += dy

    for i in range(1,10):
        hx, hy = knots[i-1]
        tx,ty = knots[i]    

        if not touching(hx, hy, tx, ty):
            move_x = 0 if hx == tx else (hx-tx)/abs(hx-tx)
            move_y = 0 if hy == ty else (hy-ty)/abs(hy-ty)

            tx += move_x
            ty += move_y

        knots[i] = [tx,ty]

movements = {
    "R": [1,0],
    "U": [0,1],
    "L": [-1,0],
    "D": [0,-1]
}

tail_visited = set()
tail_visited.add(tuple(knots[-1]))

for line in lines:
    dir, amount = line.split(" ")
    amount = int(amount)
    dx,dy = movements[dir]

    for _ in range(amount):
        move(dx,dy)
        tail_visited.add(tuple(knots[-1]))

print(len(tail_visited))



