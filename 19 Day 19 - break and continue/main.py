# for i in range(12):

#     print('5 x ', i, '=', 5 * i)

# Break =>
# for i in range(12):
#     if (i == 11):
#         break
#     print('5 x ', i, '=', 5 * i)

# print('Stop the iteration')


# Continue =>
# for i in range(15):
#     if (i == 11):
#         print('Skip the iteration')
#         continue
#     print('5 x ', i, '=', 5 * i)



i=0
while True:
    print(i)
    i+=1
    if (i % 100 == 0):
        break
    