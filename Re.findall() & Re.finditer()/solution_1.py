# Solution from the comment:
# https://www.hackerrank.com/challenges/re-findall-re-finditer/forum/comments/99146

import re


v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"


def find_vowels():
    m = re.findall(rf"(?<=[{c}])([{v}]{{2,}})[{c}]", input(), flags=re.I)
    print('\n'.join(m) or '-1')