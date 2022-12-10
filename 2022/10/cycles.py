with open('input.txt', 'r') as f:
    ops = f.read().splitlines()

strengths = []

crt = []
c = 1
val = 1
for op in ops:
    if op == 'noop':
        cycle = 1
        inc = 0
    else:
        cycle = 2
        inc = int(op.split(' ')[-1])
     
    print(inc)
    for i in range(cycle):
        if val - 1 <= len(crt) % 40 <= val + 1:
            crt.append('#')
        else:
            crt.append('.')

        print(c, val, i)

        if c % 40 == 20:
            strengths.append(val * c)

        c += 1

    val += inc
        

print(strengths)
print(sum(strengths))
print(''.join(crt[:40]))
print(''.join(crt[40:80]))
print(''.join(crt[80:120]))
print(''.join(crt[120:160]))
print(''.join(crt[160:200]))
print(''.join(crt[200:]))
