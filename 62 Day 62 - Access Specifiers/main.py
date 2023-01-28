class Employee:
    def __init__(self) -> None:
        # self.name = 'RHB!'
        self.__name = 'RHB!'

a = Employee()
# a.emp1 = 5
# print(a.__name)  # Cant be accessed directly
print(a._Employee__name)  # Can be accessed indirectly
print(a.__dir__())



class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())