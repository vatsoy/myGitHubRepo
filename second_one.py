def multiply(x):
    return (x*x)
def add(y):
    return (y+y)

funcs = [multiply, add]
for i in range(4):
    value = list(map(lambda z: z(i), funcs))
    print(value)

print funcs[1](3)
print map(lambda z: z(1), funcs)

