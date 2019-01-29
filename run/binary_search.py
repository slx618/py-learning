import math

def binary_search(list, item):
    low = 0
    high = len(list)

    while low <= high:

        mid = math.floor((low + high) / 2)
        current = list[mid]
        if(current == item):
            return mid
        if(current > item):
            high = mid - 1
        if(current < item):
            low = mid + 1
    return None

print(binary_search([1,2,3,4,5,6,7,8], 5))