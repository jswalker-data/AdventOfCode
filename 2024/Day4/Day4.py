
with open('2024\Day4\Day4 Input.txt') as f:
    mat = f.read().splitlines()
    

x = len(mat[0])
y = len(mat)

for j in range(y):
    for i in range(x):
        if mat[i][j] == 'X':
            
