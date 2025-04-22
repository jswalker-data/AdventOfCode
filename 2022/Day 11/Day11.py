

with open("Day11.txt") as file:
    raw_data = file.read().strip()

    #know dodgy name but needed singluar below, shoot me
    monkey_splits = raw_data.split("\n\n")

#print(monkeys_split)

#waiting for the classes to be added
monkeys = []

#def operation to the operation for worry level
#i.e transofrm worry level using criteria

# create a base class for a monkey
class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0

    def __str__(self):
        return f"{self.item}, {self.operation}, {self.test}"


for i, monkey_split in enumerate(monkey_splits):
    lines = monkey_split.split("\n")

    #the [2:] is to remove the spaces at the start
    items = list(map(int, lines[1][2:].split(" ", 2)[2].split(", ")))
    operation = lines[2][2:].split(" ", 3)[3].split(" ")

    # work out test
    mod = int(lines[3][2:].split(" ")[-1])
    if_true = int(lines[4][2:].split(" ")[-1])
    if_false = int(lines[5][2:].split(" ")[-1])

    # wrap it into the class
    monkeys.append(Monkey(
        items,
        operation,
        [mod, if_true, if_false]
    ))


BigAssMod = 1
for monkey in monkeys:
    BigAssMod *= monkey.test[0]


def expr(operation, x):
    left, op, right = operation

    assert left == "old" #assumed as i looked at the inputs

    if op == "+":
        ans = x + int(right)

    else:
        if right == "old":
            ans = x * x
        
        else:
            ans = x * int(right)

    return ans % BigAssMod            





# Now run the rounds 
N = len(monkeys)

for round in range(10000):
    for i in range(N):
        monkey = monkeys[i]
        for item in monkey.items:

            item = expr(monkey.operation, item)
            #item //= 3

            mod, if_true, if_false = monkey.test
            if item % mod == 0:
                monkeys[if_true].items.append(item)
            else:
                monkeys[if_false].items.append(item)

            monkey.inspections += 1

        #empty item list
        monkey.items = []

    print(round)


amounts = [m.inspections for m in monkeys]
sorted_amts = sorted(amounts)
print(sorted_amts[-1] * sorted_amts[-2])


print(BigAssMod)






