currTotal = 0
seen = {0}
notSeenTwice = True
freqs = []

with open('./input.txt', 'r') as file:
    for line in file:
        freqs.append(int(line))

while (notSeenTwice):
    for freq in freqs:
        currTotal += freq
        if (currTotal in seen):
            notSeenTwice = False
            print('inside if')
            break
        seen.add(currTotal)

print('freq seen twice = ', currTotal)
