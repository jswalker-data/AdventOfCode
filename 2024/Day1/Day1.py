
def part1():
    
    with open('2024\Day1\Day1 Input.txt') as file:
        lines = file.read().splitlines()

    first_list = []
    second_list = []

    l = len(lines)
    
    for i in range(l):
        first_list.append(int(lines[i].split('   ')[0]))
        second_list.append(int(lines[i].split('   ')[1]))

    first_list.sort()
    second_list.sort()

    s = 0
    
    for i in range(l):
        s += abs(first_list[i] - second_list[i])
    
    return s

print(part1())

def part2():
    
    with open('2024\Day1\Day1 Input.txt') as file:
        lines = file.read().splitlines()

    first_list = []
    second_list = []

    l = len(lines)
    
    for i in range(l):
        first_list.append(int(lines[i].split('   ')[0]))
        second_list.append(int(lines[i].split('   ')[1]))

    s = 0
    
    for i in range(l):
        
        n = first_list[i]
        c = second_list.count(n)
        s += c * n
    
    return s
    
print(part2())
