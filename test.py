import os as o

list1 = []
for i in range(26):
    list1.append((chr(i + ord('a'))))

list2 = []
for i in range(26):
    list2.append(chr(i + ord('A')))

dict1 = {}
for (k, v) in enumerate(list1):
    dict1[v] = list2[k]

dict2 = {}

dict2 = dict(zip(list1, list2))

print(list1)
print(list2)
print(dict1)
print(dict2)
o.wait()
