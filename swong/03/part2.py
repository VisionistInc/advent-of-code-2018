claims = {}
allClaimIDs = set()

with open('./input.txt') as file:
  for line in file:
    split = line.split()
    claimID = split[0]
    coords = split[2].split(',')
    size = split[3].split('x')

    colStart = int(coords[0])
    rowStart = int(coords[1][:-1])
    colLength = int(size[0])
    rowLength = int(size[1])

    for c in range(colLength):
      for r in range(rowLength):
        claim = 'R%dC%d' % (rowStart + r, colStart + c)

        if (claim not in claims):
          claims[claim] = [claimID]
        else:
          claims[claim].append(claimID)

        allClaimIDs.add(claimID)

for key, value in claims.items():
  if (len(value) > 1): # if len > 1, that means the tile is shared, void the entire claim
    for id in value:
      allClaimIDs.discard(id)

print('unique claim: ', allClaimIDs)
