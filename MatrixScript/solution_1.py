# https://www.hackerrank.com/challenges/matrix-script/problem

import re


def matrix_decode():
  first_multiple_input = input().rstrip().split()

  n = int(first_multiple_input[0])

  m = int(first_multiple_input[1])

  matrix = []

  for _ in range(n):
      *matrix_item, = input()
      matrix.append(matrix_item)

  text = [*' '*m*n]
  for i, c in enumerate(matrix):
    for j in range(m):
      text[i+j*n] = c[j]

  print(re.sub(r"\b\W*\W\b", ' ', ''.join(text)))
