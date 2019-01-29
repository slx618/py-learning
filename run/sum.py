def sum(arr):
    if len(arr) > 1:
        return arr[0] + sum(arr[1:])
    else:
        return arr[0]

print(sum([2, 3, 45, 5, 23]))

def count(arr):
    num = 1
    if( len(arr) > 1 ):
        return num + count(arr[1:])
    else:
        return 1;

print(count([4,5,6,1]))