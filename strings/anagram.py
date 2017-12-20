from collections import deque

def number_needed(a, b):
    letter_count_a = get_letter_count(a)
    letter_count_b = get_letter_count(b)
    return get_delta(letter_count_a, letter_count_b)

def get_delta(a, b):
    delta = 0
    for i in range(26):
        delta += abs(a[i] - b[i])
    return delta

def get_letter_count(s):
    letter_count = deque([0] * 26, 26)
    for letter in s:
        offset = ord(letter) - ord('a') # Get letter index out of 26
        letter_count[offset] += 1
    return letter_count
