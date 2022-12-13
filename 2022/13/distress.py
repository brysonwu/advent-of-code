from dataclasses import dataclass
from enum import Enum, auto
import json

from pprint import pprint

with open('input.txt', 'r') as f:
    pairs = f.read().split('\n\n')


class InOrder(Enum):
    YES = auto()
    MAYBE = auto()
    NO = auto()

@dataclass
class Packet:
    l: list

def in_order(_l, _r):
    l = _l.l if isinstance(_l, Packet) else _l
    r = _r.l if isinstance(_r, Packet) else _r

    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return True
        elif l > r:
            return False
        else:
            return None
        
    if isinstance(l, list) and isinstance(r, list):
        for n, m in zip(l, r):
            result = in_order(n, m)

            if result:
                return True
            elif result == False:
                return False
        else:
            if len(l) < len(r):
                return True
            elif len(l) > len(r):
                return False
    
    if isinstance(l, int) and isinstance(r, list):
        return in_order([l], r)
    
    if isinstance(l, list) and isinstance(r, int):
        return in_order(l, [r])


index_sum = 0
for i, pair in enumerate(pairs):
    left, right = list(map(json.loads, pair.split('\n')))

    if in_order(left, right):
        index_sum += i + 1

print(index_sum)


packets: list[Packet] = [Packet([[2]]), Packet([[6]])]
for pair in pairs:
    for packet in pair.split('\n'):
        packets.append(Packet(json.loads(packet)))


def merge_sort(ps):
    if len(ps) == 1:
        return ps

    left = merge_sort(ps[:len(ps)//2])
    right = merge_sort(ps[len(ps)//2:])

    result = []
    i = j = 0
    while len(result) < len(ps):
        if i == len(left):
            result += right[j:]
            break
        if j == len(right):
            result += left[i:]
            break

        if in_order(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    return result
        
    
packets = merge_sort(packets)
pprint(packets)
print((packets.index(Packet([[2]])) + 1) * (packets.index(Packet([[6]])) + 1))
