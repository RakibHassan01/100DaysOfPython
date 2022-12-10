# String are immutable

a = "Rakib...."
# print(len(a))
# print(a)
# print(a.upper())
# print(a.lower())
# str2 = "Silver Spoon"
# print(str2.split(" "))      #Splits the string at the whitespace " ".
# print(a.rstrip('.'))
# str3 = "Hello !!!"
# print(str3.rstrip("!"))
# print(a.replace('Rakib....', 'harry,,,,.'))
# blogHeading = 'introduction tO jAvaScript'
# print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(str1.center(50))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())