def get_average(numbers):
    if not numbers:
        return 0.0
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

def find_max(numbers):
    if not numbers:
        raise ValueError("Cannot find max of an empty list")
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

def reverse_string(s):
    return s[::-1]

print(get_average([]))
print(find_max([-5, -3, -1]))
print(reverse_string("hello"))
