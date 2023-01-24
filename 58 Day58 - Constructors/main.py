class Person :
    # name = 'Rakib'
    # occ = "Developer"
    
    def __init__(self, n, o) -> None:
        print('Hola')
        self.name = n
        self.occ = o
    
    def info(self):
        print(f'{self.name} is a {self.occ}')
        
        
a = Person('Harry', 'DEV') 
b = Person('Ritika', 'HR') 

# print(a.name)  
# a.info()     