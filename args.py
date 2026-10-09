# *args
#multiple positional arguments accept the *args


def add_numbers(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total

print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))