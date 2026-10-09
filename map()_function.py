#The map() function applies a given function to every item in an iterable, such as a list or tuple

numbers = [1, 2, 3, 4, 5]

def square(n):
    return n * n

result = map(square, numbers)

print(list(result))

# Using map() with Lambda

numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)

print(list(result))

#Convert Strings to Integers

numbers = ["10", "20", "30", "40"]

result = map(int, numbers)

print(list(result))

#Convert names to Uppercase

names = ["sravani", "ravi", "priya"]

result = map(str.upper, names)

print(list(result))