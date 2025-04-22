
with open("Day6.txt") as file:
    input = file.read()

#print(input)


#== part 1 ==

for i in range(4,len(input)):
    s = set(input[(i-4):i])
    if len(s) == 4:
        print("Answer to part 1:", i)
        break
    

# == part 2 ==
for i in range(14,len(input)):
    s = set(input[(i-14):i])
    if len(s) == 14:
        print("Answer to part 2:", i)
        break