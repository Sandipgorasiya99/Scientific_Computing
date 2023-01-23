Maxnumber = None
Minnumber = None
while True:
    Number= input('Number: ')
    if Number == 'Done':
        break
    try:
        Number=int(Number)
    except:
        print('Invalid input')
        continue
    if Maxnumber is None or Maxnumber < Number:
        Maxnumber = Number
    if Minnumber is None or Minnumber > Number:
        Minnumber = Number

print('Maxixum is ',Maxnumber)
print('Minmum is ',Minnumber)
