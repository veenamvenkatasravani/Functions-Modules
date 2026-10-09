#The nonlocal keyword allows a nested function to modify a variable from its nearest enclosing function scope.

def outer():
    count = 0

    def inner():
        nonlocal count
        count = count + 1

    inner()
    print(count)

outer()