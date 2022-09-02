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
original = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict = { k:v for k,v in original.items() if v%2!=0 if v>40 }
print(new_dict)

days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

# Creating a dictionary of weekly tempertaures
week_temp = {k:v for (k,v) in zip(days,temp_C)}
print(week_temp)
print(week_temp["Thursday"])


discount_dict= {'Alex': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}
customer = {customer:discount for (customer, discount) in discount_dict.items() if discount<30}
print(customer)