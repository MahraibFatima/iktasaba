import re

CamelCase = input("CamelCase: ")

snake_case = re.sub(r'(?<=[a-z])([A-Z])', r'_\1', CamelCase).lower()
print (snake_case)
