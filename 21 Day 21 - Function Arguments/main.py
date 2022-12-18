# Function Arguments =>
# def average(a=2, b=3):
#     print('The average is ', (a+b)/2)


# average(4, 6)
# average(5)
# average(b=2)
# average()

# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)

# name("Amy")


# Args =>
def average(*numbers):
    # sum = 0
    # for i in numbers:
    #     sum += i
    # return sum/len(numbers)
    return sum(numbers)/len(numbers)


print(average(5, 5))
