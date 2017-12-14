from collections import deque

def array_left_rotation(a, n, k):
    arr = deque(a, n)
    for i in range(n):
        new_index = (i + k) % n
        arr[i] = a[new_index]
    return arr

def array_left_rotation_generic(a, n, k):
    arr = deque(a, n)
    for _ in range(k):
        arr.rotate(-1)
    return arr
