def sort(arr):
    """
    >>> sort([4, 3, 1, 2])
    [1, 2, 3, 4]
    >>> sort([9, 8, 5, 9, 7, 0, -1])
    [-1, 0, 5, 7, 8, 9, 9]
    """
    if len(arr) <= 1:
        return arr

    key = int(len(arr)/2)
    element = arr.pop(key)

    lt = [el for el in arr if not el > element]
    gt = [el for el in arr if el > element]

    return sort(lt)+[element]+sort(gt)
