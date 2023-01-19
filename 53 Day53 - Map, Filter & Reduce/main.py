# Map =>
def cube(x):
    return x*x*x


print(cube(3))

l = [1, 2, 3, 4, 5, 6]

# newL= []
# for item in l:
#     newL.append(cube(item))

newL = list(map(cube, l))
print(newL)


# Filter =>
def filter_function(a):
    return a > 4


newL2 = list(filter(filter_function, l))
print(newL2)