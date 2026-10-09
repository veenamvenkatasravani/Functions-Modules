def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()

#global keyword
x = 10

def update():
    global x
    x = 50

update()

print(x)

#without global keyword

x = 10

def update():
    x = 50
    print("Inside:", x)

update()

print("Outside:", x)
