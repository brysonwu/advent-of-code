with open('input.txt', 'r') as f:
    moves = f.read().splitlines()

class Position:
    x = 0
    y = 0

    def follow(self, l):
        dx = l.x - self.x
        dy = l.y - self.y

        if abs(dx) <= 1 and abs(dy) <=1:
            pass
        elif abs(dx) > 1 and abs(dy) == 0:
            self.x += int(dx / abs(dx))
        elif abs(dx) == 0 and abs(dy) > 1:
            self.y += int(dy / abs(dy))
        else:
            self.x += int(dx / abs(dx))
            self.y += int(dy / abs(dy))


    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

H = Position()
T = Position()
TS = [Position() for _ in range(9)]

visits = [(0,0)]
for move in moves:
    d, n = move.split()
    print(d, n)

    match d:
        case 'U':
            sign, vert = 1, True
        case 'D':
            sign, vert = -1, True
        case 'L':
            sign, vert = -1, False
        case 'R':
            sign, vert = 1, False
    
    for m in range(int(n)):
        if vert:
            H.y += sign
        else:
            H.x += sign
        
        TS[0].follow(H)
        for i in range(1, len(TS)):
            TS[i].follow(TS[i - 1])


        if (TS[-1].x, TS[-1].y) not in visits:
            visits.append((TS[-1].x, TS[-1].y))

    print(H, TS)
    # input()
        
        
# print(sorted(visits, key=lambda c: c[1]))
print(len(visits))
