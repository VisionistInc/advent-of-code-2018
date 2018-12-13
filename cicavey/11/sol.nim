import strutils
import re
import tables
import strformat

# https://www.geeksforgeeks.org/submatrix-sum-queries/

let ser = 7689

var grid: array[0..299, array[0..299, int]]

for y in 0..299:
  for x in 0..299:
    let rack = x + 10
    let p = (((((rack * y) + ser) * rack) mod 1000) div 100) - 5
    grid[x][y] = p

# Bulid aux
echo "Building sub"
var aux: array[0..299, array[0..299, int]]

for x in 0..299:
  aux[x][0] = grid[x][0]

for y in 1..299:
  for x in 0..299:
    aux[x][y] = grid[x][y] + aux[x][y-1]

for y in 0..299:
  for x in 1..299:
    aux[x][y] = aux[x][y] + aux[x-1][y]

var mc = low(int)
var mx, my, ms: int

for s in 3..299:
  echo s
  for y in 0..299-s:
    for x in 0..299-s:
      var c = aux[x+s-1][y+s-1]
      if x > 0:
        c = c - aux[x-1][y+s-1]
      if y > 0:
        c = c - aux[x+s-1][y-1]
      if x > 0 and y > 0:
        c = c + aux[x-1][y-1]
      if c > mc:
        mc = c
        mx = x
        my = y
        ms = s

echo fmt"{mx},{my},{ms} = {mc}"
