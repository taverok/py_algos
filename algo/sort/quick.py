import random


def sort(arr):
    """
    >>> sort([4, 3, 1, 2])
    [1, 2, 3, 4]
    """
    if len(arr) <= 1:
        return arr

    key = random.randint(0, len(arr)-1)
    element = arr.pop(key)

    lt = [el for el in arr if el <= element]
    gt = [el for el in arr if el > element]

    return sort(lt)+[element]+sort(gt)
