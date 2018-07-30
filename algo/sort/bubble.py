def sort(arr):
    """
    >>> sort([4, 3, 1, 2])
    [1, 2, 3, 4]
    >>> sort([9, 8, 5, 9, 7, 0, -1])
    [-1, 0, 5, 7, 8, 9, 9]
    """

    changed = True
    while changed:
        changed = False

        for k, e in enumerate(arr):
            if k+1 < len(arr) and arr[k]>arr[k+1]:
                changed = True
                arr[k], arr[k+1] = arr[k+1], arr[k]

    return arr
