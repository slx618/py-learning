def normalize(cap):
    dict1 = {}
    dict2 = {}
    for i in range(26):
        key = chr(i + ord('a'))
        value = chr(i + ord('A'))
        dict1[key] = value
        dict1[value] = value
        dict2[value] = key
        dict2[key] = key


    for (k, v) in enumerate(cap):
        if(k == 0):
            new_word = dict1[v]
        else:
            new_word += dict2[v]

    return  new_word

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# dict1 = {}
# for i in range(26):
#     key = chr(i + ord('a'))
#     value = chr(i + ord('A'))
#     dict1[key] = value
# list1 = list(dict1.keys())
# list1.sort()
# for k in list1:
#     print(dict1[k])
# print(dict)

# print(dict1)
# print(len(dict1))
