import math as m
from datetime import datetime as dt

def binary_search(my_list, search):
    time = dt.now()
    print(time.timestamp())
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = m.floor((low + high) / 2)
        guess = my_list[mid]

        if search == guess:
            time = dt.now()
            print(time.timestamp(), 'in while')
            return mid
        # 比猜想的小
        if guess < search:
            low = mid + 1
        else:
            high = mid - 1
    time = dt.now()
    print(time.timestamp(), 'end')
    return None
print(binary_search(range(0,9010000333333333331, 21), 9))

