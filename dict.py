fruit={"apple":"red","mango":"yellow","grapes":"green"}
print(fruit)
print(fruit["apple"])
a=len(fruit) #print lengh of dict
print(a)
s=fruit.items()
print(s) #list of tuple as key value pair
print(fruit.keys()) #list of key
print(list(fruit.keys())[1]) #get 2nd ele of keys
fruit.update({"c":"pink"}) #adding new element in dict
print(fruit)
fruit.pop('c') #delete specifed key pair
print(fruit)
for key in fruit.keys():
    print(f'type of {key} is {type(key)}')
