allClaims = set()
prevClaimed = set()

with open('./input.txt') as file:
  for line in file:
    split = line.split()
    coords = split[2].split(',')
    size = split[3].split('x')

    colStart = int(coords[0])
    rowStart = int(coords[1][:-1])
    colLength = int(size[0])
    rowLength = int(size[1])

    for c in range(colLength):
      for r in range(rowLength):
        claim = 'R%dC%d' % (rowStart + r, colStart + c)

        if (claim in allClaims):
          prevClaimed.add(claim)

        allClaims.add(claim)

print('overlapped claims: ', len(prevClaimed))