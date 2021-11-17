import re
import email.utils as emutil

def Val_email():
  count = int(input())

  for _ in range(count):
    email = input()
    name, e = emutil.parseaddr(email)

    try:
      name2, domain = e.split('@')
      dom, ext  = domain.split('.')
    except:
      continue

    if re.findall(r"[^\w\-._]", name2):
      continue
    if not name2[0].isalpha():
      continue
    if re.findall(r"[^a-zA-Z.]", domain):
      continue
    if len(ext) > 3:
      continue
    print(email)