#Scope determines where a variable can be accessed in a program.
#Python commonly follows the LEGB rule when resolving variable names:

#L — Local: Inside the current function.
#E — Enclosing: Inside an outer function containing a nested function.
#G — Global: At the module level.
#B — Built-in: Names provided by Python, such as print() and len().


#Local Scope

def display():
    msg = "Hello Sravani"
    print(msg)

display()

#Enclosing Scope

def outer():
    msg = "Sravani"

    def inner():
        print(msg)

    inner()

outer()


#Global Scope

message = "Hello from global scope"

def display():
    print(message)

display()
print(message)
    