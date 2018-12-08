ids = []
correctIDPosition1 = -1
correctIDPosition2 = -1

with open('./input.txt') as file:
    for line in file:
        ids.append(line)

numIds = len(ids)

for i in range(numIds - 1): # don't need to check the last id
    # compare each string with every string that comes after in ids
    for j in range(numIds - i - 1):
        difference = []
        # compare each letter, note the positions of letter differences
        for a in range(len(ids[i])):
            if ids[i][a] != ids[i+j][a]:
                difference.append(a)
        if len(difference) == 1:
            correctIDPosition1 = i
            correctIDPosition2 = i+j
            break

# honestly at this point it would be faster to just print both strings out and look at the difference
print(ids[correctIDPosition1])
print(ids[correctIDPosition2])

# but to be complete, here it is programmatically
difference = []
for z in range(len(ids[correctIDPosition1])):
    if (ids[correctIDPosition1][z] != ids[correctIDPosition2][z]):
        difference.append(z)

# there should only be one value in the list, strip it out
final = ids[correctIDPosition1][:difference[0]] + ids[correctIDPosition1][difference[0] + 1:]
print(final)