

def func(x):
    return x**2

value = int(input('Enter value: '))
lst = [i**2 for i in range(1, value + 1)]

mapping = list(map(func, lst))
print(mapping)

print (list(map(lambda x: x**2, lst)))

