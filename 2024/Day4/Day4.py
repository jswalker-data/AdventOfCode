
with open('2024\Day4\Day4 Input.txt') as f:
    mat = f.read().splitlines()
    

x = len(mat)
y = len(mat[0])

def part1():

    c = 0

    for j in range(y):
        for i in range(x):
            if mat[i][j] == 'X':
                for dx in range(-1,2,1):
                    for dy in range(-1,2,1):
                        if dx == 0 and dy == 0:
                            continue
                        
                        #Check boundary conditions met
                        if (i+(3*dx))>=0 and (j+(3*dy))>=0 and (i+(3*dx))<x and (j+(3*dy))<y:
                            if mat[i+dx][j+dy] =='M':
                                if mat[i+(2*dx)][j+(2*dy)] =='A':
                                    if mat[i+(3*dx)][j+(3*dy)] =='S':
                                        c += 1
    return c

#print(part1)

def part2():

    c = 0

    for j in range(y):
        for i in range(x):
            if mat[i][j] == 'A':
                if (i-1)>=0 and (j-1)>=0 and (i+1)<x and (j+1)<y:
                    if (mat[i+1][j+1] == 'M' and mat[i-1][j-1] == 'S') or (mat[i+1][j+1] == 'S' and mat[i-1][j-1] == 'M'):
                        if (mat[i+1][j-1] == 'M' and mat[i-1][j+1] == 'S') or (mat[i+1][j-1] == 'S' and mat[i-1][j+1] == 'M'):
                            c += 1
    return c

print(part1(), part2())
