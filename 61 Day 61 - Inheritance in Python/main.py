# Basic Syntax =>
# class Superclass:
    # Superclass attributes and methods

# class Subclass(Superclass):
    # Subclass attributes and methods

#Example =>
class Employee:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def showDetails(self):
        print(f'The name of Employee: {self.id} is {self.name}')


class Programmer(Employee):
    def showLanguage(self):
        print('The default Language is Python')


e1 = Employee('RHB Boss', 420)
e2 = Programmer('RHB Coder', 420)
e1.showDetails()
e2.showLanguage()
