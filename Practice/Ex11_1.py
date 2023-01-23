import re
doc=open('regex_sum_1609178.txt')
print(sum([int(x) for x in re.findall('[0-9]+', doc.read())]))

print sum([int(e) for e in re.findall('[0-9]+', open('regex_sum_1609178.txt').read())])
