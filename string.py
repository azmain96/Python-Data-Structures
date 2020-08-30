str = 'i am abdullah hel azmain. i love to learn python.'
print(str.capitalize())
print(str.upper())
print(str.lower())
print(str.replace('i am', 'This is'))
print(str.find('azmain'))
print(str.lstrip('azmain'))
print(str.rstrip('love'))
pos = str.find('love')
print(pos)
print(str.strip())

string = ' xoxo love xoxo '
print(string.strip())
print(string.strip(' xoe'))
print(string.strip(' xolve'))
print(str.strip('i a'))
dic = {'a': 2, "a": 3}
n = dic['a']
print(n)
print(str.startswith('i'))
print(str.endswith('python'))

apos = str.find('a')
print(apos)
bpos = str.find("b")
print(bpos)
sppos = str.find(' ', bpos)
print(sppos)
name = str[bpos - 1:sppos]
print(name)

abc = 'With three word'
stuff = abc.split()
print(stuff)
for x in stuff:
    print(x)
line = 'A lot      of space'
print(line)
etc = line.split()
print(etc)
line = 'First;Second;Third'
thing = line.split()
print(thing)
print('Length of thing', len(thing))
thing = line.split(';')
print(thing)
print('Length of thing', len(thing))
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
print('Line:',  line)
word = line.split()
email = word[1]
pieces = email.split('@')
print('Sliceing only host part from the line:', pieces[1])