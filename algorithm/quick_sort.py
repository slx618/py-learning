import math


# D&C 分而治之
def my_sum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])

# print(my_sum([2,34,3,2,3,4,5]))


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        index = math.floor(len(arr) / 2)
        pivot = arr[index]

        less = [i for i in arr[index:] if pivot <= i]
        greater = [i for i in arr[:index] if pivot > i]

        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([2,3,4]))