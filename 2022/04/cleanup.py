with open('input.txt', 'r') as f:
    data = f.read().splitlines()

numbers = [[[int(n) for n in pair.split('-')] for pair in line.split(',')] for line in data]
print(numbers[6])

def find_full(lines):
    count = 0
    for (m0, M0), (m1, M1) in lines:
        l0 = M0 - m0
        l1 = M1 - m1

        if l0 > l1:
            if m1 >= m0 and M1 <= M0:
                count += 1
        else:
            if m0 >= m1 and M0 <= M1:
                count += 1

    return count

def find_any(lines):
    count = 0
    for (m0, M0), (m1, M1) in lines:
        i = []
        i.append(m1 <= m0 <= M1)
        i.append(m1 <= M0 <= M1)
        i.append(m0 <= m1 <= M0)
        i.append(m0 <= M1 <= M0)

        if any(i):
            count += 1
    
    return count

print(find_full(numbers))
print(find_any(numbers))
