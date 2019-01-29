def countdown(num):
    print(num)
    num -= 1
    if num > 0:
        countdown(num)


countdown(50)

