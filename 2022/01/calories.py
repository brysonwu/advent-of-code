from pathlib import Path

input = Path(__file__).parent / 'input.txt'

with open(input, 'r') as f:
    inputs = f.read().split('\n\n')

inputs = [[int(n) for n in input.split('\n')] for input in inputs]
sums = [sum(input) for input in inputs]

# Part I Solution
print(max(sums))

# Part II Solution
print(sum(sorted(sums)[-3:]))
