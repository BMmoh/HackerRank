import re

count = int(input())

for _ in range(count):
    n = input()
    try:
        float(n)
        print(bool(True and re.findall(r"[.]+\d+", n)))
    except:
        print(False)