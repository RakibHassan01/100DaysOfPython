class Person:
    name ='rakib'
    occupation = 'Software Developer'
    net_worth = 10
    
    def info(self):
        print(f'{self.name} is a {self.occupation}')
    



a = Person() 
b = Person() 
# a.name = 'RHB'
# a.occupation = 'GG'
b.name = 'Jessica'
b.occupation ='HR'
# print(a.name, a.occupation)
a.info()
b.info()