numbers = [10, 15, 20, 25, 30, 35]

result = filter(lambda x: x > 20, numbers)

print(list(result))


#Filter Positive Numbers

numbers = [-10, 5, -3, 8, 0, 12]

result = filter(lambda x: x > 0, numbers)

print(list(result))

#Filter Names Starting with A

names = ["Anu", "Ravi", "Akhil", "Sravani", "Arun"]

result = filter(lambda name: name.startswith("A"), names)

print(list(result))