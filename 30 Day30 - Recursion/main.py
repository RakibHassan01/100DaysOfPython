# factorial(6) = 6 * 5 * 4 * 3 * 2 * 1
# factorial(5) = 5 * 4 * 3 * 2 * 1
# factorial(4) = 4 * 3 * 2 * 1
# factorial(3) = 3 * 2 * 1
# factorial(0) = 1

# factorial(n) = n * factorial(n-1)


# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n-1)


# print(factorial(3))

# Fibonacci Sequence =>
# f0 = 0
# f1 = 1
# f2 = f0+f1
# f(n) = f(n-1)+f(n-2)
# 0, 1, 1, 2, 3, 5, 8....and so on

n = int(input("How many terms the user wants to print? "))
n_1 = 0
n_2 = 1
count = 0

if n <= 0:
    print(f"Please enter a positive integer, {n} is not valid number")
elif n == 1:
    print("The Fibonacci sequence of the numbers up to", n, ": ")
    print(n_1)
else:
    print('The fibonacci sequence of the numbers is:')
    while count < n:
        print(n_1)
        nth = n_1 + n_2
        n_1 = n_2
        n_2 = nth
        count = + 1
