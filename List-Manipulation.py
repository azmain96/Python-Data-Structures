print('Hello list')

ls = [10, 'Tazrian', [4, 5], 3.51]
print(ls)
slice = ls[:2]
print(slice)
slice = ls[1:]
print(slice)
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)
# stuff = stuff.append('45')   do not do that
# print(stuff)   it is not working
friends = ['Jhon', 'Niloy', 'Glen']
print('Original list', friends)
friends.sort()
print('Sorted list', friends)
print(friends[1])
number = [3, 8, 45, 39, 12, 9, 74, 16]
print('List of numbers:', number)
number.sort()
print('Sorted list', number)
print('Length of the list:', len(number))
print('Max value of the list:', max(number))
print('Min value of the list:', min(number))
print('Sum up all numbers:', sum(number))
print('Average value:', (sum(number)/len(number)))

