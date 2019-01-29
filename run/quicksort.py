def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        less = [ i for i in arr[1:] if i <= pivot ]

        more = [ i for i in arr[1:] if i > pivot ]

        return quicksort(less) + [pivot] + quicksort(more)

print(quicksort([1, 4, 2, 2, 6, 7, 3, 2, 6, 7, 8, 11, 9]))