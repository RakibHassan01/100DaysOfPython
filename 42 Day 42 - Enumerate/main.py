# marks = [12, 56, 32, 98, 12,  45, 1, 4]
# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("RHB, awesome")
#     index += 1

#   Enumerate =>

marks = [12, 56, 32, 98, 12,  45, 1, 4]

for index, mark in enumerate(marks, start=1):
    print(mark)
    if (index == 3):
        print("RHB, awesome")
