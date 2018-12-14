claims = {}
uniqueClaim = set()

with open('./input.txt') as file:
  for line in file:
    addToSet = True
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
          claims[claim] = claimID
        else: # if claim clashes, remove prev seen ID
          uniqueClaim.discard(claims[claim])
          addToSet = False

    if (addToSet): # only add claimID if no clashing tiles
        uniqueClaim.add(claimID)

print('unique claim: ', uniqueClaim)
