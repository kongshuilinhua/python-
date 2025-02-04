import random

def find_kth_element(arr, rk):
    if len(arr) <= 1:
        return arr[0]

    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if rk < len(left):
        return find_kth_element(left, rk)
    elif rk < len(left) + len(middle):
        return pivot
    else:
        return find_kth_element(right, rk - len(left) - len(middle))

