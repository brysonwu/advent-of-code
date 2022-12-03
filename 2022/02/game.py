from pathlib import Path

with open(Path(__file__).parent / 'input.txt', 'r') as f:
    hands = f.read().splitlines()

def score(hand):
    opponent_code = ord(hand[0]) - ord('A') + 1
    my_code = ord(hand[-1]) - ord('X') + 1

    if opponent_code == my_code:
        round_score = 3
    elif (opponent_code % 3) + 1 == my_code:
        round_score = 6
    else:
        round_score = 0
    
    return round_score + my_code

def alt_score(round):
    opponent_code = ord(round[0]) - ord('A') + 1

    match round[-1]:
        case 'X':
            round_score = 0
            if opponent_code == 1:
                my_code = 3
            else:
                my_code = opponent_code - 1
        case 'Y':
            round_score = 3
            my_code = opponent_code
        case 'Z':
            round_score = 6
            my_code = (opponent_code % 3) + 1
        
    return round_score + my_code

print(sum(map(score, hands)))
print(sum(map(alt_score, hands)))