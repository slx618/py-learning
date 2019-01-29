def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if( arr[i] < smallest):
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selecionsort(arr):
    new_arr = []
    for i in range(len(arr)):
        index = findsmallest(arr)
        new_arr.append(arr.pop(index))
        print(index)
        print(arr)
    return new_arr


print(selecionsort([9, 45, 11, 6, 7, 2]))