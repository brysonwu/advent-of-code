from functools import reduce

with open('inputs.txt', 'r') as f:
    trees = f.read().splitlines()

def is_visible(row, col):
    if row == 0 or row == len(trees) - 1:
        return True

    if col == 0 or col == len(trees[row]) - 1:
        return True

    t = int(trees[row][col])

    for r in range(row):
        if int(trees[r][col]) >= t:
            break
    else:
        return True
    
    for r in range(row + 1, len(trees)):
        if int(trees[r][col]) >= t:
            break
    else:
        return True
    
    for c in range(col):
        if int(trees[row][c]) >= t:
            break
    else:
        return True
    
    for c in range(col + 1, len(trees[row])):
        if int(trees[row][c]) >= t:
            break
    else:
        return True


visible = 0
for row in range(len(trees)):
    for col in range(len(trees[row])):
        if is_visible(row, col):
            visible += 1

print(visible)

def find_score(row, col):
    if row == 0 or row == len(trees) - 1:
        return 0

    if col == 0 or col == len(trees[row]) - 1:
        return 0

    t = trees[row][col]
    scores = [1] * 4

    for r in range(1, row + 1):
        if trees[row - r][col] < t:
            scores[0] += 1
        else:
            break
    else:
        scores[0] -= 1
    
    for c in range(1, col + 1):
        if trees[row][col - c] < t:
            scores[1] += 1
        else:
            break
    else:
        scores[1] -= 1

    for c in range(1, len(trees[row]) - col):
        if trees[row][col + c] < t:
            scores[2] += 1
        else:
            break
    else:
        scores[2] -= 1

    for r in range(1, len(trees) - row):
        if trees[row + r][col] < t:
            scores[3] += 1
        else:
            break
    else:
        scores[3] -= 1
    
    return reduce(lambda a, b: a * b, scores)


best_tree = (-1, -1)
best_score = 0
for row in range(len(trees)):
    for col in range(len(trees[row])):
        new_score = find_score(row, col)

        if new_score > best_score:
            best_score = new_score
            best_tree = (row, col)

print(f'{best_tree}: {trees[best_tree[0]][best_tree[1]]}')
print(best_score)
