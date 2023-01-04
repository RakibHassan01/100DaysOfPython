# try:
#     l = [1, 2, 3, 5, 6]
#     i = int(input('Enter the index: '))
#     print(l[i])
# except:
#     print('Something went wrong!!')
# finally:
#     print("i'm always executed :)")




def funx():
    try:
        l = [1, 2, 3, 5, 6]
        i = int(input('Enter the index: '))
        print(l[i])
        return 1
    except:
        print('Something went wrong!!')
        return 0
    finally:
        print("i'm always executed :)")
# print("i'm always executed :)")

y = funx()
print(y)