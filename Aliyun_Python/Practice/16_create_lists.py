
# Task: Create a list that contains my friend's names.

friends = ['Z', 'Lulu', 'Daqing', 'Zhouyi', 'Wood', 'Dawei', 'Dashen']

print(len(friends))
print(friends[1])

animal = 'dolphin'

print('d' in animal)
print('do' in animal)
print('don' in animal)

print(len(animal))

print(animal[0: 1])     # 'd'
print(animal[0: 2])     # 'do'
print(animal[0: 2: 1])  # 'do'
print(animal[0: 2: 2])  # 'd'
print(animal[0: 5: 2])  # 'dlh' (not 'dl')

print(animal.index('l'))  # 'l'
print(animal.index('l', 2))  # 2
print(animal.index('l', 2, 3))  # 2

print(animal.count('n'))

# (lines 14-17) remember to use colon instead of comma in brackets when slicing.

s = 'hello'
print(s[0: 2])
print(s[0: 2: 1])
print(s[0: 2: 2])
