s=[1,2,3,4,5,"r"]
p=[2,3,4]
print(s)
print(s[1])
print(s[2:5])
print(s[:5])
if 1 in s:
    print(" 1 is present")
s[1]="kiwi"
print(s)
s.append(5)
print(s)
s.insert(2,6)
print(s)
for i in s:
     print(s)
s.append(p)
print(s)

print(s.count('r'))
print(s.pop(2))
s.reverse()
print(s)
s.sort()
print(s)