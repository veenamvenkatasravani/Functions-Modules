lambda arguments: expressions

#lambda —keyword used to create the function.
#arguments — input values.
#: — separates inputs from the expression.
#expression — calculation or value returned by the function.

square = lambda x: x*x

print(square(5))
print(square(10))

#Addition of two numbers

add = lambda a,b: a + b
print(add(10, 20))

#Even or odd

check = lambda n: "Even" if n%2 == 0 else "Odd"

print(check(8))
print(check(7))