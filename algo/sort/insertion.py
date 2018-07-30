def sort(arr):
    """
    >>> sort([4, 3, 1, 2])
    [1, 2, 3, 4]
    >>> sort([9, 8, 5, 9, 7, 0, -1])
    [-1, 0, 5, 7, 8, 9, 9]
    """
    sorted_arr = [arr.pop(0)]

    while arr:
        inserting = arr.pop(0)
        for k, checking in enumerate(sorted_arr):
            if checking >= inserting:
                sorted_arr.insert(k, inserting)
                break
    
    return sorted_arr

sort([4, 3, 1, 2])