with open('input.txt', 'r') as f:
    items = f.read().splitlines()

def priority(c: str):
    if c > 'a':
        priority = ord(c) - ord('a') + 1
    else:
        priority = ord(c) - ord('A') + 27
    
    return priority

def score_error(bag: str):
    c1 = sorted(bag[:len(bag) // 2])
    c2 = sorted(bag[len(bag) // 2:])

    for c in c1:
        if c in c2:
            return priority(c)

print(sum(map(score_error, items)))

s = 0
for c0, c1, c2 in (items[i:i+3] for i in range(0, len(items), 3)):
    for c in c0:
        if c in c1 and c in c2:
            s += priority(c)
            break
print(s)
