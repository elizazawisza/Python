def qsort(array):
    if len(array) <= 1:
        return array
    else:
        return qsort([x for x in array[0:-1] if x < array[-1]]) + [array[-1]] + qsort(
            list(filter(lambda x: x >= array[-1], array[0:-1])))


print(qsort([1, 3, -9, 0, 5, 8, 23, 6, -6, 0, 2, 7, 1, -4]))
