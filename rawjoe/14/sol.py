with open('input', 'r') as file:
    input = file.read()

ROUNDS = int(input)

scores = [3,7]
elf1 = 0
elf2 = 1

while len(scores) < (ROUNDS+10):
    new_score = scores[elf1] + scores[elf2]
    if new_score > 9:
        scores.append(1)
        scores.append(new_score % 10)
    else:
        scores.append(new_score)
    elf1 = (elf1 + scores[elf1] + 1) % len(scores)
    elf2 = (elf2 + scores[elf2] + 1) % len(scores)

sol = [str(n) for n in scores[ROUNDS:ROUNDS+10]]
print("Part 1: ", ''.join(sol))

MATCH = [int(n) for n in list(input)]
MATCH_LEN = len(MATCH)

scores = [3,7]
elf1 = 0
elf2 = 1

while True:
    new_score = scores[elf1] + scores[elf2]
    if new_score > 9:
        scores.append(1)
        if scores[-MATCH_LEN:] == MATCH:
            break
        scores.append(new_score % 10)
        if scores[-MATCH_LEN:] == MATCH:
            break
    else:
        scores.append(new_score)
        if scores[-MATCH_LEN:] == MATCH:
            break
    elf1 = (elf1 + (scores[elf1] + 1)) % len(scores)
    elf2 = (elf2 + (scores[elf2] + 1)) % len(scores)

print("Part 2: ", len(scores)-MATCH_LEN)