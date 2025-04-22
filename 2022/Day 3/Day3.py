


from string import ascii_letters

# Get data 
with open("Day3.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

#print(data)


#iterate through data 
totalsum = 0
for rucksack in data:
    #find half
    half = len(rucksack)//2

    left = set(rucksack[:half])
    right = set(rucksack[half:])

    #print(rucksack, left, right)

    #for key, char in enumerate(ascii_letters):
    #    print(key,char)

    for priority, char in enumerate(ascii_letters):
            if char in left and char in right:
                totalsum+= priority + 1


print("Answer to part 1 is:", totalsum)


#===== Part 2 =====

totalsum=0

j=3
for i in range(0,len(data),3):
    rucksacks = data[i:j]
    j += 3
    #print(rucksacks)

    for priority, char in enumerate(ascii_letters):
        if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
            totalsum += priority +1


print("Answer to part 2 is:", totalsum)
