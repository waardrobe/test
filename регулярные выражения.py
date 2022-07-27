import re
s = "AC/AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC"
result = re.match("AC", s)
print(result)
result = re.match("DC", s)
print(result)
result = re.search("DC", s)
print(result[0])

result = re.findall("DC", s)
print(result)

result = re.split("/", s)
print(result)

result = re.split("/", s, maxsplit=3)
print(result)

result = re.sub("A","D", s,)
result = re.fullmatch("A", s,)

s = "A"
result = re.fullmatch("A", s,)
print(result)

