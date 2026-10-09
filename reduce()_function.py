#The reduce() function repeatedly combines items in an iterable to produce a single accumulated result.
#Unlike map() and filter(), reduce() must be imported from the functools module.

#Sum of All Numbers

from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a + b, numbers)

print(result)


#Product of All Numbers

from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a * b, numbers)
print(result)

#Find the Largest Number

from functools import reduce

numbers = [10, 45, 20, 80, 30]

result = reduce(lambda a, b: a if a > b else b, numbers)

print(result)

#Using an Initial Value

from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers, 10)

print(result)