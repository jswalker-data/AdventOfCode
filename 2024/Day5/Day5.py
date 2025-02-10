with open('2024/Day5/Day5 Input.txt') as f:
    rules, update = f.read().split('\n\n')

rules = [r.strip() for r in rules.splitlines()]
update = [list(map(int, map(str.strip, line.split(',')))) for line in update.splitlines()]

def check_rules(num_list, rules):
    for r in rules:
        r1, r2 = map(int, r.strip().split('|'))
        
        # Ignore rules that don’t apply
        if r1 not in num_list or r2 not in num_list:
            continue  

        order = False
        for n in num_list:
            if n == r1:
                order = True  
            elif n == r2 and order:
                break  
        else:
            return False  
    
    return True  


def fix_list(num_list, rules):
    """ Reorder num_list to satisfy all rules using a stable sorting approach """
    num_list = num_list[:]  # Copy list to avoid modifying the original
    changed = True

    while changed:  # Keep fixing until no more changes
        changed = False
        for r in rules:
            r1, r2 = map(int, r.strip().split('|'))
            
            if r1 in num_list and r2 in num_list:
                i1, i2 = num_list.index(r1), num_list.index(r2)
                if i1 > i2:  # If r1 appears after r2, swap them
                    num_list[i1], num_list[i2] = num_list[i2], num_list[i1]
                    changed = True  # A change happened, so we check again

    return num_list

def check_and_fix_updates(update, rules):
    """ Checks validity of updates, fixes incorrect ones, and sums the middle elements """
    correct_sum = 0
    fixed_sum = 0

    for u in update:
        if check_rules(u, rules):
            correct_sum += u[len(u) // 2]  
        else:
            fixed_list = fix_list(u, rules)
            if check_rules(fixed_list, rules):  # Ensure the fix is valid
                fixed_sum += fixed_list[len(fixed_list) // 2]

    print(f"Total valid sequences sum: {correct_sum}")
    print(f"Total fixed sequences sum: {fixed_sum}")

check_and_fix_updates(update, rules)