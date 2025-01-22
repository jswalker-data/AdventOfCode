#Open the file and split into lines
with open('2024\Day2\Day2 Input.txt') as file:
    lines = file.read().splitlines()

#Create a list of lists ill call arr and split the lines
arr = list()

for l in lines:
    int_list = list(map(int,l.split()))
    arr.append(int_list)

def is_safe(line):
    
        
    s = sorted(line)
    sr = sorted(line, reverse = True)
    a = 0
        
    #check if always increasing or decreasing
    if (s == line or sr == line):

        #Check the ranges arent too big
        for i in range(len(line)-1):
            if (abs(line[i+1] - line[i]) >= 1 and abs(line[i+1] - line[i]) <= 3):
                a +=1
                    
        #Check all pass the test
        if a == len(line)-1:
            return True
    
    return False

#Initiaite count for passing    
c = 0

#Loop over all and check if safe
for line in arr:
    c += is_safe(line)
    
print(c)

#part 2

#Same approcah but manually remove a number each time and see if safe
def is_actually_safe(line):
    if is_safe(line):
        return True
    for i in range(len(line)):
        l = (line[:i] + line[i+1:])
        if is_safe(l):
            return True
    return False

#now loop over again, new count
ans = 0
for line in arr:
    ans += is_actually_safe(line)
    
print(ans)