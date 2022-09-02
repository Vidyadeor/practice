#list compression
# Using list comprehension to iterate through loop
L = [x for x in [1, 2, 3]]
print(L)
#even list
li = [i for i in range(11) if i % 2 == 0]
print(li)
# using lambda to print table of 10
numbers = list(map(lambda i: i * 10, [i for i in range(1, 6)]))
print(numbers)

# Getting square of from 1 to 10
squares = [n ** 2 for n in range(1, 11)]
print(squares)
# Reverse each string in tuple
L = [string[::-1] for string in ('Geeks', 'for', 'Geeks')]
print(L)

#dict compression