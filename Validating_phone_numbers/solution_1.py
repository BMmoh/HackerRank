# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

count = int(input())
numbers = []

for _ in range(count):
    numbers.append(input())

def filter_lists(n):
    return 'YES' if (n[0] in '789') and (len(n) == 10) and n.isdigit() else 'NO'

print('\n'.join(map(filter_lists, numbers)))