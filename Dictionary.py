purse = dict()
purse['Money'] = 12
purse['Candy'] = 3
purse['Tissues'] = 75
print(purse)
print(purse['Candy'])
purse['Candy'] = purse['Candy'] + 2
print(purse['Candy'])

counts = dict()
names = ['Zqian', 'Csev', 'Tazrian', 'Csev', 'Cwen', 'Zqian', 'Tarfee', 'Cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

print(counts.get('Zqia', 'Not Found! '))

print('Cwen')
if name in counts:
    x = counts[name]
else:
    x = 0
x = counts.get(name, 0)
print(x)

counts = dict()
names = ['Zqian', 'Csev', 'Tazrian', 'Csev', 'Cwen', 'Zqian', 'Tarfee', 'Cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

for x in counts:
    print(x)

print(counts.values())
print(counts.items())

x = (0, 1, 2) < (5, 1, 2)
print(x)
y = (0, 1, 20000000) < (0, 3, 4)
print(y)
a = ('Jones', 'Sally') < ('Jones', 'Sam')
print(a)
b = ('Jones', 'Sally') > ('Adam', 'Sam')
print(b)
print(sorted(counts.items()))