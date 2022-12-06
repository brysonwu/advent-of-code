with open('input.txt', 'r') as f:
    msg = f.read()

for i in range(len(msg)):
    l1 = len(set(msg[i: i+14]))
    l2 = len(msg[i: i+14])

    if l1 == l2:
        print(msg[i:i + 14])
        print(i + 14)
        break
