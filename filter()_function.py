#filter(function, iterable)

#filter even number

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def is_even(n):
    return n%2 == 0

result = filter(is_even, numbers)

print(list(result))

#1 % 2 == 0 is false, so 1 is excluded.
#2 % 2 == 0 is true, so 2 is included.
#The same check is performed for every number.
#Only even numbers remain.