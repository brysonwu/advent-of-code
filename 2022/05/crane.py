with open('input.txt', 'r') as f:
    init, moves = [p.splitlines() for p in f.read().split('\n\n')]

stacks = {n: [] for n in range(1, 10)}
for row in init[:-1]:
    for s in stacks.keys():
        if s == 1:
            c = row[s]
            if c is ' ':
                continue

            stacks[s].insert(0, c)
        else:
            c = row[1 + (s - 1) * 4]
            if c is ' ':
                continue

            stacks[s].insert(0, c)

print(*[s for s in stacks.values()], sep='\n')
for move in moves:
    _, num, _, src, _, dst = move.split(' ')

    stacks[int(dst)].extend(stacks[int(src)][-1 * int(num):])
    del stacks[int(src)][-1 * int(num):]

print()
print(*[s for s in stacks.values()], sep='\n')
print(*[s[-1] for s in stacks.values()])