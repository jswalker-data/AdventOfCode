#from pprint import pprint
from collections import defaultdict
from functools import lru_cache


with open('Day7.txt') as file:
    blocks = ("\n" + file.read().strip()).split("\n$ ")[1:]

#print(commands[3])

path = []

dir_size = defaultdict(int)
offspring =  defaultdict(list)

def parse(block):
    lines = block.split("\n")
    command = lines[0]
    outputs = lines[1:]

    parts = command.split(" ")
    op = parts[0]

    if op == 'cd':
        if parts[1] == "..":
            path.pop()

        else:
            path.append(parts[1])

        return

    abspath = "/".join(path)

    assert op == "ls"

    sizes = []

    for line in outputs:
        if not line.startswith("dir"):
            sizes.append(int(line.split(" ")[0]))
        else: 
            dir_name = line.split(" ")[1]
            offspring[abspath].append(f"{abspath}/{dir_name}")

    dir_size[abspath] = sum(sizes)


for block in blocks:
    parse(block)

# Do DFS

#recursive cache
@lru_cache(None)
def dfs(abspath):
    size = dir_size[abspath]
    for child in offspring[abspath]:
        size += dfs(child)
    return size

ans = 0

for abspath in dir_size:
    if dfs(abspath) <= 100000:
        ans += dfs(abspath)

print(ans)

#=== Part 2 ===

#subtract root dir
unused = 70000000 - dfs("/")
required = 30000000 - unused

#initialise to stupid number to help witth minimisation
ans = 1 << 60
for abspath in dir_size:
    size = dfs(abspath)
    if size >= required:
        ans = min(ans,size)

print(ans)




