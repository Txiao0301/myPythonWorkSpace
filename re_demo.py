import re

line = "Cats are smarter than dogs"
print(re.search(r'DOGS', line, re.M | re.I))
