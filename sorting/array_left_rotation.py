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

def array_left_rotation_slow(a, n, k):
    width = len(a)
    for _ in range(k):
        a.append(a[0])
        a = a[1:]
    return  a[:width//2] + a[width//2:]
