a = 330000
b = 3303
print("A") if a > b else print("=") if a == b else print("B")

c = 9 if a > b else 0
print(c)


# Syntax =>
# result = value_if_true if condition else value_if_false


x = 8
y = 10

max_value = x if x> y else y
print(max_value)

x = 8
y = 10
z = 20

max_value = x if x> y and x> z else y if y > z else z
print(max_value)
