
# Get data 

with open("Day4.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

#print(data)

pairs = 0
for entry in data:
    first, second = entry.split(",")

    #print(first, second)

    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    #print(first,second)

    if first[0] <= second[0] and first[1] >= second[1]:
        pairs += 1
    elif first[0] >= second[0] and first[1] <= second[1]:
        pairs += 1


print("Answer for 1:", pairs)

# Part 2
pairs = 0
for entry in data:
    first, second = entry.split(",")

    #print(first, second)

    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    if first[0] is range(second[0], second[1]+1) or first[1] in range(second[0], second[1]+1):
        pairs += 1
    
    elif second[0] is range(first[0], first[1]+1) or second[1] in range(first[0], first[1]+1):
        pairs += 1

print("Answer to 2 is:", pairs)