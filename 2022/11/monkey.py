import re
from dataclasses import dataclass

with open('input.txt', 'r') as f:
    monkeys = [b.split('\n') for b in f.read().split('\n\n')]

@dataclass
class Monkey:
    items: list[int]
    op: str
    val: int
    test: int
    true: int
    false: int
    inspected: int = 0

    def __post_init__(self):
        match self.op:
            case '+':
                self.op = lambda o: o + self.val
            case '*':
                self.op = lambda o: o * self.val
            case '**':
                self.op = lambda o: o ** self.val


BIGMOD = 1
monks: dict[int, Monkey] = {}
for monkey in monkeys:
    m = int(re.search(r'\d', monkey[0]).group())
    items = [int(i) for i in re.findall(r'\d+', monkey[1])]
    op, val = monkey[2].split(' ')[-2:]

    if val == 'old':
        op = '**'
        val = 2
    else:
        val = int(val)

    test = int(monkey[3].split(' ')[-1])
    true = int(monkey[4].split(' ')[-1])
    false = int(monkey[5].split(' ')[-1])

    monks[m] = Monkey(items, op, val, test, true, false)

    BIGMOD *= test


print(monks)


def inspect(m: Monkey):
    for i, item in enumerate(m.items):
        m.items[i] = int(m.op(item))
        m.inspected += 1


def manage(val, target):
    global monks

    result = val % monks[target].test

    if result == 0:
        result = val
    
    return result


def test_and_throw(m: Monkey):
    global monks

    for item in m.items:
        if item % m.test == 0:
            monks[m.true].items.append(item % BIGMOD)
        else:
            monks[m.false].items.append(item % BIGMOD)
    
    m.items = []


def round(m: Monkey):
    inspect(m)
    test_and_throw(m)

for r in range(10_000):
    for m in monks.values():
        round(m)

    if r % 19 == 0:
        print([m.inspected for m in monks.values()])

a, b = sorted(monks.values(), key=lambda m: m.inspected)[-2:]
print(a.inspected * b.inspected)
