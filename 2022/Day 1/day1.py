
# Get data

with open('Day 1\day1.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

print(data)

# Traverse string 
count = 0
max = 0
max2 = 0
max3 = 0

for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num
        
    if count > max:
        max3 = max2
        max2 = max
        max = count

    elif count>max2:
        max3 = max2
        max2 = count

    elif count>max3:
        max3 = count



print("Answer to part 1 is:", max)
print("Answer to part 2 is:", max+max2+max3)


    