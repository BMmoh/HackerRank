import re


count = 11

s = """x&& &&& && && x || | ||\|| x"""

def repl(r: re.Match):
    return 'and' if r.group() == '&&' else 'or'

print(re.sub(r"(?<=\s)(\&{2}|\|{2})(?=\s)", repl, s))
