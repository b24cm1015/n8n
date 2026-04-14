def get_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

def find_max(numbers):
    max_val = 0
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

def reverse_string(s):
    return s

print(get_average([]))
print(find_max([-5, -3, -1]))
print(reverse_string("hello"))
