import re

with open('2024\Day3\Day3 Input.txt') as file:
    lines = file.read().splitlines()
    
def part1():
    pattern = r"mul\((-?\d+),\s*(-?\d+)\)"    

    result = []
    total = 0

    for l in lines:
        matches = re.findall(pattern, l)
        result += [(int(a), int(b)) for a, b in matches]

    for a, b in result:
        total += a*b

    return total

def part2():
    
    pattern = r"(do\(\))|(don't\(\))|(mul\((-?\d+),\s*(-?\d+)\))"
    
    matches = []
    
    for l in lines:
        matches += re.findall(pattern, l)
    
    counted_switch = True
    valid_results = []
    total = 0
    
    print(matches)
    
    for match in matches:
        if match[0] == "do()":
            counted_switch = True
        elif match[1] == "don't()":
            counted_switch = False
        elif match[2].startswith("mul") and counted_switch:
            valid_results.append((int(match[3]), int(match[4])))
    
    print(valid_results)
    
    for a, b in valid_results:
        total += a*b
    
    return total


print(part2())

    