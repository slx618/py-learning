def findbiger(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if( arr[i] > max ):
            max = arr[i]
    return  max


print(findbiger([7, 5, 6, 8, 99]))


def max(arr):
    if len(arr == 2):
        return arr[0] if arr[0] > arr[1] else arr[1]

    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(max([1,3,4,56,2222,7,7,777]))