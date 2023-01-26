class MyClass:
    def __init__(self, value) -> None:
        self.value = value
        
    @property
    def value(self):
        return self._value
    
obj = MyClass(10)    

# Be Rich Be powerful :) =>