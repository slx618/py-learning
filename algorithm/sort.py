def smallest(arr):
    smallest_index = 0
    smaller = arr[smallest_index]

    for i in range(0, len(arr)):
        if smaller >= arr[i]:
            smaller = arr[i]
            smallest_index = i

    return smallest_index


def sort(arr):
    new_arr = []

    for i in range(0, len(arr)):
        smaller_index = smallest(arr)
        new_arr.append(arr.pop(smaller_index))

    return new_arr
print(sort(range(9999,2)))