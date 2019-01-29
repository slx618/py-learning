# -*- encoding: utf-8 -*-
from functools import reduce

def myreduce(num1, num2):
    return num1 * num2

print(reduce(myreduce, [2, 3, 4, 5]))