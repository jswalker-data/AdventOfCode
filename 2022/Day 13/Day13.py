from functools import cmp_to_key

with open("Day13.txt") as file:
    parts = file.read().strip().split("\n\n")

with open("Day13.txt") as file:
    bigparts = file.read().strip().replace("\n\n", "\n").split("\n")


#print(parts[1])


# define comparable between 2 vales, 1 is right order, 0 is if a == b and -1 if wrong order
def comp(a,b):

    #Convert types first to match
    if isinstance(a, list) and isinstance(b, int):
        b = [b]

    if isinstance(a,int) and isinstance(b, list):
        a = [a]

    #Compare
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        if b == a:
            return 0
        return -1

    if isinstance(a,list) and isinstance(b,list):
        i = 0
        while i < len(a) and i < len(b):
            x = comp(a[i], b[i])
            if x == 1:
                return 1
            if x == -1:
                return -1

            i += 1

        if i == len(a):
            if len(a) == len(b):
                return 0
            return 1

        return -1

answer = 0

for i, block in enumerate(parts):
    a, b = map(eval, block.split("\n"))
    if comp(a, b) == 1:
        #print(i+1)
        answer += i + 1

#print(answer)


#====  part 2  ======

#Convert to big list with all elements
BigList = list(map(eval, bigparts))
BigList.append([[2]])
BigList.append([[6]])
BigList = sorted(BigList, key=cmp_to_key(comp), reverse = True)

#Find divider packets

for i, el in enumerate(BigList):
    #print(i+1, "\t", el)

    if el == [[2]]:
        a = i+1

    if el == [[6]]:
        b = i + 1

print(a,b)

print(104*198)


