
with open("Day5.txt") as file:
    stack_strings, instructions = (i.splitlines() for i in file.read().strip("\n").split("\n\n"))

#print(stack_strings,instructions)

stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ","")}
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]


def display_stacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")


def load_stacks():
    for string in stack_strings[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] !=" ":
                stacks[stack_num].insert(0, string[index])
            stack_num += 1

def empty_stacks():
    for stack_num in stacks:
        stacks[stack_num].clear()

def getstackends():
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer


load_stacks()

# === PART 1 ===
for instruction in instructions:
    instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [int(i) for i in instruction]

    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    for crate in range(crates):
        crate_removed = stacks[from_stack].pop()
        stacks[to_stack].append(crate_removed)


print("Answer for part 1:", getstackends())

# == part 2 ==

empty_stacks()
load_stacks()

for instruction in instructions:
    instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [int(i) for i in instruction]

    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    crates_to_remove = stacks[from_stack][-crates:]             #finding what to remove
    stacks[from_stack] = stacks[from_stack][:-crates]           #removing crates

    for crate in crates_to_remove:
        stacks[to_stack].append(crate)                          #adding to different stack

    
print("Answer for part 2:", getstackends())


