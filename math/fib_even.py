def fib_even(n):
    sum = 2
    a = 1
    b = 2

    while True:
        c = 3*b + 2*a
        if c >= n:
            break
        sum += c
        a += 2*b
        b = c

    return sum

print(fib_even(100))
