import re

doc=open('regex_sum_1609178.txt')
Total = 0
for line in doc:
    val=re.findall('[0-9]+',line)
    print(val)
    for x in val:
        Total = int(x) + Total
print(Total)
