# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode


import string
import random
# from random import randint


str = input('Enter your message: ')
words = str.split(' ')
# jn = ''.join(words)
# print(words)
# print(jn)

coding = input('1 for Coding or 0 for decoding')
coding = True if (coding == '1') else False
print(coding)

letters = string.ascii_letters + string.digits
rand1 = ''.join(random.choice(letters) for i in range(3))
rand2 = ''.join(random.choice(letters) for i in range(3))

if (coding):
    nwords = []
    for word in words:
        if (len(word) >= 3):
            stnew = rand1 + word[1:] + word[0] + rand2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(' '.join(nwords))
else:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(' '.join(nwords))
