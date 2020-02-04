def search(lst, number, lower = 0, upper = None):
    if upper == None:
        upper = len(lst) - 1
    if lower == upper:
        return upper
    else:
        middle = (upper + lower) // 2
        if number < lst[middle]:
            return search(lst, number, lower, middle)
        else:
            return search(lst, number, middle + 1, upper)

seq = list(range(0,1000))
print(search(seq, 938))

    
    